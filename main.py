import os
import discord
from dotenv import load_dotenv
import requests
import json

load_dotenv()

CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
AGENT_ID = os.getenv('AGENT_ID')
UID = os.getenv('UID')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)


def call_api(utterance):
    url = "https://api-mebo.dev/api"
    headers = {"Content-Type": "application/json"}
    data = {
        "api_key": "bc222440-dacc-44c7-9fb3-4839616b72a0187601cbf571e5",
        "agent_id": "2030c8a3-5e4c-417a-bc52-abde6533fcc8186de7095d116",
        "utterance": utterance,
        "uid": "be85ac08-f19f-42b8-97c9-25d9db90a2911876025e1a01a7",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author.bot or message.channel.id != CHANNEL_ID:
        return

    if client.user in message.mentions:
        print(f"{message.content}")
        response = call_api(message.content)
        print(f"{response}")
        await message.reply(response['bestResponse']['utterance'])

client.run(BOT_TOKEN)
