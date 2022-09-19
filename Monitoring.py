from multiprocessing.dummy import current_process
from threading import current_thread
from linode_api4 import LinodeClient
toekn = ""
client = LinodeClient(toekn)

Linode_ID = 35495125
Current_load = client.account.invoices()

for i in Current_load:
##    network = client.get(any)
    print(i)
