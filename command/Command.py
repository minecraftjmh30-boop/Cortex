class Command:
    def __init__(self,key,ip):
        self.key = key
        self.ip = ip



lights = Command("lights", ("255.255", "111.111"))
