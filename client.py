
from abc import ABC, abstractmethod
import asyncio
import discord
from discord.message import Message
from discord.channel import TextChannel


class Module(ABC):
    """Represent a module that handles various discord events."""
    async def handle_message(self, client: 'ModularClient', message: discord.Message):
        pass

    async def handle_command(self, client: 'ModularClient', message: discord.Message):
        pass

    async def handle_edit(self, client: 'ModularClient', before: discord.Message, after: discord.Message):
        pass


class Service(ABC):
    """Represents a non discord service that the bot can react to."""
    @abstractmethod
    async def run(client: 'ModularClient'):
        pass
        

class ModularClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.modules: list[Module] = []
        self.services: list[Service] = []
        self.command_char = '!'
        pass

    def add_module(self, module: Module):
        self.modules.append(module)

    def add_service(self, service: Service):
        self.services.append(service)

    # Handlers

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await asyncio.gather(*[s.run(self) for s in self.services])

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

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.content == after.content:
            return
        print(f'>>> Message edited by {after.author}: {after.content}')
        for m in self.modules:
            await m.handle_edit(self, before, after)

    # Helper functions

    async def send_message(self, channel: TextChannel, msg):
        print(f'>>> Sending message "{msg}" to channel "{channel}"')
        await channel.send(msg)
