import asyncio
import inspect


class Command:
    def __init__(self, name, keys, function):
        self.name = name
        self.keys = keys
        self.function = function

    async def execute(self): # Changed to async
        if callable(self.function):
            if inspect.iscoroutinefunction(self.function):
                await self.function() # Use await instead of asyncio.run()
            else:
                self.function()