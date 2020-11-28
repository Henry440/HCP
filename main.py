#Libarys
import socket
#From Project
from client.client import client

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
c = client(str(local_ip))