import socket
import datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host = "localhost"
host_ip = "149.28.63.177"
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

    bytedata = conn.recv(1024)
    data = bytedata.decode()

    print(data)
    print("--------------------  [END OF TRANSMISSION]  --------------------")
    with open("{}.txt".format(datetime.datetime.now()), "w") as myfile:
        myfile.write(data)
    conn.close()
    print("[...] Closed connection from:", addr)
