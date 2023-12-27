import lightbulb

from utils.RiotAPI.league import League
from utils.config import GetConfig
from utils.database import Database
db = Database()

league_api = League(GetConfig()['riot_api_key'])
plugin = lightbulb.Plugin("LeagueOfLegends")

@plugin.command()
@lightbulb.option("region", "Region of the account", choices=['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru'], required=False)
@lightbulb.option("name", "Name of the account", required=False)
@lightbulb.command("top-masteries", "Get masteries of your top 10 champions", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def TopMasteries(ctx: lightbulb.SlashContext) -> None:
    username = ctx.options.name
    region = ctx.options.region

    try:
        if not username or not region:
            _, username, region = db.GetUserByID(ctx.author.id)
    except TypeError:
        return await ctx.respond('**Error getting details!** (/update-details)')

    try:
        data = league_api.MasteriesByName(region, username)[:10]
        message = f"**__{username} Top 10 Masteries__**  <:mastery:1188997591308980274>\n"
        for i in data:
            message = f"{message}> {league_api.IDToName(i['championId'])}: {i['championPoints']}\n"
        await ctx.respond("Success!")
        await ctx.bot.rest.create_message(ctx.channel_id, message)
    except KeyError:
        await ctx.respond(f'Problem finding data. Please check "/update-details"!')

@plugin.command()
@lightbulb.option("region", "Region of the account", choices=['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru'], required=False)
@lightbulb.option("name", "Name of the account", required=False)
@lightbulb.option("champion", "Name of the champion")
@lightbulb.command("champion-mastery", "Get mastery of a specific champion", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def ChampionMastery(ctx: lightbulb.SlashContext) -> None:
    username = ctx.options.name
    region = ctx.options.region

    try:
        if not username or not region:
            _, username, region = db.GetUserByID(ctx.author.id)
    except TypeError:
        return await ctx.respond('**Error getting details!** (/update-details)')

    try:
        data = league_api.MasteriesByNameByChamp(region, username, ctx.options.champion)
        message = f"**__{username}'s {ctx.options.champion.title()} Mastery__**  <:mastery:1188997591308980274>\n> Level: {data['championLevel']}\n> Points: {data['championPoints']}"
        await ctx.respond("Success!")
        await ctx.bot.rest.create_message(ctx.channel_id, message)
    except KeyError:
        await ctx.respond(f'Problem finding data. Please check "/update-details"!')

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)