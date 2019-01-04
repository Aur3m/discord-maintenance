
import discord

token = ""

client = discord.Client()



@client.event
async def on_ready():
    print(u'\n\nVous êtes connecté avec le compte {0.user}'.format(client) + '\n\n')


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    elif message.content == '!help':
        await client.send_message(message.channel, '`Bot that can create automatic channels when someone join : It creates a similar channel with a suffix or a prefix.\n\nYou need to be inside the specific voice channel you want to configure to use these commands :\n!addautochannel prefix [prefix you chose]\n!addautochannel suffix [suffix you chose]\n!removeautochannel\nThank you for adding the bot !`')

    elif "autochannel" in message.content:
        ch = message.content
        if ch[0] == "!":
            await client.send_message(message.channel, "The Bot is in maintenance mode right now. Please wait less than 24 hours and this function will be available.")

client.run(token)
