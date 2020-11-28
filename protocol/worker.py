#Libarys
import pickle

class network():

    def __init__(self):
        self.init = False #Send or recice have to used to unlock th object
        self.type = 0     #Type 0 is Lock, 1 is send, 2 is recive

    def send(self, data):
        self.init = True
        self.type = 1
        return pickle.dumps(data)

    def recive(self, data):
        self.init = True
        self.type = 2
        return pickle.loads(data)