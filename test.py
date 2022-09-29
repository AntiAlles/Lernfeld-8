from monitor import *

while True:
    data = Monitor.get_instance_stats()
    
    Monitor.display_cpu