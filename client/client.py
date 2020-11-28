#Libarys

#From Project
from configs import C_KEY_FILE

class client():

    def __init__(self):
        self.uname = ""
        self.id = -1
        self.connected = False
        self._set_data()
        print(self.uname)
        print(self.id)

    def go_online(self):
        pass

    def _new_device(self):
        print("Neuer Client")
        print("Dein Username : ")
        self.uname = input("> ")
        print("Deine ID : ") #TODO SPäter von Server
        self.id = int(input("> "))
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

