import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
dlugosc_rozkladu = [
'Butelki plastikowe (PET) - do 450 lat',
'Torby plastikowe - 10 do 1000 lat',
'Puszki aluminiowe - 80 do 200 lat',
'Kubki styropianowe - ponad 500 lat',
'Szkło - 1 milion lat lub nigdy się nie rozkłada',
'Papierowe ręczniki - 2 do 4 tygodni',
'Gazety - 6 tygodni',
'Skórka od banana - 2 lata',
'Buty gumowe - 50 do 80 lat',
'Baterie - 100 lat',
'Filtry do papierosów - 10 do 12 lat',
'Pieluchy jednorazowe - 450 do 500 lat',
'Kapsułki do kawy - 150 do 500 lat',
'Karty plastikowe - do 1000 lat',
'Papierowe torby - około 1 miesiąc',
'Chusteczki higieniczne - 3 do 4 miesiące',
'Zapałki - 6 miesięcy',
'Drewniane meble - 13 do 100 lat',
'Ubrania bawełniane - 5 miesięcy do 1 roku',
'Ubrania syntetyczne - kilkaset lat',
'Tetra Pak - do 30 lat',
'Gumy do żucia - do 5 lat',
'Sznurki i liny - 3 do 14 miesięcy',
'Plastikowe butelki na wodę - 450 lat',
'Papierowa chusteczka - 3 miesiące',
'Karton mleczny - do 5 lat',
'Zębatki z drewna - 13 lat',
'Siatki rybackie - do 600 lat',
'Kubki papierowe z powłoką - 30 lat',
'Butelki szklane - 1 milion lat',
]

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    pictures_name = os.listdir('images')
    meme = random.choice(pictures_name)
    with open(f'images/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def odpad(ctx):
    o = random.choice(dlugosc_rozkladu)
    await ctx.send(o)

bot.run("TOKEN")
