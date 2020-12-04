#Libarys
import socket
#From Project
from configs import C_KEY_FILE, SERVER_IP, SERVER_PORT
from protocol.command import cmd as cmds
from protocol.worker import network

class client():

    def __init__(self, ip = "127.0.0.1"):
        assert isinstance(ip, str), f"IP muss ein str sein gegeben {type(ip)}"
        self.uname = ""
        self.id = -1
        self.ip = ip
        self.connected = False
        self._set_data()
        print(self.uname)
        print(self.id)

    def _server_request(self, targetid, cmd, args):
        command = cmds(self.ip, self.id, targetid, cmd, args)
        senddata = network().send(command)

        return command

    def _new_device(self):
        print("Neuer Client")
        print("Dein Username : ")
        self.uname = input("> ")
        self._connection()
        answer = self._server_request(0, "register", [self.uname, self.ip])
        #self.id = answer.get_args()[0]
        self.id = 1
        with open(C_KEY_FILE, "a") as file:
            file.write(self.uname + "\n")
            file.write(str(self.id))

    def _connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SERVER_IP, SERVER_PORT))
        if(self.id == -1):
            print("NO ID SET")
        else:
            print("ID IS SET")

    def _set_data(self):
        try:
            with open(C_KEY_FILE, "r") as file:
                datas = file.read().split("\n")
                self.uname = datas[0]
                self.id = int(datas[1])
                self._connection()
        except FileNotFoundError:
            self._new_device()

