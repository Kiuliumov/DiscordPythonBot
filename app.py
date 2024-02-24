import discord
from discord.ext import commands
import random
import requests
from modules.games import Games
from modules.economy import Economy
from apikeys import login_key

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

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

@client.tree.command(name='roll', description='Rolls a random number between 1 and 100 and gives you this many cantina coins!')
@discord.app_commands.checks.cooldown(1,3600, key=lambda i: (i.guild_id, i.user.id))
async def diceroll(interaction: discord.Interaction):
    roll = random.randint(1, 100)
    id = interaction.user.name
    embed = discord.Embed(title='Roll!',
                          url='https://discord.gg/YRyN5ZY4',
                          description=f'{(str(id)).capitalize()} has rolled {roll}!',
                          color=0xFF5733)
    await interaction.response.send_message(embed=embed)
    await Economy.add_coins(interaction.user.id, roll)

@client.tree.error
async def on_test_error(interaction: discord.Interaction, error: commands.CommandError):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after, 2)
        hours = int(remaining_time // 3600)
        minutes = int((remaining_time % 3600) // 60)
        seconds = int(remaining_time % 60)
        await interaction.response.send_message(f"This command is on cooldown. Please try again in {hours} hours, {minutes} minutes, and {seconds} seconds.", ephemeral=True)

@client.tree.command(name='balance', description='Check your balance')
async def balance(interaction: discord.Interaction):
    await Economy.open_account(interaction.user.id)
    users = await Economy.get_bank_data()
    bank_amount = users[str(interaction.user.id)]['bank']

    embed = discord.Embed(
        title='Balance',
        description=f"{interaction.user.name.capitalize()}'s balance!",
        color=0xFF5733
    )
    embed.add_field(name='', value=f'{bank_amount} Cantina Coins')
    await interaction.response.send_message(embed=embed)

@client.tree.command(name='rps', description='Play rock,paper,scissors!')
@discord.app_commands.checks.cooldown(1,3600, key=lambda i: (i.guild_id, i.user.id))
async def rps(interaction: discord.Interaction,move: str):
    result, computer_choice = Games.rps(move)
    
    if move in ['rock','paper','scissors']:
        if move == 'paper':
         move = 'newspaper'
        if computer_choice == 'paper':
         computer_choice = 'newspaper'

        if result == 'win':
            await interaction.response.send_message(f'You Won! You chose :{move}: and the computer chose :{computer_choice}:\nYou got 100 Cantina Coins!')
            await Economy.add_coins(interaction.user.id,100)
        elif result == 'draw':
            await interaction.response.send_message(f'Its a draw! You chose :{move}: and the computer chose :{computer_choice}:')
        else:
           await interaction.response.send_message(f'You Lost! You chose :{move}: and the computer chose :{computer_choice}:\nYou lost 100 Cantina Coins!')
           await Economy.remove_coins(interaction.user.id,100)
    else:
        await interaction.response.send_message(f'Only valid moves are rock,paper,scissors!')
@client.tree.error
async def on_test_error(interaction: discord.Interaction, error: commands.CommandError):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after, 2)
        hours = int(remaining_time // 3600)
        minutes = int((remaining_time % 3600) // 60)
        seconds = int(remaining_time % 60)
        await interaction.response.send_message(f"This command is on cooldown. Please try again in {hours} hours, {minutes} minutes, and {seconds} seconds.", ephemeral=True)
client.run(login_key)
@client.tree.command(name='help',description='Shows all the commands the bot has!')
async def helpcommand(interaction: discord.Interaction):
    await interaction.response.send_message('All the bot commands: ping,info,dogpicture,balance,roll,rps'
