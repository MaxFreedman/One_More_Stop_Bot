import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

# channel to post join/leave messages to
join_leave_channel = os.environ['general']

# randomized messages for leave description
welcome = [
    "You hear the slap of a mirror in the distance...",
    "\"That's fire!\" whispers in the breeze...",
    "A street photographer springs out from an alley...",
    "An off camera flash temporarily blinds you...",
    "A fresh roll of Ektar 100 gets loaded...",
    "The autofocus chirps...",
]

farewell = [
    "**Footsteps echo into the distance...**",
    "**Only a camera remains, broken and discarded....**",
    "**Cursing ensued, children cried, & the cops were called...**",
    "**Everyone stopped and stared....**",
    "**That wasn't very fire....**",
    "**Denial, anger, bargaining, depression, and acceptance...**"
]


class OnEventCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(join_leave_channel)
        join_msg = discord.Embed(
            title=f"Welcome to {member.guild.name}, {member.name}!",
            color=0xFFAFDE)
        join_msg.set_author(
            name=random.choice(welcome)
        )
        join_msg.add_field(
            name="Reminder!",
            value=f"{member.mention}, be sure to check out "
            " <#756743311011741747> and <#756327485473423381>. They let other"
            " members of the server know more about what types of cameras,"
            " formats, and styles you shoot, and you can also change your name"
            " color there!"
        )
        join_msg.set_footer(
            text=f"({member.guild.member_count} members!)")
        await channel.send(embed=join_msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(join_leave_channel)
        remove_msg = discord.Embed(
            title=f"{member.display_name}'s film back opened mid roll.",
            description=random.choice(farewell),
            color=0x4F545C)
        remove_msg.set_author(
            name="A moment of silence.",
        )
        remove_msg.set_footer(
            text=f"({member.guild.member_count} members!)")
        await channel.send(embed=remove_msg)


# Setup ----------------------------------------------------------------------
def setup(bot):
    bot.add_cog(OnEventCommands(bot))
