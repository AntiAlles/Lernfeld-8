from __init__ import __init__ as Init
from dotenv import load_dotenv
from threading import Thread

#loads the environmental variables from the .env file 
load_dotenv()

#declares variable names for the new threads
main_thread = Thread(target=Init.main)
secondary_thread = Thread(target=Init.secondary)

#starts the previously declared threads
main_thread.start()
secondary_thread.start()