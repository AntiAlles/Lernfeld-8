import smtplib
import os

class Alarm():

    def send_email(subject, body):
        if os.getenv('IS_TEST_ENV') == 'true': 
            return
        # Env Variables for the login into gmail mail server and recipient of the mails
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        recipient = os.getenv('RECIPIENT')

        # enter prepared variables into Constant so they cant change anymore
        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        # Try connection to gmail smtp server, login and send mail
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, password)
            server.sendmail(FROM, TO, message)
            server.close()
            print('Successfully sent the mail')
        # Throw error incase gmail smtp server refuses to send the mail or accept the password 
        except:
            print("Failed to send mail")


    def is_CPU_over_threshold(data, max_CPU_load):

        #Variables for the Location in the Python Dir of data
        cpu = data["data"]["cpu"][-1]

        # display the cpu usage
        if int(cpu[1]) >= max_CPU_load:

            # Text inside of the Mail
            subject = "Server Warning: CPU Load over threshold"
            body = "WARNING! CPU Load on server exceeded threshold! Current server load: " + str(cpu[1]) + "%"

            # function to send mail with prepared text
            Alarm.send_email(subject, body)

            #Alarm in Prompt
            print("ALARM JUNGE CPU IST BEI:", cpu[1], "%")
            return True
        return False    

    def is_IO_over_threshold(data, max_IO_load):

        #Variables for the Location in the Python Dir of data
        io = data["data"]["io"]["io"][-1]

        # display the io usage
        if int(io[1]) >= max_IO_load:

            # Text inside of the Mail
            subject = "Server Warning: IO Load over threshold"
            body = "WARNING! IO Load on server exceeded threshold! Current server load: " + str(io[1]) + "Blocks/s"

            # function to send mail with prepared text
            Alarm.send_email(subject, body)

            #Alarm in Prompt
            print("ALARM JUNGE io IST BEI:", io[1], "Blocks/s")
            return True
        return False  
