""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""


import discord
from discord.ext import commands
from discord.ext.commands import Context

# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="testcommand",
        description="This is a testing command that does nothing.",
    )
    async def testcommand(self, context: Context) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        pass
    @commands.hybrid_command()
    async def kill(self,ctx, user: discord.User ) -> None:
        """ Do you dare?? """
        # Then responds in the channel with this messag
        await ctx.send(f"{user.name} Died")

    @commands.Cog.listener("on_message")
    async def listener_one(self, message):
     if message.content == "hi":
        await message.channel.send("hello", reference=message)


    @commands.Cog.listener("on_message")
    async def listener_two(self, message):
     if message.content == "https://cdn.discordapp.com/emojis/1157937726528700476.gif?size=48&name=Vibin&quality=lossless":
        emoji = self.bot.get_emoji(1157937726528700476)
        await message.add_reaction(emoji)


    @commands.Cog.listener("on_message")
    async def listener_four(self, message):
     if message.content == "https://cdn.discordapp.com/emojis/1169886085543903272.gif?size=48&name=DancingCat&quality=lossless":
        emoji1 = self.bot.get_emoji(1169886085543903272)
        await message.add_reaction(emoji1)


    @commands.Cog.listener("on_message")
    async def listener_five(self, message):
     if message.content == "https://cdn.discordapp.com/emojis/1170200140158619668.gif?size=48&name=Jeb&quality=lossless":
        emoji2 = self.bot.get_emoji(1170200140158619668)
        await message.add_reaction(emoji2)


    @commands.Cog.listener("on_message")
    async def listener_three(self, message):
     if message.content == "ping":
        await message.channel.send("pong", reference=message)
        
# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Template(bot))
