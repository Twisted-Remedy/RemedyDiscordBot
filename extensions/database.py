import lightbulb

from utils.database import Database
db = Database()

plugin = lightbulb.Plugin("Database")

@plugin.command()
@lightbulb.option("region", "Region of the account", choices=['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru'], required=True)
@lightbulb.option("name", "Name of the account", required=True)
@lightbulb.command("update-details", "Save your username and region to save time in commands later", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def UpdateDetails(ctx: lightbulb.SlashContext) -> None:
    try:
        exists = db.GetUserByID(ctx.author.id)
        if exists:
            db.UpdateDetails(ctx.author.id, ctx.options.name, ctx.options.region)
        else:
            db.InsertUser(ctx.author.id, ctx.options.name, ctx.options.region)
        await ctx.respond("Successful!")
    except:
        await ctx.respond("Unsuccessful.")

@plugin.command()
@lightbulb.command("remove-details", "Remove your details from the database", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def RemoveDetails(ctx: lightbulb.SlashContext) -> None:
    try:
        exists = db.GetUserByID(ctx.author.id)
        if exists:
            db.RemoveUser(ctx.author.id)
            await ctx.respond("Successful!")
        else:
            await ctx.respond("User already doesn't exist")
    except:
        await ctx.respond("Unsuccessful.")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)