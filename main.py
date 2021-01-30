# discord moderation bot made with <3 by Ieo#0002


import discord
import random
import json
from discord.ext import commands, tasks
import time
token = 'ENTER_TOKEN_HERE'
# change by replacing ' ' with your desired command prefix
client = commands.Bot(command_prefix = '.')


# check bot ready; discord presence - shows bot playing ' '
@client.event
async def on_ready():
    print('Ready')
    print('Logged in as {0.user}'.format(client))
    game = discord.Game(name=".help")
    await client.change_presence(activity=game)


# log join/leaves in cmd
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# check for errors on commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        title='Error',
        description='Invalid Command',
        color=discord.Color(3553600)
    )
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        title='Error',
        description='Missing Permissions',
        color=discord.Color(3553600)

    )
        await ctx.send(embed=embed)


# mod commands (clear messages, kick/ban members)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title='Action',
        description=(f'{member} has been kicked'),
        color=discord.Color(3553600)
    )
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title='Action',
        description=(f'{member} has been banned'),
        color=discord.Color(3553600)
    )
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.send(embed=embed)


# other (pong, 8ball, check avatar)
@client.command()
async def ping(ctx):
    embed = discord.Embed(
        description='Pong! ' + (f'{round(client.latency * 1000)}ms'),
        color=discord.Color(3553600)
    )
    await ctx.send(embed=embed)

@client.command()
async def ball(ctx, *, question):
    responses = [
                'It is certain.','Without a doubt','Yes - definitely.','Most likely.','Yes.',
                'Sure.','Ask again later.','Cannot predict now.','My reply is no.',
                'My sources say no.','Very doubtful.','Outlooks not good.','No.','Ask again.'
                ]
    embed = discord.Embed(
        title=random.choice(responses),
        color=discord.Color(3553600)
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def av(ctx):
    embed = discord.Embed(
        color=discord.Color(3553600)
        )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)




client.run(token)