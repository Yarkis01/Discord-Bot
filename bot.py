import sys ; sys.dont_write_bytecode = True

import disnake, os
from disnake.ext import commands

class Bot(commands.AutoShardedInteractionBot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def on_connect(self) -> None:
        print(f"Logged in as {self.user}!")

    async def on_ready(self) -> None:
        await self.change_presence(
            activity = disnake.Activity(
                name = "Disnake",
                type = disnake.ActivityType.watching
            ),
            status = disnake.Status.do_not_disturb
        )


if __name__ == '__main__':
    bot = Bot(
        intents     = disnake.Intents.default(),
        test_guilds = [0]
    )

    for file in os.listdir('./cogs/'):
        if not file.endswith(".py"):
            continue

        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"cogs.{file[:-3]} has been loaded!")

    bot.run("TOKEN")