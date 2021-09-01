import discord
from datetime import datetime
from discord.ext import commands
import random

# Random butter --------------------------------------------------------------
butter = ["https://tinyurl.com/3mxmjysu",
          "https://tinyurl.com/537xppet",
          "https://tinyurl.com/75r3fzca",
          "https://tinyurl.com/ytc9z4jk",
          "https://tinyurl.com/d2cm5nw",
          "https://tinyurl.com/3jtuvtk5",
          "https://tinyurl.com/2hzawas9",
          "https://tinyurl.com/yfr8svht",
          "https://tinyurl.com/7x25m488",
          "https://tinyurl.com/y6p3yjn8",
          "https://tinyurl.com/2mxn76wa",
          "https://tinyurl.com/dpzy5pxa",
          "https://tinyurl.com/3d3vt6fy"]


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bebutter')
    async def bebutter(self, ctx):
        bebutter = discord.Embed(
            color=0xffea00)
        bebutter.set_image(
            url=random.choice(butter))
        await ctx.channel.send(embed=bebutter)

    @commands.command(name='bebetter')
    async def bebetter(self, ctx):
        bebetter = discord.Embed(
            description="Your actions and commentary negatively impact our"
            " efforts to build a positive community. It creates a hostile"
            " space for current members and reduces the likelihood that a new"
            " member stays in the server if their first impression is"
            " normalized toxicity. **Change your behavior. Be better.**",
            color=0xff0000)
        bebetter.set_footer(
            text="Continuing to act like this will result in a loss of"
            " privileges or ban.")
        await ctx.channel.send(embed=bebetter)

    @commands.command(name="deadpool")
    async def deadpool(self, ctx):
        deadpool = discord.Embed(
            title="**Twenty three photographers attempt the impossible.**",
            description="https://liquid.hotpinkbulb.uk/",
            color=0x4CB8A1)
        deadpool.set_image(
            url="https://tinyurl.com/2astrxpk")
        deadpool.set_footer(
            text="Who will remain? Find out ")
        deadpool.timestamp = datetime(2022, 1, 2)
        await ctx.channel.send(embed=deadpool)

    @commands.command(name='ektar')
    async def ektar(self, ctx):
        ektar = discord.Embed(
            title="Ektar just isn't my favorite",
            color=0x4F545C)
        ektar.set_image(
            url='https://tinyurl.com/cm8deu54')
        await ctx.channel.send(embed=ektar)

    @commands.command(name='flickr')
    async def flickr(self, ctx):
        flickr = discord.Embed(
            title="One More Stop",
            description="Join us for prime pixel peeping glory.",
            url='https://www.flickr.com/groups/onemorestop',
            color=0xffffff)
        flickr.set_thumbnail(
            url='https://tinyurl.com/2cuvnemt')
        flickr.set_footer(
            text="Ektar, our beloved.")
        await ctx.channel.send(embed=flickr)

    @commands.command(name='hasbeen')
    async def hasbeen(self, ctx):
        await ctx.send("🌍 :astronaut: 🔫👩‍🚀")
        # Deletes the command that called it
        await ctx.message.delete()

    @commands.command(name='lomo')
    async def lomo(self, ctx):
        lomo = discord.Embed(
            title="Komrades",
            description="In Soviet Russia, we only shoot Ленинградское"
            " Oптико-Mеханическое Oбъединение in our лпькьузчьу щаьу ущь!",
            color=0x9100B1)
        await ctx.channel.send(embed=lomo)

    @commands.command(name='minecraft')
    async def minecraft(self, ctx):
        minecraft = discord.Embed(
            title="Minecraft Java server (ver. 1.17.1) address:",
            description="**onemorestop.duckdns.org**",
            color=0x75cc72)
        minecraft.set_thumbnail(
            url='https://tinyurl.com/ax4fe3pc')
        minecraft.set_footer(text="Server members must be whitelisted")
        await ctx.channel.send(embed=minecraft)

    @commands.command(name='police')
    async def police(self, ctx):
        police = discord.Embed(
            title=":rotating_light: WOOP WOOP :rotating_light: ",
            description="That's the sound of da police",
            color=0x4F545C)
        police.set_image(
            url='https://tinyurl.com/48tr5pnu')
        await ctx.channel.send(embed=police)

    @commands.command(aliases=['terminator'])
    async def termin8or(self, ctx):
        termin8or = discord.Embed(
            color=0x50E3C2)
        termin8or.set_image(
            url='https://tinyurl.com/55wmb427')
        await ctx.channel.send(embed=termin8or)

    @commands.command(name='thatsfire')
    async def thatsfire(self, ctx):
        thatsfire = discord.Embed(
            title="You hear the clattering of cameras behind you as you walk.",
            description="You quicken your pace.\n"
                        "The sounds draw closer.\n"
                        "You hear shallow, raspy breathing.\n"
                        "The hair on your neck stands on end.\n",
            color=0xD0021B)
        thatsfire.add_field(
            name="**A shutter clicks**",
            value="*A man whispers in your ear...*",
            inline=False
        )
        thatsfire.add_field(
            name="**That's fire**",
            value="You turn around and realize you're alone\n"
                  "The sound echoes into the night...\n",
            inline=False
        )
        thatsfire.set_image(
            url='https://tinyurl.com/ufd4237u')
        await ctx.channel.send(embed=thatsfire)

    @commands.command(aliases=['trashfire'])
    async def thatstrashfire(self, ctx):
        thatstrashfire = discord.Embed(
            description="⁣:fire_extinguisher::fire::wastebasket::fire:"
                        ":fire_extinguisher::fire::wastebasket::fire:"
                        ":fire_extinguisher::fire::wastebasket::fire:"
                        ":fire_extinguisher::fire::wastebasket::fire:"
                        ":fire_extinguisher::fire::wastebasket::fire:"
                        ":fire_extinguisher:",
            color=0xDDBB65)
        thatstrashfire.set_image(
            url='https://tinyurl.com/m2hsasdc')
        await ctx.channel.send(embed=thatstrashfire)

# Setup ----------------------------------------------------------------------


def setup(bot):
    bot.add_cog(MiscCommands(bot))
