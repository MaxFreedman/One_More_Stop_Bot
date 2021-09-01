# Commands handled on event
import discord
from discord.ext import commands
import asyncio


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned.", delete_after=2.0)
        await ctx.message.delete()

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.", delete_after=2.0)
        await ctx.message.delete()

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (
                    member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned: {user.mention}",
                                       delete_after=2.0)
                await ctx.message.delete()

    @commands.command(aliases=['tempmute'])
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member = None, time="5m", *,
                   reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        try:
            # Gets the numbers from the time argument, start to -1
            seconds = time[:-1]
            duration = time[-1]  # Gets the timed maniulation, s, m, h, d
            if duration == "s":
                seconds = seconds * 1
            elif duration == "m":
                seconds = seconds * 60
            elif duration == "h":
                seconds = seconds * 60 * 60
            elif duration == "d":
                seconds = seconds * 86400
            else:
                await ctx.send("Invalid duration input")
                return
        except Exception as e:
            print(e)
            await ctx.send("Invalid time input")
            return

        await member.add_roles(mutedRole, reason=reason)
        await ctx.channel.send(f"Muted: {member.mention} by"
                               " {ctx.author.mention} for {time}",
                               delete_after=2.0)
        await asyncio.sleep(seconds)
        await member.remove_roles(mutedRole)

    @commands.command(name="unmute")
    @commands.has_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await ctx.channel.send(f"Unmuted: {member.mention}",
                               delete_after=2.0)
        await ctx.message.delete()

    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.author.send("```Available Commands:\n"
                              "bebetter\n"
                              "bebutter\n"
                              "deadpool\n"
                              "ektar\n"
                              "flickr\n"
                              "hasbeen\n"
                              "homework\n"
                              "lomo\n"
                              "minecraft\n"
                              "police\n"
                              "termin8or\n"
                              "thatsfire\n"
                              "thatstrashfire```"
                              )
        await ctx.message.delete()

# Setup ----------------------------------------------------------------------


def setup(bot):
    bot.add_cog(AdminCommands(bot))
