from data_class import *

# function to get the IDs of the Linode Instances 
monitor.getInstanceID()

# function to update the log file and print current stats to the prompt
monitor.updateLog()

# function to scan for CPU Load over the MaxLoad Value given
Alarm.ScanCPULoad()