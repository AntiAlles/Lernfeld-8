from data_class import *

load_dotenv()

# Needed Vars to call the api
client = LinodeClient(os.getenv('TOKEN'))

#get instance ids
Linode_Instances = client.linode.instances()


# function to itterate through the Linode_Array list
for Linode_Instance in Linode_Instances:
    #turn the list into a string and remove everything after the first ": "
    Linode_ID = str(Linode_Instance).split(": ")[1]

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

    last_entry = int(286)
    cpu = data["data"]["cpu"][last_entry] 
    io = data["data"]["io"]["io"][last_entry]
    ipv4 = data["data"]["netv4"]["in"][last_entry]
    ipv6 = data["data"]["netv6"]["in"][last_entry]

    #Convert first array item of Cpu into integer and divide it by 1000
    timestamp = int(cpu[0]/1000)
    #Print UTC timestamp of server With Year-Month-Day Hour-Minute-Seconds 
    print(timedate.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

    #display the cpu usage with timestamp
    print("CPU:", cpu[1],"%")

    #display the io usage as blocks/s with timestamp
    print("io:", io[1],"b/s")

    #display the network ipv4 usage with timestamp
    print("IPv4: ", ipv4[1],"Bits/s")    

    #display the network ipv6 usage with timestamp
    print("IPv6: ", ipv6[1],"Bits/s")
    
    f.close