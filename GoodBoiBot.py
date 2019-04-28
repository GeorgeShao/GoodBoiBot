from discord.ext.commands import Bot

BOT_PREFIX = "/gbb"
file = open("TOKEN.txt","r")
TOKEN = file.read()

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    #Prevents bot from responding to other bots, including itself.
    if message.author.bot:
        return

@client.command()
async def ping():
    await client.say("pong")

@client.command()
async def square(number: int):
    answer = number ** 2
    await client.say(f"{number} squared is {answer}")

client.run(TOKEN)