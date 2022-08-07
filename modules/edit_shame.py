
import asyncio
import discord


from client import Module, ModularClient

class EditShame(Module):
    async def handle_edit(self, client: ModularClient, before: discord.Message, after: discord.Message):
        WAIT_TIME = .5
        LONG_WAIT_TIME = 2
        print('Edit shaming!')

        for emoji in ['🇪', '🇩', '🇮', '🇹']:
            await after.add_reaction(emoji)
            await asyncio.sleep(WAIT_TIME)

        await asyncio.sleep(LONG_WAIT_TIME)

        for emoji in ['🇪', '🇩', '🇮', '🇹']:
            await after.remove_reaction(emoji, client.user)
            await asyncio.sleep(WAIT_TIME)

        await asyncio.sleep(LONG_WAIT_TIME)

        for emoji in ['🇸', '🇭', '🇦', '🇲', '🇪']:
            await after.add_reaction(emoji)
            await asyncio.sleep(WAIT_TIME)

        await asyncio.sleep(LONG_WAIT_TIME)

        for emoji in ['🇸', '🇭', '🇦', '🇲', '🇪']:
            await after.remove_reaction(emoji, client.user)
            await asyncio.sleep(WAIT_TIME)
