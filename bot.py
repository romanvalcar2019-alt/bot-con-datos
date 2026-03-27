import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):
    with open('images/MEME1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def list(ctx):
    imageName = random.choice(os.listdir("images"))
    with open(f"images/{imageName}", "rb") as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
@bot.command()
async def animales(ctx):
    # Elegimos un archivo aleatorio de la subcarpeta 'animales'
    folder = "images/animales"
    imageName = random.choice(os.listdir(folder))
    
    with open(f"{folder}/{imageName}", "rb") as f:
        picture = discord.File(f)
        await ctx.send("¡Aquí tienes un meme de animales!", file=picture)

def get_dog_image_url():    
    url = ' https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
bot.run("TOKEN")
