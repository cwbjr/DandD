# DandD
Dungeons and Dragons Dungeon Master API
162.243.13.105

https://www.youtube.com/watch?v=L8p8ceKqvVQ

### TL;DR: A tool for a Dungeon Master (DM) to record all data pertaining to the the game. Other players can also look at it and see information pertaining to their own character.

##### Understood:  
  Databases (mongoDB) to store each account's information (games, characters, items, monsters, story progress)  
  Forms to grab the information entered by the DM  
  CSS to prettify  
  Javascript to animate certain interactions (selecting an icon, drag and drop, etc.)  

##### Not understood but probably not that bad:  
  flask-socketio to constantly update the information  

##### Wat:  
  Map maker for the DM to create his dungeon.  
  Map of the dungeon that is interactive - can place characters on squares and move things around.  

##### Player Traits:  

  Strength (*Str*)  
  Dexterity (*Dex*)  
  Constitution (*Con*)  
  Intelligence (*Int*)  
  Wisdom (*Wis*)  
  Charisma (*Cha*)  

##### Skills:  
  Physical:  
  Magical:  
  Passive:  


##### Items:  
  Weapons:  
  Consumables:  
  Armor:  
  Trinkets:  
  Quest Items:  

##### Races:  
  Aberrations  
  Beasts  
  Celestials  
  Constructs  
  Dragons  
  Elementals  
  Fey  
  Fiends  
  Giants  
  Humanoids  
  Monstrosities  
  Oozes  
  Plants  
  Undead  

##### Home Page:  
  A brief description of the page and how to use it.

##### Register and Login/Logout:
  Save your games so you can abstain with the pen and paper! No more hassle!

##### Games Page:  
  A list of all games you currently manage.

##### Build and Run!:  
  req - pymongo, flask-socketio, flask, eventlet, gunicorn, nginx
  to simply run this just python app.py in the home directory of this folder
