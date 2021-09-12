from discord.ext import commands, tasks
from coincappy import CoinMarketCap
import discord
import random
import sqlite3 as sql
import utility
import cryptocompare


TKNS = [
  "ODQwNzEwMDM3NTgwMjgzOTE0.YJcKPA.w7ylZe1sgfbTRRy2GnnHOAILsvk"
  ]
TOKEN = TKNS[0]

intents = discord.Intents.default()
intents.members = True
intents.typing = False
bot = commands.Bot(command_prefix="$", case_insensitive=True, intents=intents)
bot.remove_command("help")
cmc = CoinMarketCap("9fafa4e9-1891-42cb-b765-a105c2bd6639")

@bot.event
async def on_ready():
  print("Crypto Online")


@bot.command(name="convert", aliases=['c'])
async def convertCurrencies(ctx, c1, c2):
    price = cryptocompare.get_price(c1, c2)
    embed=discord.Embed(description="""
    """, color=int("2f3136", 16))
    embed.set_author(name=f'1 {c1} = {price[c1][c2]} {c2}', icon_url="https://cdn.discordapp.com/attachments/819322820177297408/842198260742488064/iconEnlarged.png")
    await ctx.send(embed=embed)


@bot.command(name = "value", aliases=["v"])
async def  value(ctx, symbol):
    symbol = symbol.upper()
    response = cmc.crypto_quotes(symbol=symbol)
    stringedResponse = str(round(response[symbol][0]['quote']['USD']['price'], 3))
    p1h = str(round(response[symbol][0]['quote']['USD']['percent_change_1h'], 3))
    p24h = str(round(response[symbol][0]['quote']['USD']['percent_change_24h'], 3))
    p7d = str(round(response[symbol][0]['quote']['USD']['percent_change_7d'], 3))
    p30d = str(round(response[symbol][0]['quote']['USD']['percent_change_30d'], 3))
    p90d = str(round(response[symbol][0]['quote']['USD']['percent_change_90d'], 3))
    
    name = response[symbol][0]['name']
    print(name)
    iconUrl = utility.fetchIcon(name.replace(" ", "-").replace(".", "-"))

    embed=discord.Embed(title=f"Statistics for {name}:", description=f"""
    **Price:** {stringedResponse} USD
    **Percent changed, 1 hour:** {p1h}%
    **Percent changed, 24 hours:** {p24h}%
    **Percent changed, 7 days:** {p7d}%
    **Percent changed, 30 days:** {p30d}%
    **Percent changed, 90 days:** {p90d}%
    """, color=int("2f3136", 16))

    embed.set_author(name=f"Data gathered from coinmarketcap.com", icon_url=iconUrl)
    await ctx.send(embed=embed)


@bot.command(aliases=["help"])
async def helpCMD(ctx):
  embed=discord.Embed(description="""
  `$value [SYMBOL]` get the value and statistics from a crypto. 
  `$stats` - The bot's statistics, such as amount of servers it is in.
  `$help` this!
  """, color=int("2f3136", 16))
  embed.set_author(name="Crypto Help Page")
  await ctx.send(embed=embed)


@bot.command(name = "statistics", aliases=["stats"])
async def  statsCMD(ctx):
  embed = discord.Embed(description=f"""
  **Servers:** {len(bot.guilds)}
  **Developer:** SpicyJungle#1111
  **Version:** Beta

  **[Join the support server!](https://discord.gg/Zvt4cesG)**
  """, color=int("2f3136", 16))
  embed.set_author(name="Crypto Bot Info", icon_url="https://cdn.discordapp.com/attachments/819322820177297408/840734342417219594/icon.png")
  
  await ctx.send(embed=embed)



bot.run(TOKEN)

