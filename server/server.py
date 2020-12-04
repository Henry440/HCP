#Libarys
import socket
#From Project
from configs import S_KEY_FILE, SERVER_PORT, SERVER_IP
from protocol.command import cmd as cmds
from protocol.worker import network

class server():

    def __init__(self, ip = "127.0.0.1"):
        assert isinstance(ip, str), f"IP muss ein str sein gegeben {type(ip)}"
        self.id = 0
        self.ip = ip

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, SERVER_PORT))

