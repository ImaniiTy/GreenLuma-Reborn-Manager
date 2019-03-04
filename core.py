import cfscrape
import os
import shutil
import json
import time
from bs4 import BeautifulSoup as parser
from concurrent.futures.thread import ThreadPoolExecutor

BASE_PATH = "{}/GLR_Manager".format(os.getenv("LOCALAPPDATA"))
PROFILES_PATH = "{}/Profiles".format(BASE_PATH)
CURRENT_VERSION = "1.2.0"

class Game:
    def __init__(self,id,name,type):
        self.id = id
        self.name = name
        self.type = type

    def to_JSON(self):
        return {"id": self.id, "name": self.name, "type": self.type}

    def to_string(self):
        return "ID: {0}\nName: {1}\nType: {2}\n".format(self.id,self.name,self.type)

    def to_list(self):
        return [self.id, self.name, self.type]

    def __eq__(self, value):
        return self.id == value.id and self.name == value.name and self.type == value.type

    @staticmethod
    def from_JSON(data):
        return Game(data["id"],data["name"],data["type"])
    
    @staticmethod
    def from_table_list(list):
        games = []
        for i in range(int(len(list)/3)):
            games.append(Game(list[i * 3].text(), list[i * 3 + 1].text(), list[i * 3 + 2].text()))

        return games

class Profile:
    def __init__(self,name = 'default',games = None):
        self.name = name
        self.games = [] if games is None else games

    def add_game(self,game):
        self.games.append(game)

    def remove_game(self,game):
        if type(game) is Game:
            self.games.remove(game)
        else:
            for game_ in self.games:
                if game_.name == game: self.games.remove(game_)
    
    def export_profile(self,path = PROFILES_PATH):
        data = {"name": self.name, "games": [game.to_JSON() for game in self.games]}
        with open("{}/{}.json".format(path, self.name), "w") as outfile:
            json.dump(data,outfile,indent=4)

    def __eq__(self, value):
        return self.name == value.name

    @staticmethod
    def from_JSON(data):
        return Profile(data["name"], [Game.from_JSON(game) for game in data["games"]])

class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.load_profiles()

    def load_profiles(self):
        if not os.path.exists(PROFILES_PATH):
            os.makedirs(PROFILES_PATH)
            self.create_profile("default")
        elif len(os.listdir(PROFILES_PATH)) == 0:
            self.create_profile("default")

        for filename in os.listdir(PROFILES_PATH):
            with open("{}/{}".format(PROFILES_PATH,filename), "r") as file:
                data = json.load(file)
                self.register_profile(Profile.from_JSON(data))

    def register_profile(self, profile):
        self.profiles[profile.name] = profile

    def create_profile(self, name, games = None):
        if name is "":
            return
        
        self.register_profile(Profile(name,games))
        self.profiles[name].export_profile(PROFILES_PATH)

    def remove_profile(self, profile_name):
        self.profiles.pop(profile_name)
        os.remove("{}/{}.json".format(PROFILES_PATH,profile_name))

class Config:
    def __init__(self, steam_path = "AppList", is_path_setup = False, no_hook = True, no_update = False, version = CURRENT_VERSION, last_profile = "default"):
        self.steam_path = steam_path
        self.is_path_setup = is_path_setup
        self.no_hook = no_hook
        self.no_update = no_update
        self.version = version
        self.last_profile = last_profile

    def export_config(self):
        data = {"steam_path": self.steam_path, "is_path_setup": self.is_path_setup, "no_hook": self.no_hook, "no_update": self.no_update, "version": self.version, "last_profile": self.last_profile}
        with open("{}/config.json".format(BASE_PATH), "w") as outfile:
            json.dump(data,outfile,indent=4)

    @staticmethod
    def from_JSON(data):
        keys = data.keys()
        config = Config()
        return Config(data["steam_path"] if "steam_path" in keys else config.steam_path, 
                      data["is_path_setup"] if "is_path_setup" in keys else config.is_path_setup, 
                      data["no_hook"] if "no_hook" in keys else config.no_hook, 
                      data["no_update"] if "no_update" in keys else config.no_update, 
                      data["version"] if "version" in keys else config.version,
                      data["last_profile"] if "last_profile" in keys else config.last_profile)

    @staticmethod
    def load_config():
        if not os.path.isfile("{}/config.json".format(BASE_PATH)):
            config = Config()
            if not os.path.exists(BASE_PATH):
                os.makedirs(BASE_PATH)
            
            config.export_config()
            return config
        else:
            with open("{}/config.json".format(BASE_PATH), "r") as file:
                data = json.load(file)
                config = Config.from_JSON(data)
                config.export_config()
                return config


#-------------
config = Config.load_config()

def createFiles(games):
    if not os.path.exists("{}/AppList".format(config.steam_path)):
        os.makedirs("{}/AppList".format(config.steam_path))
    else:
        shutil.rmtree("{}/AppList".format(config.steam_path))
        time.sleep(0.5)
        os.makedirs("{}/AppList".format(config.steam_path))

    for i in range(len(games)):
        with open("{}/AppList/{}.txt".format(config.steam_path,i),"w") as file:
            file.write(games[i].id)

def parseGames(html):
    p = parser(html, 'html.parser')

    rows = p.find_all("tr", class_= "app")

    games = []
    for row in rows:
        data = row("td")
        if(data[1].get_text() != "Unknown"):
            game = Game(data[0].get_text(),data[2].get_text(),data[1].get_text())
            #print(game.to_string())
            games.append(game)

    return games


def queryfy(input_):
    arr = input_.split()
    result = arr.pop(0)
    for word in arr:
        result = result + "+" + word
    print(result)
    return result

def queryGames(input_):
    scraper = cfscrape.create_scraper()
    html = scraper.get("https://steamdb.info/search/?a=app&q={0}&type=-1&category=0".format(queryfy(input_))).content

    return parseGames(html)