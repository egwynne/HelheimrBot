import pandas as pd
from discord.ext import commands
from functions.yeah import save
from functions.creator import createEmbed


class Character(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='register')
    async def _register(self, ctx):
        registered = pd.DataFrame(pd.read_csv('.\data\\registered.csv', header=0))
        if ctx.message.author.id in registered['id'].values:
            await ctx.send("Ya se encuentra registrado")
        else:
            # Si al registrarse debe hacer algo mas, se ve aqui
            save( '.\data\\registered.csv', [ctx.message.author.id, ctx.message.author.name, ])
            await ctx.send("Registro exitoso")

    @_register.error
    async def register_error(self, error, ctx):
        await ctx.send("Error al registrarte, intenta contactar a un moderador.")

    @commands.command(name='test')
    async def test(self, ctx):
        embed = createEmbed("probando", "yeah perdonen")


def setup(client):
    client.add_cog(Character(client))
