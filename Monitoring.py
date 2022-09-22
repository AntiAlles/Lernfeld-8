from multiprocessing.dummy import current_process
from threading import current_thread
from time import time
from tkinter.tix import DirTree
from linode_api4 import *
import re
import json

# Needed Vars to call the api
token = "014415c4e2a9f7049f4b7558f13b8cc6e6f5bc686ad88eb0c3fc10b1cff787f8"
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
    