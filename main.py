#Libarys
import socket
#From Project
from client.client import client
from server.server import server
from helper import inp

def start(mode):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Verwendete IP ist " + local_ip)
    value = inp("IP ändern [Y/n]", ["Y", "y", "N", "n"]).lower()
    if(value == "y"):
        local_ip = input("Neue IP : ")
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
    start(choice)
else:
    print("Starte für Consolendbugen")