import discord
from discord.ext import commands
import json
import os
from apikeys import login_key
import random
import requests
intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

# Change this to your own path
os.chdir("C:\\Users\\mitib\\OneDrive\\Documents\\GitHub\\DiscordPythonBot\\")

async def open_account(user_id):
    with open('bank.json', 'r') as f:
        users = json.load(f)

    if str(user_id) in users:
        return False
    else:
        users[str(user_id)] = {'bank': 500}

    with open('bank.json', 'w') as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open('bank.json', 'r') as f:
        users = json.load(f)
    return users

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

@client.tree.command(name='dogpicture', description='Sends a random dog picture')
async def dogpicture(interaction: discord.Interaction):
    response_API = requests.get('https://dog.ceo/api/breeds/image/random')
    picture = response_API.json()
    picture = picture['message']
    await interaction.response.send_message(picture)

@client.tree.command(name='roll', description='Rolls a random number between 1 and 100!')
async def diceroll(interaction: discord.Interaction):
    roll = random.randint(1, 100)
    id = interaction.user.name
    embed = discord.Embed(title='Roll!',
                          url='https://discord.gg/YRyN5ZY4',
                          description=f'{(str(id)).capitalize()} has rolled {roll}!',
                          color=0xFF5733)
    await interaction.response.send_message(embed=embed)

@client.tree.command(name='balance', description='Check your balance')
async def balance(interaction: discord.Interaction):
    await open_account(interaction.user.id)
    users = await get_bank_data()
    bank_amount = users[str(interaction.user.id)]['bank']

    embed = discord.Embed(
        title='Balance',
        description=f"{interaction.user.name.capitalize()}'s balance!",
        color=0xFF5733
    )
    embed.add_field(name='',value=bank_amount)

    await interaction.response.send_message(embed=embed)
@client.tree.command(name='leaderboard',description='Shows who are the richest people on the server!')
async def leaderboard(interaction:discord.Interaction):
    with open('bank.json', 'r') as file:
     data = json.load(file)
     account_list = [{"id": acc_id, "balance": acc_data["bank"]} for acc_id, acc_data in data.items()]
     sorted_accounts = sorted(account_list, key=lambda x: x['balance'], reverse=True)
     for i in range(1,3):
           account = sorted_accounts[i]
           await interaction.response.send_message(f"{i+1}. Account ID: {account['id']} - Balance: ${account['balance']}")
    
client.run(login_key)
