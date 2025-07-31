import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_weather(city):
    url = f'https://wttr.in/{city}?format=3'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error. Unable to fetch weather data."
class MyClient(discord.Client):

    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

        if message.content.startswith('$weather'):
            parts = message.content.split(' ', 1)
            if len(parts) == 2:
                city = parts[1]
                weather = get_weather(city)
                await message.channel.send(weather)
            else:
                await message.channel.send("🌍 Usage: `$weather <city>`")

    async def on_ready(self):
        print('Logged on as, {0}!'.format(self.user))
    
intents = discord.Intents.default()
intents.message_content = True 

client = MyClient(intents=intents)
client.run('YOUR_DISCORD_BOT_TOKEN') 