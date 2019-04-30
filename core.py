import cfscrape
import os
import subprocess
import shutil
import json
import time
import sys
from bs4 import BeautifulSoup as parser
from requests.exceptions import ConnectionError, ConnectTimeout

BASE_PATH = "{}/GLR_Manager".format(os.getenv("LOCALAPPDATA"))
PROFILES_PATH = "{}/Profiles".format(BASE_PATH)
CURRENT_VERSION = "1.3.1"

class Game:
    def __init__(self, id, name, type):
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
    def __init__(self,name = 'default',games = []):
        self.name = name
        self.games = games

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
                try:
                    data = json.load(file)
                    self.register_profile(Profile.from_JSON(data))
                except json.JSONDecodeError:
                    file.close()
                    os.remove("{}/{}".format(PROFILES_PATH,filename))

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
    def __init__(self, steam_path = "", no_hook = True, compatibility_mode = False, version = CURRENT_VERSION, last_profile = "default", check_update = True):
        self.steam_path = steam_path
        self.no_hook = no_hook
        self.compatibility_mode = compatibility_mode
        self.version = version
        self.last_profile = last_profile
        self.check_update = check_update

    def export_config(self):
        with open("{}/config.json".format(BASE_PATH), "w") as outfile:
            json.dump(vars(self),outfile,indent=4)

    #  Mass set attributes and export the config
    def set_attributes(self, dict_):
        for name, value in dict_.items():
            if name in vars(self).keys():
                setattr(self, name, value)
            else:
                print("Attribute {0} don't exist.".format(name))
        
        self.export_config()

    @staticmethod
    def from_JSON(data):
        config = Config()
        for key, value in data.items():
            if key in vars(config).keys():
                setattr(config, key, value)
            
        return config

    @staticmethod
    def load_config():
        if not os.path.isfile("{}/config.json".format(BASE_PATH)):
            if not os.path.exists(BASE_PATH):
                os.makedirs(BASE_PATH)
            
            config = Config()
            config.export_config()
            return config
        else:
            with open("{}/config.json".format(BASE_PATH), "r") as file:
                data = json.load(file)
                config = Config.from_JSON(data)
                config.version = CURRENT_VERSION
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
    try:
        result = scraper.get("https://steamdb.info/search/?a=app&q={0}&type=-1&category=0".format(queryfy(input_)))
    except (ConnectionError, ConnectTimeout) as err:
        return err
    
    html = result.content
    return parseGames(html)

def runUpdater():
    if "-NoUpdate" not in sys.argv and config.check_update:
        subprocess.run("GLR Updater.exe")
    
    # Post update measure
    if "-PostUpdate" in sys.argv:
        for fl in os.listdir("./"):
            if fl.startswith("new_"):
                real_name = fl.replace("new_","")
                os.remove(real_name)
                os.rename(fl, real_name)