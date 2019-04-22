# GreenLuma Reborn Manager
An app to manage the Steam unlocker "GreenLuma Reborn" AppList folder

## What is [GreenLuma Reborn](https://cs.rin.ru/forum/viewtopic.php?f=29&t=80797) ?
GreenLuma Reborn (GLR) is a Steam unlocker made by Steam006 that is used to obtain games from family shared libraries and DLC for games. There's much more to it, though.

The full list of features provided by Steam006.

![alt text](https://i.imgur.com/D18pz0f.png)

## Can I get banned for using GreenLuma Reborn ?
There will always be a risk when using GLR. If you're willing to take that risk, go right on ahead. If not, then don't bother. Especially when that risk means the status of your Steam account.

As expected, there are some games that blacklist GLR and using it will result in receiving a game ban. Refer to [this page](https://github.com/linkthehylian/GreenLuma-Reborn-App/wiki/Blacklist) if you want to check what games NOT to play.

Please keep in mind. Like CreamAPI, GreenLuma Reborn **does not** work for every game.

Also, keep in mind that not **every game** is available to play through Steam family sharing.

I **highly advise** you to follow the "Legit stealth mode" installation instructions if you do plan on using GreenLuma Reborn.

![alt text](https://i.imgur.com/XSjQFn9.png)

#### Credits to [@linkthehylian](https://github.com/linkthehylian) for this brief explanation

## Latest release: **[GreenLuma Reborn Manager v1.2.4](https://github.com/ImaniiTy/GreenLuma-Reborn-Manager/releases)**

## Features
  * Easily manage profiles for various games(good to circumvent the 160 id limit)
    * Add/Remove 1 or more games at once
    * Add/Remove profiles
  * Search for any game you want to add direct from the app
    * Search results are directly from SteamDB
    * Sort the results from Type(DLC, Game, etc..) or Name
  * Generate the Applist, close steam and run the GLR in one click
    * You can choose any GLR parameters before launch
    * It will detect whether the steam is open or not and close it if necessary
  * All the profiles info are in JSON files so you can easily share with anyone
    * The profiles are saved on: C:\Users\YOUR_USER\AppData\Local\GLR_Manager\Profiles

![alt text](https://i.imgur.com/F4dvAjV.png)
  
## What's the difference between your app and [GreenLuma Reborn App](https://github.com/linkthehylian/GreenLuma-Reborn-App)?
  Well the main difference, like i said on the topic above, is that on my app you can search the game you want to add directly from the program and my version is more focused on the management of the folder (and if you're like me who don't like having all the games unlocked at the same time the profile system can help you alot)
  
## Future Plans
* **Work on the UI(I still suck at UI design)**
* **Add varius QoL stuff(Would love some ideas for this)**
* Add a way to load previous games on your AppList folder
* ~~Add a way to launch GLR direct from the app~~
* Add some user input validation
  
## Built With
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) - The GUI framework
* [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) - Used to make the standalone executable

## Authors
[**ImaniiTy**](https://github.com/ImaniiTy):

![alt text](https://i.imgur.com/zmS7oBs.gif)
