import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.AutoShardedInteractionBot) -> None:
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Message sent from the file Ping.py")

    @commands.slash_command(name = "ping", description = "Ping ? Pong !")
    async def _ping(self, inter: disnake.CommandInteraction) -> None:
        await inter.send(f"🏓 Pong !\nMy latency is about **{int(self.__bot.latency * 1000)}ms**.")


def setup(self: commands.AutoShardedBot) -> None:
    self.add_cog(Ping(self))