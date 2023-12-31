import discord
import responses
import os

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot(): 
    TOKEN = os.environ['DISCORD_TOKEN']
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = message.author.name
        user_message = str(message.content)
        channel = str(message.channel.name)

        if user_message[0] == '%':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '$':
            await send_message(message, user_message, is_private=True)
    
    client.run(TOKEN)