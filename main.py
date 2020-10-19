import discord
import random
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = 'ic ')
token = open("token.txt", "r")
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Activity(name="Intersection Controller", type=discord.ActivityType.playing)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')

@client.command()
async def suggest(ctx, *, suggestion):
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        title=suggestion,
    )
    embed.set_footer(text=f'Suggested by {ctx.message.author}', icon_url=ctx.author.avatar_url)

    channel = ctx.bot.get_channel(600465489508171776)
    likes = await channel.send(embed=embed)
    like = ctx.bot.get_emoji(759059895424909380)
    dislike = ctx.bot.get_emoji(759060520455766036)
    await likes.add_reaction(like)
    await likes.add_reaction(dislike)
    await ctx.message.add_reaction('📬')

@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        title=f'Need some help?',
        timestamp=ctx.message.created_at
    )
    embed.add_field(name='Help', value='shows this command', inline=False)
    embed.add_field(name='Suggest', value='suggest a new feature to the Dev! it will be posted in <#600465489508171776>', inline=False)
    embed.add_field(name='Verify', value='verify a new user! required aarguments: `ic verify <user.mention> <nickname>` (admin-only)', inline=False)
    embed.add_field(name='Ping', value="checks the client's latency", inline=False)
    embed.add_field(name='Cheats', value='shows all the cheats', inline=False)

    await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def verify_everyone(ctx):
    for Member in ctx.guild.members:
        for role in Member.roles:
            if role.name == 'IC player':
                await Member.remove_roles(discord.utils.get(ctx.guild.roles, name='Unverified'))
    await ctx.send('Done!')

@client.command()
async def ping(ctx):
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        title=f'Pong! {round(client.latency * 1000)}ms',
        timestamp=ctx.message.created_at
    )
    await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def verify(ctx, member : discord.Member, *, nick):
    guild = ctx.guild
    chance=random.randint(0, 100)
    if chance < 5:
        response=f'{member.mention} **just got Intersection Controlled!**'
    else:
        response=f'**An administrator has successfully verified** {member.mention}**!**'

    for role in guild.roles:
        if role.name == 'IC player':
            await member.add_roles(role)
    for role in guild.roles:
        if role.name == 'Unverified':
            await member.remove_roles(role)
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        description=response,
        timestamp=ctx.message.created_at
    )
    await ctx.channel.purge(limit=1)
    await member.edit(nick=nick)
    await ctx.send(embed=embed)

@client.command()
async def cheats(ctx):
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        title="Cheats",
        description='**Here are the current "cheats" which will not break the game:**\n\n\n**Fps** - Displays an FPS counter.\n\n**RegnarDet?** - Forces the weather to rain.\n\n**TorsVrede** - Forces the weather to thunderstorm.\n\n**Solkatt** - Forces the weather to sunny.\n\n**Dimfilt** - Forces the weather to fog.\n\n**Väderlek or Vaderlek** - Sets the weather to the default dynamic setting.\n\n**Händelser or Handelser** - Random events are triggered as often as possible.\n\n**Ögonsten or Ogonsten** - Graphics settings not lowered when zooming out.\n\n**GömdaSaker or GomdaSaker** - Unlocks all decorative objects.\n\n**Uppdatera** - Opens the update link for your installation (shadowtree.se / Google Play / Amazon)\n\n**Blindstyre** - Disables vehicles stopping before crashed vehicles.',
        timestamp=ctx.message.created_at
    )
    await ctx.send(embed=embed)

client.run(token.read())