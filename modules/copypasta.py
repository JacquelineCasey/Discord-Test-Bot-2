
import discord
import json
import io

from client import Module, ModularClient


class CopyPasta(Module):
    def __init__(self, file_path):
        self.triggers_to_pastas = {}

        with io.open(file_path) as file:
            data: dict = json.load(file)
            for key in data.keys():
                for trigger in data[key]["triggers"]:
                    self.triggers_to_pastas[trigger] = data[key]["text"]

    @Module.message_handler
    async def recite_pasta(self, client: ModularClient, message: discord.Message):
        for trigger in self.triggers_to_pastas.keys():
            if trigger.lower() in message.content.lower():
                print(f"Found copypasta trigger {trigger}")
                await client.send_message(message.channel, self.triggers_to_pastas[trigger])
                break
