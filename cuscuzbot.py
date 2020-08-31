### Bot created using the tutorial:
### https://realpython.com/how-to-make-a-discord-bot-python

import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} conectou-se ao Discord no servidor '
        f'"{guild.name}" (id: {guild.id})'
    )

    ### TODO: Averiguar a sintaxe dentro do join()
    usuarios = '\n - '.join([member.name for member in guild.members])

    print(f'Membros do Servidor:\n {usuarios}')

client.run(TOKEN)