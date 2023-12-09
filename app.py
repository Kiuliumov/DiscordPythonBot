from apikeys import *
import random
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
    embed = discord.Embed(
        title='Info!',
        url='https://discord.gg/YRyN5ZY4',
        description='This is a chatbot that I am creating for fun, so please don\'t judge it too harshly!',
        color=0xFF5733
    )
    embed.set_author(name='Kiuliumov', url='https://discord.gg/YRyN5ZY4', icon_url='https://i.imgur.com/oPkwCHZ.jpg')
    embed.set_thumbnail(url='')
    embed.add_field(name='Instagram:', value='[dkiuliumov](https://www.instagram.com/dkiuliumov/)', inline=False)
    embed.add_field(name='Github:', value='[Kiuliumov](https://github.com/Kiuliumov)', inline=False)
    embed.add_field(name='YouTube:', value='[Kiuliumov](https://www.youtube.com/channel/UC84Nzj5Ruyc-ltYUU53pxHg)', inline=False)
    embed.add_field(name='Discord:', value='Kiuliumov', inline=False)
    await interaction.response.send_message(embed=embed)

@client.tree.command(name='dogpicture',description='Sends a random dog picture')
async def dogpicture(interaction:discord.Interaction):
   response_API = requests.get('https://dog.ceo/api/breeds/image/random')
   picture = response_API.json()
   picture = picture['message']
   await interaction.response.send_message(picture)


@client.tree.command(name='roll',description='Rolls a random number between 1 and 100!')
async def diceroll(interaction:discord.Interaction):
    roll = random.randint(1,100)
    id = interaction.user.name
    embed = discord.Embed(title ='Roll!',
    url ='https://discord.gg/YRyN5ZY4' ,
    description = f'{(str(id)).capitalize()} has rolled {roll}!',
    color = 0xFF5733)
    await interaction.response.send_message(embed=embed)

   
client.run(login_key)
