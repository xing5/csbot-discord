import os
import json
import discord
from discord.ext import commands
from qa import answer_question
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.typing = True 
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

def get_answer(question):
    try:
       answer = answer_question(question)
       return answer
    except Exception as e:
        return f"An error occurred while fetching the answer from the API. {e}"

@bot.command(name='ask')
async def ask_question(ctx, *, question):
    async with ctx.typing():
        answer = get_answer(question)
        await ctx.send(answer)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord and is ready to answer questions!')


TOKEN = "xxx"

if __name__ == "__main__":
    bot.run(TOKEN)
