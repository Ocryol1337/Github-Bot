import discord
import requests
import json
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')

@client.command()
async def instagram(ctx, *, name: str = 'officialrickastley') -> None:
    r       = requests.get(f"https://api.popcat.xyz/instagram?user={name}")
    nameinfo     = r.json()
    em      = discord.Embed(color=000000)
    fields  = [ 
        {'name': 'Username:',          'value': nameinfo['username']},
        {'name': 'Full Name:',     'value': nameinfo['full_name']},
        {'name': 'Biography:',     'value': nameinfo['biography']},
        {'name': 'Posts:',        'value': nameinfo['posts']},
        {'name': 'Reels:',   'value': nameinfo['reels']},
        {'name': 'Followers:',     'value': nameinfo['followers']},
        {'name': 'Following:',         'value': nameinfo['following']},
        {'name': 'Private Account:',    'value': nameinfo['private']},
        {'name': 'Verified:',   'value': nameinfo['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)

    em.set_footer(text='\u200b')
    em.timestamp = datetime.datetime.utcnow()  
    em.set_footer(text='Source Code: https://github.com/Ocryol1337/Instagram-Bot') # Please don't remove this part as i'm giving it to everyone :)
    em.set_thumbnail(url=f'https://api.popcat.xyz/instagram/pfp/{name}')
    await ctx.send(embed = em)


client.run("TOKEN HERE")
