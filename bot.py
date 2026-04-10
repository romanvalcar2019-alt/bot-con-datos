import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def eco(ctx, accion, *, dato=""):
    if accion == "donde": 
        guia = {"aceite": "Punto Limpio", "pila": "Contenedor rojo/tienda", "vidrio": "Iglú verde"}
        await ctx.send(f"📍 **{dato.capitalize()}** debe ir a: {guia.get(dato.lower(), 'Consulta tu centro local.')}")
    elif accion == "ahorro": 
        tips = ["Lava a 30°C", "Usa modo ECO", "Apaga el stand-by"]
        await ctx.send(f"💡 **Tip de ahorro:** {random.choice(tips)} (Ahorra hasta un 10% anual).")
    elif accion == "pass": 
        await ctx.author.send(f"Contraseña segura: `{random.choice(['Bosque','Oceano','Solar'])}{random.randint(10,99)}#`")

bot.run("TOKEN")
