import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "1496823926").split()))

API_ID = int(os.getenv("API_ID", "24072173"))

API_HASH = os.getenv("API_HASH", "c29528643f49ef1913999453f09f70d6")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7423163316:AAHcY7xOFv-XIVx317TYDhfyMcwjdgzkAoA")

OWNER_ID = int(os.getenv("OWNER_ID", "1496823926"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Indiaindiahottt:Indiaindiahottt@indiaindiahottt.o3ihegl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))

