#file for information
import json, random

def ally_hp():
    file= 'allyhp.json'
    try:
        with open(file) as f:
            ally=  json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ally

def ene_hp():
    file= 'enehp.json'
    try:
        with open(file) as f:
            ene=  json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ene
        
def currentally_hp(value):
            hp=value 
            file= 'allyhp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)

def currentenemy_hp(value):
            hp=value
            file= 'enehp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)
