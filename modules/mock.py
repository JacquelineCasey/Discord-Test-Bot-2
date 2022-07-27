
import discord

from client import Module, ModularClient


class Mock(Module):
    def __init__(self):
        self._last_msg_in_channels = {}

    def activate(self, client: ModularClient):
        client.add_message_handler(self.handle_message)
        client.add_command_handler(self.handle_command)

    async def handle_message(self, client: ModularClient, message: discord.Message):
        self._last_msg_in_channels[message.channel] = message.content

    async def handle_command(self, client: ModularClient, message: discord.Message):
        if (message.content.replace(" ", "") == '!mock'):
            print("Mock command triggered!")
            if message.channel in self._last_msg_in_channels.keys():
                await client.send_message(
                    message.channel, 
                    Mock.mock_string(self._last_msg_in_channels[message.channel])
                )
            else:
                print("Could not find message to mock.")


    def mock_string(s: str):
        output = ''
        upper = False
        for c in s.lower():
            if upper:
                output += c.upper()
            else:
                output += c
            upper = not upper
        return output
