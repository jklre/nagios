import socket
import time
import os

def AlwaysTrue(data):
    #print("I am in Always True")
    print(data)
    #response = raw_input("Reply: ")
    if data == "exit":
        s.sendall(response1)
    time.sleep(1)
    sendReply(data)

def sendReply(data):
    if data == "No Fuck You":
        s.sendall("Fuck You")
        print(data)
        time.sleep(1)
        AlwaysTrue(data)
    else:
        AlwaysTrue(data)

def newResponse():
    data = s.recv(1024)
    AlwaysTrue(data)

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected to " + (host) + " on port " + str(port))
initialMessage = "Fuck You"
s.sendall(initialMessage)

data = s.recv(1024)
AlwaysTrue(data)
#formatData(data)
s.close()