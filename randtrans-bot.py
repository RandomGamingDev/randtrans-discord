import discord
import randtrans

TOKEN = "" # Put your token here
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Client Started!\nLoading Server List...")
    print("SERVERS:\n--------")
    for guild in client.guilds:
        print(str(guild.name) + ': \n' + "ID: " + str(guild.id) + ", " + "COUNT: " + str(guild.member_count) + '\n')
    print("Loaded Server List!\nWe have logged in as {0.user}!".format(client))

@client.event
async def on_message(message):    
    if message.author == client.user:
        return

    command = message.content.split(' ', 3)
    if len(command) < 4:
        return
    if command[0] == "randtrans":
        await message.channel.send(randtrans.RandomlyTranslate(command[3], command[1], int(command[2])))

client.run(TOKEN)
