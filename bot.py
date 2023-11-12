'''
This is the main file for the Discord bot. It handles the setup of the bot, as well as the command handling.
'''
import discord
from discord.ext import commands
import requests
import json

giphy_api_key = 'INSERT YOUR GIPHY API KEY HERE'
discord_bot_token = 'INSERT YOUR DISCORD BOT TOKEN HERE'
if not giphy_api_key or not discord_bot_token:
    raise ValueError("GIPHY_API_KEY and DISCORD_BOT_TOKEN must be set in environment variables")

intents = discord.Intents(messages=True, message_content=True)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def meme(ctx, *, search_term):
    '''
    This function is triggered when the user types "!meme" followed by a search term.
    It uses the Giphy API to search for a meme related to the search term and sends it to the Discord channel.
    '''
    url = f'http://api.giphy.com/v1/gifs/search?q={search_term}&api_key={giphy_api_key}&limit=1'
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        meme_url = data['data'][0]['images']['original']['url']
        await ctx.send(meme_url)
    except Exception as e:
        await ctx.send(f"Sorry, I couldn't fetch a meme due to the following error: {str(e)}")
        
bot.run(discord_bot_token)