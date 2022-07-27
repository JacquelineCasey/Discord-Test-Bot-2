
import discord

from client import Module, ModularClient


class Mock(Module):
    def activate(self, client: ModularClient):
        client.add_message_handler(self.handle_message)

    async def handle_message(self, client: ModularClient, message: discord.Message):
        pass # STUB

    

last_msg_dict = {}