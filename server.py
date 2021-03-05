import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host = "localhost"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
host_port = 15420
print("Hostname :  ",host_name)
print("IP : ",host_ip)

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
    conn.close()
    print("[...] Closed connection from:", addr)