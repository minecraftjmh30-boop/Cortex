
class Command:
    def __init__(self,name,keys,function):
        self.name = name
        self.keys = keys
        self.function = function

    def execute(self):
        if callable(self.function):
            self.function()
        else:
            print(f"No function assigned to command: {self.name}")



