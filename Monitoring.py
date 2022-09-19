from multiprocessing.dummy import current_process
from threading import current_thread
from linode_api4 import LinodeClient
toekn = "014415c4e2a9f7049f4b7558f13b8cc6e6f5bc686ad88eb0c3fc10b1cff787f8"
client = LinodeClient(toekn)

Linode_ID = client.networking.ips()
    ##my_linodes = client.load(Linode_ID)

for i in Linode_ID:
    ##network = client.load(i)
    print(i)
