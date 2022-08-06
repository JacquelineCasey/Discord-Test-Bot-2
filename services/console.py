
from email.policy import default
import aioconsole
import discord
from typing import Dict

from client import Service, ModularClient


class Console(Service):
    async def run(self, client: ModularClient):
        self.guild: discord.Guild = None
        self.channel = None

        self.guild_id_dict: Dict[str, discord.Guild] = {}
        async for g in client.fetch_guilds(limit = None):
            self.guild_id_dict[g.name] = g.id

        while True:
            msg = await aioconsole.ainput()
            print(f'---- running: "{msg}" ----')
            await self.process_command(msg, client)
            print(f'---- done ----')

    async def process_command(self, command: str, client: ModularClient):
        words = command.strip().split(' ')
        match words:
            case ['set', 'guild' | 'g' | 'server' | 's', * name]:
                name = ' '.join(name)
                if name in self.guild_id_dict.keys():
                    self.guild = client.get_guild(self.guild_id_dict[name])
                    self.channel = None
                    print(f'Set guild to "{name}"')
                else:
                    print(f'Failed to find guild "{name}"')

            case ['set', 'channel' | 'ch' | 'c', * name]:
                name = ' '.join(name)
                for ch in self.guild.text_channels:
                    if ch.name == name:
                        self.channel = ch
                        print(f'Set channel to "{name}"')
                        return
                print(f'Failed to find channel "{name}"')

            case ['list', 'guild' | 'guilds' | 'g' | 'servers' | 'server' | 's']:
                print("Listing guild names:")
                for name in sorted(self.guild_id_dict.keys()):
                    print(f'- {name}')

            case ['list', 'channels' | 'channel' | 'ch' | 'c']:
                if self.guild is not None:
                    print("Listing channels in guild:")
                    for ch in self.guild.text_channels:
                        print(f'- {ch.name}')
                else:
                    print('Guild not set.')

            case ['message' | 'msg', * message]:
                message = ' '.join(message)
                if self.channel is not None:
                    await client.send_message(self.channel, message)
                else:
                    print("Channel not set.")

            case _:
                print('Unrecognized Command.')

