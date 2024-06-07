#file for information
import json

# Function to get ally health
def ally_hp():
    file = 'allyhp.json'
    try:
        with open(file) as f:
            ally = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ally

# Function to get enemy health
def ene_hp():
    file = 'enehp.json'
    try:
        with open(file) as f:
            ene = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return ene

# Function to set current ally health
def currentally_hp(value):
    hp = value
    file = 'allyhp.json'
    with open(file, 'w') as f:
        json.dump(hp, f)

# Function to set current enemy health
def currentenemy_hp(value):
    hp = value
    file = 'enehp.json'
    with open(file, 'w') as f:
        json.dump(hp, f)



def balance():
    file= 'balance.json'
    try:
        with open(file) as f:
            ally=  json.load(f)
    except FileNotFoundError:
        return 0
    else:
        return ally

def getbalance(value):
    hp=value
    file= 'balance.json'
    with open(file, 'w') as f:
        json.dump(hp,f)
