import robloxpy
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="-")
@bot.command(pass_context=True)
async def robloxasset(id):
    embed = discord.Embed(title="Roblox Asset Information")
    embed.add_field(name="Created At",value=robloxpy.Asset.created_at(id))
    embed.add_field(name="Is Limited", value=robloxpy.Asset.is_limited(id))
    embed.add_field(name="Is New",value=robloxpy.Asset.is_new(id))
    embed.add_field(name="Price (Tickets)", value=robloxpy.Asset.price_in_tickets(id))
    embed.add_field(name="Price (Robux)", value=robloxpy.Asset.price_in_robux(id))
    embed.add_field(name="Is For Sale", value=robloxpy.Asset.is_for_sale(id))
    embed.add_field(name="Sales", value=robloxpy.Asset.sales(id))
    await bot.say(embed=embed)
bot.run("your_token_here")
