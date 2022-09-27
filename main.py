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

    # function to scan for CPU Load over the max_CPU_load Value given
    Alarm.is_CPU_over_threshold(data, 80)

    # function to scan for IO load over the max_IO_usage value given
    Alarm.is_IO_over_threshold(data, 4)
    print("Run Done")
    time.sleep(300)