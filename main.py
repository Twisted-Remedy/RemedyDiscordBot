import hikari
import lightbulb

from utils.config import GetConfig

config = GetConfig()

bot = lightbulb.BotApp(token=config['bot_token'], default_enabled_guilds=(config['guild_ids']))
bot.load_extensions_from("./extensions/")

@bot.listen(hikari.StartedEvent)
async def on_Started(event):
    print('Bot has started!')
    print(f'https://discord.com/api/oauth2/authorize?client_id={bot.cache.get_me().id}&permissions=329728&scope=bot')

bot.run()