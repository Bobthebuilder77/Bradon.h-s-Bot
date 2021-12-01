##############################
# IMPORTS

import discord
from discord.ext import commands
import datetime
import time
import requests
import json
from replit import db
from keep_alive import keep_alive

##############################
# PUBLIC VARIABLES AND SETUP

start_time = time.time()
token = open("token.txt", "r").read()
client = commands.Bot(command_prefix='.')  #Defines client
matches = db.prefix(".")
client.remove_command("help")


@client.event
async def on_ready():
    # Bot Presence:
    await client.change_presence(status=discord.Status.idle,
                                 activity=discord.Game(
                                     type=discord.ActivityType.playing,
                                     name="in the workshop! | .help"))

    print('{0.user} has successfully logged in to Discord API.'.format(client))
    print('We have logged in as {0.user}'.format(client))


##############################
# PING


@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')


##############################
# NOTPING (EASTER EGG)


@client.command(name='notping')
async def notPing(ctx):
    await ctx.send("Hooray! You have just found an easter egg.")


##############################
# ABOUT BOT


@client.command(name='aboutbot')
async def aboutBot(ctx):
    await ctx.send(
        "SSSHH! Looks like I'm in use... NOTE: I will remain in the workshop until further notice, so I can better do my job as a bot. :thumbsup: The bot owner will announce everything you need to know to you on the main server. Server link: https://discord.gg/CuQM2g3f6F"
    )


##############################
# INVITE


@client.command(name='invite')
async def invite(ctx):
    await ctx.send(
        "smh. This bot is not currently set to 'Public'. Please content the bot owner to check it out, AKA: AbsoluteGamer#9759."
    )


##############################
# INSPIRE


@client.command(name='inspire')
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


##############################
# HELP


@client.command(name='help')
async def help(ctx):
    #helpEmbed = discord.Embed(colour=discord.Colour.blue())
    helpEmbed = discord.Embed(colour=0x206694)
    helpEmbed.set_author(name='Help : list of commands available')
    helpEmbed.add_field(name='.help',
                        value='Get the list of commands',
                        inline=False)
    helpEmbed.add_field(name='.ping',
                        value='Latency in milliseconds',
                        inline=False)
    helpEmbed.add_field(name='.aboutbot',
                        value='Info about the bot.',
                        inline=False)
    helpEmbed.add_field(name='.inspire',
                        value='Do this command to get an inspirational quote.',
                        inline=False)
    helpEmbed.add_field(name='.invite',
                        value='Invites the bot to your server.',
                        inline=False)
    helpEmbed.add_field(
        name='.uptime',
        value=
        'Shows how long the bot has been running (in seconds)',  #How long the bot has been running (in seconds)
        inline=False)

    await ctx.send(embed=helpEmbed)


##############################
# UPTIME


@client.command(name='uptime')
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text="<Gamers Up!>")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)


##############################
# PROFILE STATS
### NOTE: LINES 25 & 28 ARE VALID ###

##############################
#react to any message that contains 'drama'

#### NOTE: DO NOT DELETE LINES 150 TO 157 ####


#@client.event
#async def on_message(ctx):
#if 'drama' in ctx.content:
#emoji = '\N{EYES}'
#await ctx.add_reaction(emoji)

##############################
# END OF CODE

keep_alive()
client.run(token)  #Initializes the bot
