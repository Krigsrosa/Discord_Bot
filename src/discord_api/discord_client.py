import os
import discord
from dotenv import load_dotenv
from discord.client import Client
from discord.flags import Intents
from discord.message import Message
from openai_api.openai_connection import get_gpt_response
from openweather_api.current_weather import get_weather_response
from typing import Dict, List, Any

load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")

bot_caller: List[str] = ["/regras", "/bot", "/weather"]

class CustomDiscordClient(Client):
    async def on_ready(self):
        print(f"Logged in as user {self.user}")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}. Seja bem vindo!'
            await guild.system_channel.send(content=mensagem)

    async def on_message(self, message):
        message_content: str = message.content
        if bot_caller[0] in message_content:
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1 - Não desrespeitar os membros')
        elif bot_caller[1] in message_content:
            prompt: str = message_content.split(bot_caller[1])[1]
            chat_gpt_response: str = get_gpt_response(question=prompt)
            if chat_gpt_response:
                await message.channel.send(content=chat_gpt_response)
        elif bot_caller[2] in message_content:
            prompt: str = message_content.split(bot_caller[2])[1]
            weather_response: str = get_weather_response(city=prompt)
            if weather_response:
                mensagem = f'{message.author.name}, o clima atual de{weather_response[0]} é:{os.linesep}Clima: {weather_response[1]}{os.linesep}Temperatura: {weather_response[2]}{os.linesep}Sensação Térmica: {weather_response[3]}{os.linesep}Humidade: {weather_response[6]}{os.linesep}Velocidade do Vento: {weather_response[7]}'
                await message.channel.send(content=mensagem)

intents = Intents.default()
intents.message_content = True
custom_discord_client: CustomDiscordClient = CustomDiscordClient(intents=intents)