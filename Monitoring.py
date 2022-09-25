from datetime import datetime as timedate
from time import time
from linode_api4 import *
import re
import json

# Needed Vars to call the api
token = ""
client = LinodeClient(token)

#get instance ids
Linode_Array = client.linode.instances()


# function to itterate through the Linode_Array list
for x in Linode_Array:
    #turn the list into a string and remove everything after the first ": "
    Linode_ID = str(x).split(": ")[1]

    #call the instance class with the ID and token
    my_instance = Instance(client, Linode_ID)

    #Get current stats from instance
    Current_load = my_instance.stats

    #Converting the serialized JSON into a str
    json_string = json.dumps(Current_load)
    
    #creating a Json datafile
    my_file = open("data.json","w+")
    my_file.write(json_string)
    
    f = open('data.json')      
    data = json.load(f)

    #go through the data dictionary to extract the right information
    print("io")
    for io in data["data"]["io"]["io"]:

        ts = int(io[0]/1000)
        print(timedate.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        print(io[1],"%")

    print("CPU")
    for cpu in data["data"]["cpu"]:
        print(cpu, "%")

    print("IPv4")
    for ipv4 in data["data"]["netv4"]["in"]:
        print(ipv4)
    
    print("IPv6")
    for ipv6 in data["data"]["netv6"]["in"]:
        print(ipv6)

    f.close