from ast import arg
from __init__ import __init__ as Init
from dotenv import load_dotenv
from threading import Thread

#loads the environmental variables from the .env file
load_dotenv()

#declares the Softlimits for the use case 
cpu_max_soft = int(input("Max CPU Load(0 - 100):\n"))
io_max_soft = int(input("Max io Load(0 - 6):\n"))

#declares variable names for the new threads
main_thread = Thread(target=Init.main, args=(cpu_max_soft, io_max_soft))
secondary_thread = Thread(target=Init.secondary)

#starts the previously declared threads
main_thread.start()
secondary_thread.start()