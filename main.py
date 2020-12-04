#Libarys
import socket
#From Project
from client.client import client
from server.server import server

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

def start(mode):
    if mode == 0:
        print("Server Start")
        s = server(str(local_ip))
    elif mode == 1:
        print("Client Start")
        c = client(str(local_ip))

if __name__ == "__main__":
    print("Programmstart")
    choice = -1
    while choice == -1:
        try:
            choice = int(input("Server : 0/ Client : 1 \n>"))
            if not(choice == 0 or choice == 1):
                raise Exception
        except Exception:
            print("Bitte geb eine Zahl ein")
            choice = -1
else:
    print("Starte für Consolendbugen")