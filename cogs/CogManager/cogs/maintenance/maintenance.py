from redbot.core import commands, checks
from redbot.core import Config
import os
import json


class Maintenance(commands.Cog):

    @checks.admin_or_permissions()
    @commands.command()
    async def gitpull(self, ctx: commands.Context):
        os.system('cd ~/TheHatBot/ && git pull')
        await ctx.send("I pulled the code!")

    @checks.admin_or_permissions()
    @commands.command()
    async def gitreset(self, ctx: commands.Context):
        os.system('git rev-parse HEAD | git reset --hard')
        await ctx.send("I reset to the latest local git hash.")

    @checks.admin_or_permissions()
    @commands.command()
    async def updateRed(self, ctx: commands.Context):
        os.system('pyenv shell ACM_BOT && python -m pip install --upgrade Red-DiscordBot')
        # sed -i '' -e 's/\.is_owner/.admin_or_permissions/g' s/regex/replacement/
        os.system("find /home/pi/.pyenv/versions/ACM_BOT/lib/python3.8/site-packages/redbot/ -type f -name \"*.py\" -exec sed -r -i'' -e 's/\.is_owner/.admin_or_permissions/g' {} +")
        await ctx.send("The redbot python package has been updated and the necessary changes to the packages has been made.")

    @checks.admin_or_permissions()
    @commands.command()
    async def reinstallRed(self, ctx: commands.Context):
        os.system('pyenv shell ACM_BOT && python -m pip install --upgrade --force-reinstall Red-DiscordBot')
        # sed -i '' -e 's/\.is_owner/.admin_or_permissions/g' s/regex/replacement/
        os.system( "find /home/pi/.pyenv/versions/ACM_BOT/lib/python3.8/site-packages/redbot/ -type f -name \"*.py\" -exec sed -r -i'' -e 's/\.is_owner/.admin_or_permissions/g' {} +")
        await ctx.send("The redbot python package has been reinstalled and the necessary changes to the packages has been made.")

    @checks.admin_or_permissions()
    @commands.command()
    async def restartBot(self, ctx: commands.Context):
        os.system('sudo systemctl restart red@TheHatBot')
        await ctx.send("I will be back.")

    @checks.admin_or_permissions()
    @commands.command()
    async def viewLogs(self, ctx: commands.Context, *args: str):
        if not args:
            return await ctx.send_help()
        args.split()
        os.system(f'cd ~/TheHatBot/logs && journalctl --since -u red@TheHatBot -o json-pretty --no-pager > test.json')

        @checks.admin_or_permissions()
        @commands.command()
        async def test(self, ctx: commands.Context, *args: str):
            if not args:
                return await ctx.send_help()
            return await ctx.send(args)