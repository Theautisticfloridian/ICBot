import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = 'ic ')

@client.event
async def on_ready():
    activity = discord.Activity(name="Intersection Controller", type=discord.ActivityType.playing)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')

@client.command()
@has_permissions(administrator=True)
async def verify(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == 'IC player':
            await member.add_roles(role)

    await ctx.send(f'An administrator has successfully verified **{member}**')

@client.command()
async def cheats(ctx):
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(66, 135, 245),
        title="Cheats",
        description='**Here are the current "cheats" which will not break the game:**\n\n\n**Fps** - Displays an FPS counter.\n\n**RegnarDet?** - Forces the weather to rain.\n\n**TorsVrede** - Forces the weather to thunderstorm.\n\n**Solkatt** - Forces the weather to sunny.\n\n**Dimfilt** - Forces the weather to fog.\n\n**Väderlek or Vaderlek** - Sets the weather to the default dynamic setting.\n\n**Händelser or Handelser** - Random events are triggered as often as possible.\n\n**Ögonsten or Ogonsten** - Graphics settings not lowered when zooming out.\n\n**GömdaSaker or GomdaSaker** - Unlocks all decorative objects.\n\n**Uppdatera** - Opens the update link for your installation (shadowtree.se / Google Play / Amazon)\n\n**Blindstyre** - Disables vehicles stopping before crashed vehicles.',
        timestamp=ctx.message.created_at
    )
    await ctx.send(embed=embed)

client.run('NzQ3ODkyODQ2MTc4MzM2ODY4.X0VffQ.kShZQlSYj1nDK86BSkcxGNH5qpU')