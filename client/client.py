#Libarys

#From Project
from configs import C_KEY_FILE

def init():
    try:
        file = open(C_KEY_FILE, "r")
        data = file.read()
    except FileNotFoundError as e:
        print("ERSTELLE DIE DATEI")
        print("Dein Username : ")
        uname = input("> ")
        print("Deine ID : ") #TODO SPäter von Server
        id = input("> ")
        file = open(C_KEY_FILE, "a")
        file.write(uname + "\n")
        file.write(id + "\n")