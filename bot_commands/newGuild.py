from discord.ext import commands
from functions.yeah import save


class NewGuild(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print("Raid bot se unio a al servidor - ", guild.name, " - id : ", guild.id)
        await guild.create_role(name="Raider",colour=discord.Colour.blue())

    @commands.Cog.listener()
    async def on_guild_role_create(self,rol):
        save('.\data\guilds_id.csv',[rol.guild.id, rol.guild.name,rol.id])



def setup(client):
    client.add_cog(NewGuild(client))
