
import discord

from client import Module, ModularClient


# The command ! causes the bot to be summoned, printing a simple message
class Summon(Module):
    async def handle_command(self, client: ModularClient, message: discord.Message):
        '''Greets the user. Triggered by "!".'''
        if message.content.strip() == '!':
            await client.send_message(message.channel, "Hello there!")
