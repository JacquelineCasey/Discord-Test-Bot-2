
import discord

from client import Module, ModularClient

# The command ! causes the bot to be summoned, printing a simple message
class Summon(Module):
    @Module.command_handler
    async def greet(self, client: ModularClient, message: discord.Message):
        if message.content.strip() == '!':
            await client.send_message(message.channel, "Hello there!")

