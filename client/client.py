#Libarys

#From Project
from configs import C_KEY_FILE
from protocol.command import cmd
from protocol.worker import network

class client():

    def __init__(self, ip):
        self.uname = ""
        self.id = -1
        self.ip = ip
        self.connected = False
        self._set_data()
        print(self.uname)
        print(self.id)

    def _server_request(self, targetid, cmd, args):
        command = cmd(self.ip, self.id, targetid, cmd, args)
        senddata = network().send(command)

        return command

    def _new_device(self):
        print("Neuer Client")
        print("Dein Username : ")
        self.uname = input("> ")
        print("Deine ID : ") #TODO SPäter von Server
        answer = self._server_request(0, "register", (self.uname, self.ip))
        self.id = answer.get_args()[0]
        with open(C_KEY_FILE, "a") as file:
            file.write(self.uname + "\n")
            file.write(str(self.id))

    def _set_data(self):
        try:
            with open(C_KEY_FILE, "r") as file:
                datas = file.read().split("\n")
                self.uname = datas[0]
                self.id = int(datas[1])
        except FileNotFoundError:
            self._new_device()

