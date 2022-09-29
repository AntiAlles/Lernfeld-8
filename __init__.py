from monitor import Monitor, Display
from alarm import Alarm
import time
from threading import Thread

class __init__:

    # function the main process of logging the data into the status.log and scan for unusual high loads
    def main():

        cpu_max_soft = int(input("Max CPU Load(0 - 100):\n"))
        io_max_soft = int(input("Max io Load(0 - 6):\n"))
        
        
        secondary_thread = Thread(target=__init__.secondary())
        secondary_thread.join()

        while True:    
            # function to get the IDs of the Linode Instances 
            data = Monitor.get_instance_stats()

            # function to update the log file and print current stats to the prompt
            Monitor.update_log(data)

            # function to scan for CPU Load over the max_CPU_load Value given
            Alarm.is_CPU_over_threshold(data, 80, cpu_max_soft)

            # function to scan for IO load over the max_IO_usage value given
            Alarm.is_IO_over_threshold(data, 4, io_max_soft)

            # Wait for 10 seconds
            time.sleep(10)

    # function for the secondary process for the user to display individual loads
    def secondary():
            print("Please enter what you want to Display:")

            while True:
                #get stats dir from instance 
                data = Monitor.get_instance_stats()
                #wait for input in the prompt and convert all lowercase Chars
                prompt_input = str.lower(input())

                if prompt_input == "-h" or prompt_input == "":
                    print("You can display performance stats by typing one of the 4 into the prompt:\n [cpu]    [io]    [ipv4]    [ipv6]")  

                elif prompt_input == "cpu":
                    Display.display_cpu(data)

                elif prompt_input == "io":
                    Display.display_io(data)

                elif prompt_input == "ipv4":
                    Display.display_ipv4(data)

                elif prompt_input == "ipv6":
                    Display.display_ipv6(data)