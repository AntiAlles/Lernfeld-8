from linode_api4 import *
import re

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
    print(Current_load)
