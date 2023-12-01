from apikeys import *
import discord
from discord import app_commands
from discord.ext import commands
import requests
#-------------------------------------------------------------------------------
intents = discord.Intents.default()
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    print(client.user)
    print(client.user.id)
    print('------------------------------')
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@client.tree.command(name='ping', description='This is a ping command!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! The client latency is {round(client.latency * 1000)}ms.')


@client.tree.command(name='info', description='This is an info command!')
async def info(interaction: discord.Interaction):
    embed = discord.Embed(title ='Info!',
    url ='https://discord.gg/YRyN5ZY4' ,
    description = 'Under construction',
    color = 0xFF5733)
    embed.set_author(name = 'Kiuliumov',url='https://discord.gg/YRyN5ZY4',icon_url='https://i.imgur.com/oPkwCHZ.jpg')
    embed.set_image(url = 'https://images-ext-2.discordapp.net/external/sSU94Q41MQgIIX0XiXXyDOcGeiY6__xq2eS_zQ33v34/%3Fcid%3D73b8f7b12ba3c3497960d92cf377ac6ee4d8a3e4046135c6%26rid%3Dgiphy.mp4%26ct%3Dg/https/media2.giphy.com/media/Nx0rz3jtxtEre/giphy.mp4')
    await interaction.response.send_message(embed=embed)





@client.tree.command(name='joinedwhen',description='Checks when a user joined the server!')
@app_commands.describe(member='The member you want to get the joined date from')
async def joined(interaction: discord.Interaction, member: discord.Member):
    """Says when a member joined."""
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@client.tree.command(name='dogpicture',description='Sends a random dog picture')
async def catpicture(interaction:discord.Interaction):
   response_API = requests.get('https://dog.ceo/api/breeds/image/random')
   picture = response_API.json()
   picture = picture['message']
   await interaction.response.send_message(picture)

   


client.run(login_key)
