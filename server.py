import socket
from datetime import datetime
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host = "localhost"
host_ip = "149.28.55.11"
host_port = 15420
print("IP :  ",host_ip)
print("Port : ",host_port)

sock.bind((host_ip,host_port))
print("[...] Waiting for transmission")
sock.listen(5)

while True:
    conn,addr = sock.accept()
    print("[...] Transmission received from:", addr)
    print("-------------------- [START OF TRANSMISSION] --------------------")

    bytedata = conn.recv(10240)
    data = bytedata.decode()

    print(data)
    print("--------------------  [END OF TRANSMISSION]  --------------------")
    try:
        with open(addr[0]+"/"+addr[0]+".txt", "r") as f:
            f.read()
    except IOError:
        os.mkdir(addr[0])
        with open(addr[0]+"/"+addr[0]+".txt", "w") as f:
            f.write("DIRECTORY CREATED - {0}".format(datetime.now().strftime("%m/%d/%Y-%H:%M:%S")))
    finally:
        with open(addr[0]+"/"+"{0}.txt".format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S")), "w") as f:
            f.write(data)
    conn.close()
    print("[...] Closed connection from:", addr)