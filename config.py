# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28243586")
    API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7273354975:AAGrkcgUdrdUvitwdger1XfA8vtHcmLGIuE") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5340652544').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://telegra.ph/file/a87e65f65e37aafd745df.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://smkbotz:YPYAFx0wxDqTiyfE@cluster0.auq84bb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002235766670"))
    
    UPDATES_CHANNEL = "-1002235661888"


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
