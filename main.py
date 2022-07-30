
from ast import Mod
import discord

from dotenv import load_dotenv
import os

from client import ModularClient
from modules.mock import Mock
from modules.summon import Summon
from modules.copypasta import CopyPasta


def main():
    load_dotenv() # Does nothing if it can't find .env
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

    client = ModularClient()
    client.add_module(Mock())
    client.add_module(Summon())
    client.add_module(CopyPasta("resources/copypasta.json"))

    print('Attempting to Connect to Discord')
    client.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
