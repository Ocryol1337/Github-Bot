import discord
import requests
import json
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')


@client.command()
async def github(ctx, *, name: str = 'Ocryol1337') -> None:
    r       = requests.get(f"https://api.popcat.xyz/github/{name}")
    nameinfo     = r.json()
    em      = discord.Embed(color=000000)
    fields  = [ 
        {'name': 'Name:',          'value': nameinfo['name']},
        {'name': 'Bio:',     'value': nameinfo['bio']},
        {'name': 'Url:',     'value': nameinfo['url']},
        {'name': 'Account Type:',        'value': nameinfo['account_type']},
        {'name': 'Location:',   'value': nameinfo['location']},
        {'name': 'Twitter:',   'value': nameinfo['twitter']},
        {'name': 'Public Repos:',    'value': nameinfo['public_repos']},
        {'name': 'Followers:',     'value': nameinfo['followers']},
        {'name': 'Following:',         'value': nameinfo['following']},
        {'name': 'Email:',         'value': nameinfo['email']},
        {'name': 'Account Created:',   'value': str(nameinfo['created_at'])[0:10]},
    ]
    avatar_one = f"{nameinfo['avatar']}"
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)

    em.set_footer(text='\u200b')
    em.timestamp = datetime.datetime.utcnow()  
    em.set_footer(text='Source code: https://github.com/Ocryol1337/Github-Bot')#change for creator name 
    em.set_thumbnail(url=f'{avatar_one}')#for gif display
    await ctx.send(embed = em)


client.run("TOKEN HERE")
