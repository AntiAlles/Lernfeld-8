from datetime import datetime as timedate
from time import time
from linode_api4 import *
from dotenv import load_dotenv

import smtplib
import re
import json
import os


class monitor():

    def getInstanceID():
        load_dotenv()
        # Needed Vars to call the api
        client = LinodeClient(os.getenv('TOKEN'))

        # get instance ids
        Linode_Instances = client.linode.instances()
        for Linode_Instance in Linode_Instances:
            # turn the list into a string and remove everything after the first ": "
            Linode_ID = str(Linode_Instance).split(": ")[1]

            # call the instance class with the ID and token
            my_instance = Instance(client, Linode_ID)

            # Get current stats from instance
            Current_load = my_instance.stats

            # Converting the serialized JSON into a str
            json_string = json.dumps(Current_load)

            # creating a Json datafile
            my_file = open("data.json", "w+")
            my_file.write(json_string)

    def updateLog():
        f = open('data.json')
        data = json.load(f)

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        cpu = data["data"]["cpu"][last_entry]
        io = data["data"]["io"]["io"][last_entry]
        ipv4 = data["data"]["netv4"]["in"][last_entry]
        ipv6 = data["data"]["netv6"]["in"][last_entry]

        # Convert first array item of Cpu into integer and divide it by 1000
        timestamp = int(cpu[0]/1000)
        # Print UTC timestamp of server With Year-Month-Day Hour-Minute-Seconds
        print(timedate.utcfromtimestamp(
            timestamp).strftime('%Y-%m-%d %H:%M:%S'))

        # display the cpu usage
        print("CPU:", cpu[1], "%")

        # display the io usage as blocks/s
        print("io:", io[1], "b/s")

        # display the network ipv4 usage
        print("IPv4: ", ipv4[1], "Bits/s")

        # display the network ipv6 usage
        print("IPv6: ", ipv6[1], "Bits/s")

        f.close


class Alarm():

    def send_email(subject, body):

        user = os.getenv('USER')
        pwd = os.getenv('PWD')
        recipient = os.getenv('RECIPIENT')

        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")


    def ScanCPULoad():
        f = open('data.json')
        data = json.load(f)

        #Maximum CPU Utilization in % 
        MaxLoad = 0

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        cpu = data["data"]["cpu"][last_entry]

        # display the cpu usage
        if int(cpu[1]) >= MaxLoad:
            subject = "Server Warning: CPU Load over threshold"
            body = "WARNING! CPU Load on server exceeded threshold! Current server load:", cpu[1]
            Alarm.send_email(subject, body)
            print("ALARM JUNGE CPU IST BEI:", cpu[1], "%")

    def ScanIoUsage():
        f = open('data.json')
        data = json.load(f)

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        io = data["data"]["io"]["io"][last_entry]

        # display the cpu usage
        print("CPU:", io[1], "%")