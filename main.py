import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Siema nie, tu {self.user}!')
        
    async def on_message(self, message):
        if message.author==self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'hello there {message.author}')
        #print(f'Message from {message.author}: {message.content}')
        
ticket = open("BotTicket.txt",'r').read()        
intents = discord.Intents.default()
intents.message_content=True

client = Client(intents=intents)
client.run(ticket)