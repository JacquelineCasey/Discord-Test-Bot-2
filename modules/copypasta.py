
import discord
import io
import json

from client import Module, ModularClient


class CopyPasta(Module):
    def __init__(self, file_path):
        self.triggers_to_pastas: dict[str, str] = {}
        with io.open(file_path) as file:
            data: dict = json.load(file)
            
        for key in data.keys():
            for trigger in data[key]["triggers"]:
                self.triggers_to_pastas[trigger] = data[key]["text"]

    async def handle_message(self, client: ModularClient, message: discord.Message):
        "Scans messages for keywords and recites appropriate copypasta."
        for trigger in self.triggers_to_pastas.keys():
            if trigger.lower() in message.content.lower():
                print(f"Found copypasta trigger {trigger}")
                await client.send_message(message.channel, self.triggers_to_pastas[trigger])
                break
