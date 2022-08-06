
from abc import ABC, abstractclassmethod, abstractmethod
import discord
from discord.message import Message
from discord.channel import TextChannel

class Module(ABC):
    async def handle_message(self, client: 'ModularClient', message: discord.Message):
        pass

    async def handle_command(self, client: 'ModularClient', message: discord.Message):
        pass


class ModularClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.modules: list[Module] = []
        self.command_char = '!'
        pass

    def add_module(self, module: Module):
        self.modules.append(module)

    # Handlers

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        print(f'>>> Message from {message.author}: {message.content}')
        if message.author.bot:
            print(f'Message from bot. Ignoring.')
            return

        if message.content[0] == self.command_char:
            print(f'Message is command. Running.')
            for m in self.modules:
                await m.handle_command(self, message)
        else:
            print(f'Normal message. Processing.')
            for m in self.modules:
                await m.handle_message(self, message)

    # Helper functions

    async def send_message(self, channel: TextChannel, msg):
        print(f'>>> Sending message "{msg}" to channel "{channel}"')
        await channel.send(msg)
