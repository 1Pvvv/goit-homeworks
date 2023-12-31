from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read("../config/config.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
domain = config.get("DB", "domain")

# connect to cluster on AtlasDB with connection string
connect(
    host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority",
    ssl=True,
)
