from linode_api4 import LinodeClient
toekn = "a2a41dae2f7f9a10997b1b21b378d643c6cda81675f8dd6539960c2754b80cba"
client = LinodeClient(toekn)

my_linodes = client.linode.instances()

for current_linode in my_linodes:
    print(current_linode)