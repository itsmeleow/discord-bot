# DISCORD BOT by Ieo#0002
import discord
import random
import json
from discord.ext import commands, tasks
# ENTER DISCORD BOT TOKEN IN THE ''
# ENTER COMMAND PREFIX IN THE ''
token = 'NzMwMTE2NTQyNTYxMzg2NTc3.Xxh4xQ.HQvlwaXg8OB3d3ErDDlnET75bUM'
client = commands.Bot(command_prefix = '.')


# ACTIVITY
@client.event
async def on_ready():
    print('Ready')
    print('Logged in as {0.user}'.format(client))
    game = discord.Game(name=".help")
    await client.change_presence(activity=game)


# LOGS
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# ERRORS
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        title='Error',
        description='Invalid Command',
        colour=discord.Colour.default()
    )
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        title='Error',
        description='Missing Permissions',
        colour=discord.Colour.default()
    )
        await ctx.send(embed=embed)


# MODERATION
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title='Action',
        description=(f'{member} has been kicked.'),
        colour=discord.Colour.default()
    )
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title='Action',
        description=(f'{member} has been banned.'),
        colour=discord.Colour.default()
    )
    embed.set_author(name=member, icon_url=member.avatar_url)
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guid.unban(user)
            await ctx.send(f'{member} has been unbanned.')
        return


# OTHER
@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title='Pong! ' + (f'{round(client.latency * 1000)}ms'),
        colour=discord.Colour.default()
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
@client.command()
async def ball(ctx, *, question):
    responses = [
                'It is certain.','Without a doubt','Yes - definitely.','Most likely.','Yes.',
                'Yessir','Sure.','Ask again later.','Cannot predict now.','My reply is no.',
                'My sources say no.','Very doubtful.','Outlooks not good.','No.','Ask again.'
                ]
    embed = discord.Embed(
        title=random.choice(responses),
        colour=discord.Colour.default()
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx):
    embed = discord.Embed(
        title='KITH X COCA-COLA',
        description='[Click here to sign up](https://forms.gle/iDFUTVwdwGuJUjHc7)',
        colour=discord.Colour.default()
    )
    embed.set_image(url='https://media.discordapp.net/attachments/728893994423287818/743988725704425532/unknown.png?width=766&height=333')
    embed.add_field(name=':date: Release Date', value='August 15', inline=True)
    embed.add_field(name=':moneybag: PAS Fee', value='$5', inline=True)
    embed.add_field(name=':alarm_clock: Close Time', value='Today @ 11pm est', inline=True)
    embed.add_field(name=':bell: Important Info', value='[Lookbook](https://kith.com/blogs/news/a-closer-look-at-kith-x-coca-cola-2020)', inline=True)
    embed.add_field(name='Have questions?', value='[Make a support ticket](https://discordapp.com/channels/670051671598170123/731191234881912863/731192361174040617)', inline=True)
    await ctx.send(embed=embed)
@client.command()
async def faq(ctx):
        embed = discord.Embed(
        title='FAQ',
        colour=discord.Colour.default()
    )
        embed.add_field(name='• What is an ACO?', value='ACO is Auto checkout, in other words, we will run your profile and try to cop you the item.', inline=False)
        embed.add_field(name='• What is PAS?', value='PAS (Pay After Success) means that you will only pay after the bot shows success.', inline=False)
        embed.add_field(name='• How much is the fee?', value='The fee depends on each drop and will be stated on the form', inline=False)
        await ctx.send(embed=embed)
@client.command()
async def suggest(ctx, *args):
    if ctx.author == client.user:
        return
    suggestion = ""
    for arg in args:
        suggestion += arg + " "

    embed = discord.Embed(description=suggestion)
    embed.set_author(name=ctx.author.name + " suggested:", icon_url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author.id)
    await ctx.message.delete()
    sent_message = await ctx.send(embed=embed)
    await sent_message.add_reaction("✅")
    await sent_message.add_reaction("❌")



client.run(token)