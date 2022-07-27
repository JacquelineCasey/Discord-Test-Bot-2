
from abc import ABC, abstractmethod
import discord
from discord.message import Message
from discord.channel import TextChannel


class Module(ABC):
    @abstractmethod
    def activate(self, client):
        '''Given a client, attaches all necessary hooks.'''
        pass


class ModularClient(discord.Client):
    def __init__(self):
        super().__init__()
        self._message_handlers = []
        self._command_handlers = []
        self.modules = []
        self.command_char = '!'
        pass

    def add_module(self, module: Module):
        self.modules.append(module)
        module.activate(self)

    # Module Setup Functions

    def add_message_handler(self, func):
        '''Registers a handler to run on all non command, non bot messages.
        
        A message handler is an async function that takes this client and a message. 
        '''

        self._message_handlers.append(func)

    def add_command_handler(self, func):
        '''Registers a handler to run on all command, non bot messages.
        
        A command handler is an async function that takes this client and a message. 
        '''
        self._command_handlers.append(func)

    # Handlers

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.bot:
            print(f'Message from bot. Ignoring.')
            return

        if message.content[0] == self.command_char:
            print(f'Message is command. Running.')
            for handler in self._command_handlers:
                await handler(self, message)
        else:
            print(f'Normal message. Processing.')
            for handler in self._message_handlers:
                await handler(self, message)

    # Helper functions

    async def send_message(self, channel: TextChannel, msg):
        print(f'Sending message "{msg}" to channel "{channel}"')
        await channel.send(msg)
