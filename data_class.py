from asyncio.log import logger
from datetime import datetime as timedate
from email import message
from time import *
from linode_api4 import *
from dotenv import load_dotenv

import smtplib
import logging
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
        
        # function to get the IDs of the Linode Instances 
        monitor.getInstanceID()

        #Open and map data.json
        f = open('data.json')
        data = json.load(f)

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        cpu = data["data"]["cpu"][last_entry]
        io = data["data"]["io"]["io"][last_entry]
        ipv4 = data["data"]["netv4"]["in"][last_entry]
        ipv6 = data["data"]["netv6"]["in"][last_entry]

        #Configure the logging method
        logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(message)s', force=True)
        
        # Convert first array item of Cpu into integer and divide it by 1000 Print UTC timestamp of server With Year-Month-Day Hour-Minute-Seconds
        timestamp = timedate.utcfromtimestamp(int(cpu[0]/1000)).strftime('%Y-%m-%d %H:%M:%S')

        message = str(timestamp) + "; CPU:" + str(cpu[1]) + "%;" + "io:" + str(io[1]) + "B/s; " + "IPv4: " + str(ipv4[1]) + "Bits/s; " + "IPv6: " + str(ipv6[1]) + "Bits/s"
        logging.critical(message)

        # display the cpu usage
        #print("CPU:", cpu[1], "%")
        # display the io usage as blocks/s
        #print("io:", io[1], "b/s")
        # display the network ipv4 usage
        #print("IPv4: ", ipv4[1], "Bits/s")
        # display the network ipv6 usage
        #print("IPv6: ", ipv6[1], "Bits/s")

        f.close


class Alarm():

    def send_email(subject, body):

        # Env Variables for the login into gmail mail server and recipient of the mails
        user = os.getenv('USER')
        pwd = os.getenv('PWD')
        recipient = os.getenv('RECIPIENT')

        # enter prepared variables into Constant so they cant change anymore
        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        # Try connection to gmail smtp server, login and send mail
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('Successfully sent the mail')
        # Throw error incase gmail smtp server refuses to send the mail or accept the password 
        except:
            print("Failed to send mail")


    def ScanCPULoad():
        f = open('data.json')
        data = json.load(f)

        #Maximum CPU Utilization in % 
        MaxCPULoad = 80

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        cpu = data["data"]["cpu"][last_entry]

        # display the cpu usage
        if int(cpu[1]) >= MaxCPULoad:

            # Text inside of the Mail
            subject = "Server Warning: CPU Load over threshold"
            body = "WARNING! CPU Load on server exceeded threshold! Current server load: " + str(cpu[1]) + "%"

            # function to send mail with prepared text
            Alarm.send_email(subject, body)

            #Alarm in Prompt
            print("ALARM JUNGE CPU IST BEI:", cpu[1], "%")

    def ScanIoUsage():
        f = open('data.json')
        data = json.load(f)

        # Maximum Blocks/s io usage
        MaxioLoad = 4

        #Variables for the Location in the Python Dir of data
        last_entry = int(286)
        io = data["data"]["io"]["io"][last_entry]

        # display the cpu usage
        if int(io[1]) >= MaxioLoad:

            # Text inside of the Mail
            subject = "Server Warning: CPU Load over threshold"
            body = "WARNING! IO Load on server exceeded threshold! Current server load: " + str(io[1]) + "Blocks/s"

            # function to send mail with prepared text
            Alarm.send_email(subject, body)

            #Alarm in Prompt
            print("ALARM JUNGE io IST BEI:", io[1], "Blocks/s")
        
