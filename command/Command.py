import asyncio
import inspect


class Command:
    def __init__(self,name,keys,function):
        self.name = name
        self.keys = keys
        self.function = function

    def execute(self):
        if callable(self.function):
            if inspect.iscoroutinefunction(self.function):
                asyncio.run(self.function())
            else:
                self.function()


