#file for information
import json, random
#Function of the health to declare to import it to the user
def ally_hp():
    file= 'allyhp.json'
    try:
        with open(file) as f:
            ally=  json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ally
#Function of the health to declare to import it to the Enemy AI
def ene_hp():
    file= 'enehp.json'
    try:
        with open(file) as f:
            ene=  json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ene
 # states the curretn health of the user       
def currentally_hp(value):
            hp=value 
            file= 'allyhp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)
 # states the curretn health of the enmey AI
def currentenemy_hp(value):
            hp=value
            file= 'enehp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)
