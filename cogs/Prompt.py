import discord
from discord.ext import commands
import random


# Prompt Attributes ----------------------------------------------------------
emulsion = ["**black and white**",
            "**color negative**",
            "**color positive**"]
emulsion2 = ["**black and white**",
             "**color negative**"]
film_speed = ["**50**",
              "**100**",
              "**160**",
              "**200**",
              "**400**",
              "**800**"]
push_pull = ["**box speed**",
             "**box speed**",  # entered twice to increase chance
             "**+1**",
             "**+2**",
             "**-1**",
             "**-2 **"]
subject = ["**isolated object**",
           "**self portrait**",
           "**low perspective**",
           "**bushes**",
           "**flowers**",
           "**still life**",
           "**hard light**",
           "**long exposure**",
           "**night photography**",
           "**double exposure**",
           "**trees**",
           "**abstract**",
           "**architecture**",
           "**diptych**",
           "**opposites**",
           "**\"Group\" f/64**"]

rand = random.choice


class PromptCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['prompt', 'hw'])
    @commands.has_permissions(ban_members=True)
    async def homework(self, ctx):
        if rand(emulsion) == "**color positive**":
            homework = discord.Embed(
                title="Photography Assignment:",
                color=discord.Colour.random(),
                description="Shoot a roll of __" + rand(film_speed) +
                "__ speed __**color positive**__ film at __**box speed**__"
                " with a focus on __" + rand(subject) + "__.")
            await ctx.send(embed=homework)
        else:
            homework = discord.Embed(
                title="Photography Assignment:",
                color=discord.Colour.random(),
                description="Shoot a roll of __" + rand(film_speed) +
                "__ speed __" + rand(emulsion2) +
                "__ film at __" + rand(push_pull)
                + "__ with a focus on __" + rand(subject) + "__.")
            await ctx.send(embed=homework)


# Setup ----------------------------------------------------------------------
def setup(bot):
    bot.add_cog(PromptCommand(bot))
