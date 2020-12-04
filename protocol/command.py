from configs import WHITELIST_CMD

#ID Types
#-1 Undefined/Unset
#0 Brodcast
#ID > 0 Devices

class cmd:

    def __init__(self, senderip, senderid, targetid, cmd, args): 
        #Check for correct types
        assert isinstance(senderip, str), "Sender IP muss ein String sein"
        assert isinstance(senderid, int), "Sender ID muss ein Integer sein"
        assert isinstance(targetid, int), "Target ID muss ein Integer sein"
        assert isinstance(cmd, str),"Der Command muss ein String sein"
        assert isinstance(args, list), "Die Argumente müssen ein Tuple sein"
        #Routing Checks
        assert len(senderip.split(".")) == 4, "Fehler in der Senderip erkannt"
        assert senderid > 0 or (senderid == -1 and cmd in WHITELIST_CMD), "Senderid ist Ungültig"
        assert targetid >= 0, "Targetid ungültig"
        #Content Check
        assert len(cmd.split(" ")) != 0, "Der Command darf kein Leerzeichen Enthalten"
        
        for i in range(len(args)):
            args[i] = str(args[i])

        self.senderip = senderip
        self.senderid = senderid
        self.targetid = targetid
        self.cmd = cmd
        self.args = args

    def get_args(self):
        return self.args