if bool(os.environ.get("ENV", False)):
    from assistant.sample_config import Config
else:
    from assistant.config import Config


# TODO: is there a better way?
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
