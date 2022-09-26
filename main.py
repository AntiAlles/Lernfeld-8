from monitor import Monitor
from alarm import Alarm
from dotenv import load_dotenv
import time

load_dotenv()

while True:    
    # function to get the IDs of the Linode Instances 
    data = Monitor.get_instance_stats()

    # function to update the log file and print current stats to the prompt
    Monitor.update_log(data)

    # function to scan for CPU Load over the MaxCPULoad Value given
    Alarm.scan_CPU_load(data)

    # function to scan for IO load over the MaxioLoad value given
    Alarm.scan_IO_usage(data)
    print("Run Done")
    time.sleep(10)