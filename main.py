from data_class import *

while True:
    # function to update the log file and print current stats to the prompt
    monitor.updateLog()

    # function to scan for CPU Load over the MaxCPULoad Value given
    Alarm.ScanCPULoad()

    # function to scan for IO load over the MaxioLoad value given
    Alarm.ScanIoUsage()
    print("Run Done")
    time.sleep(10)