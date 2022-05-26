from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)

    @_clear.error
    async def register_error(self, error, ctx):
        await ctx.send("Error al registrarte, intenta contactar a un moderador.")


def setup(client):
    client.add_cog(Admin(client))