from multiprocessing.dummy import current_process
from threading import current_thread
from linode_api4 import *
toekn = "014415c4e2a9f7049f4b7558f13b8cc6e6f5bc686ad88eb0c3fc10b1cff787f8"
client = LinodeClient(toekn)

Linode_ID = 35495125
my_instance = Instance(client, Linode_ID)

##for i in Current_load:
Current_load = my_instance.stats
print(Current_load)
