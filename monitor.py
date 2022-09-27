from datetime import datetime as timedate
from linode_api4 import *
import logging
import os


class Monitor():

    def get_instance_stats():
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
            return my_instance.stats
             

    def update_log(data):

        #Variables for the Location in the Python Dir of data
        cpu = data["data"]["cpu"][-1]
        io = data["data"]["io"]["io"][-1]
        ipv4 = data["data"]["netv4"]["in"][-1]
        ipv6 = data["data"]["netv6"]["in"][-1]

        #Configure the logging method
        logging.basicConfig(filename="status.log", level=logging.INFO, format='%(message)s', force=True)
        
        # Convert first array item of Cpu into integer and divide it by 1000 Print UTC timestamp of server With Year-Month-Day Hour-Minute-Seconds
        timestamp = timedate.utcfromtimestamp(int(cpu[0]/1000)).strftime('%Y-%m-%d %H:%M:%S')

        message = str(timestamp) + "; CPU:" + str(cpu[1]) + "%; " + "io:" + str(io[1]) + "B/s; " + "IPv4: " + str(ipv4[1]) + "Bits/s; " + "IPv6: " + str(ipv6[1]) + "Bits/s"
        logging.critical(message)