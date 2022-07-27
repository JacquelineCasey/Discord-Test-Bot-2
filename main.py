
import discord
from discord.message import Message
from discord.channel import TextChannel
from dotenv import load_dotenv
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            print(f'Message from self. Ignoring.')
            return
            
        await self.process_message(message)

    async def process_message(self, msg: Message):
        if msg.content[0] == '!':
            await self.send_message(msg.channel, 'I saw that!')

    async def send_message(self, channel: TextChannel, msg):
        print(f'Sending message "{msg}" to channel "{channel}"')
        await channel.send(msg)


load_dotenv() # Does nothing if it can't find .env
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

print('Preparing to Connect to Discord')
client = MyClient()
client.run(DISCORD_BOT_TOKEN)
