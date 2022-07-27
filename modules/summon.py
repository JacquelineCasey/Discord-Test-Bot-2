
import discord

from client import Module, ModularClient

# The command ! causes the bot to be summoned, printing a simple message
class Summon(Module):
    def activate(self, client: ModularClient):
        client.add_command_handler(self.handle_command)

    async def handle_command(self, client: ModularClient, message: discord.Message):
        if message.content.strip() == '!':
            await client.send_message(message.channel, "Hello there!")

