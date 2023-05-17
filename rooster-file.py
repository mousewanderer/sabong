# file for character stuff
import random, time
import json

#info chicken file
import infoChicken
from infoChicken import ally_hp, ene_hp
from infoChicken import currentally_hp, currentenemy_hp

def dicechance(crit):
    folder=[]
    crit2= 100 * crit
    crit2=int(crit2)
    norm= 100 -crit2
    norm=int(norm)
    for this in range(0,crit2):
        folder.insert(this, 'critic')
        for num in range(0,norm):
            folder.insert(num,'nothing')
    value= random.choice(folder)
    if value=='critic':
        mult=2
    else:
        mult=1
    return mult
    
        

def ally():
    things=['q','w','r','p','v','u']
    thing=random.choice(things)
    if thing =='q':
        print(Rooster.intro())
        player = Rooster
    elif thing=='w':
        print(FighterR.intro())
        player= FighterR
    elif thing=='r':
        print(GunRooster.intro())
        player= GunRooster
    elif thing=='p':
        print(MilitaryR.intro())
        player= MilitaryR
    elif thing=='v':
        print(assrooster.intro())
        player= assrooster
    elif thing=='u':
        print(kungfu.intro())
        player= kungfu
    return player
        
def enemy():
    things=['q','w','r','p','v','u']
    thing=random.choice(things)
    if thing =='q':
        print(Rooster.intro())
        player = Rooster
    elif thing=='w':
        print(FighterR.intro())
        player= FighterR
    elif thing=='r':
        print(GunRooster.intro())
        player= GunRooster
    elif thing=='p':
        print(MilitaryR.intro())
        player= MilitaryR
    elif thing=='v':
        print(assrooster.intro())
        player= assrooster
    elif thing=='u':
        print(kungfu.intro())
        player= kungfu
    return player


class rooster:
    def __init__(self, name, health, Def, Atk, critical):
        self.name=name
        self.health =health
        self.Atk= Atk
        self.Def= Def
        self.critical =str(critical*100) +'%'
        self.critic= critical
    

    def intro (self):
        value=f'I am a {self.name} \n I have a {self.health} of hp'
        value2=f'\nI have {self.Atk} damage and {self.Def} defense with {self.critical} critical chance'
        result=value + value2
        return result

    def get_hpally(self):
            hp=self.health 
            file= 'allyhp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)

    
    def get_hpeme(self):
            hp=self.health 
            file= 'enehp.json'
            with open(file, 'w') as f:
                json.dump(hp,f)


Rooster=rooster(name='rooster',health=100,Def=3,Atk=5,critical=.05)
FighterR=rooster(name='figheter rooster',health=140,Def=5,Atk=6,critical=0.1)
GunRooster=rooster(name='Rooster with a gun',health=100,Def=3,Atk=20,critical=0.5)
MilitaryR=rooster(name='Military Rooster',health=200,Atk=7,Def=6,critical=.15)
assrooster=rooster(name='Assassin Rooster',health=300,Def=5,Atk=20,critical=.2)
kungfu=rooster(name='Kungfu Rooster',health=250,Def=10,Atk=5,critical=0.3)
shaolinR=rooster(name='Shaolin Rooster',health=300, Def=12, Atk=10, critical=0.35)
knighted=rooster(name='Knight Rooster',health=200, Def=15, Atk=5, critical=0.1)
sniper=rooster(name='Sniper Rooster',health=120, Def=5, Atk=35, critical=0.7)
roosterslay=rooster(name='Rooster Slayer',health=150, Def=10,Atk=10, critical=0.5)

player=''
global turn
global objective


turn= True
objective= True

Ally=ally()
Enemy=enemy()

while objective:

    something=input('Click to continue')
    
    if something==something and turn==True :
         healthally=Ally.get_hpally()
         healthenemy=Enemy.get_hpeme()
         allyhp= ally_hp()
         enemyhp= ene_hp()
         truedamage= Ally.Atk - Enemy.Def
         trueinflict= Enemy.Atk - Ally.Def
         if truedamage <=0:
             truedamage=1
         else: pass
         if trueinflict <=0:
             trueinflict=1
         else: pass
         damage= enemyhp - truedamage
         inflict= allyhp - trueinflict
         print(f'{Ally.name} health is {inflict} and the \n {Enemy.name} is {damage}.')
         current=currentally_hp(value=inflict)
         some=currentenemy_hp(value=damage)
         turn= False
         
    elif something==something and turn==False :
         allyhp=ally_hp()
         enemyhp= ene_hp()
         truedamage= Ally.Atk - Enemy.Def
         trueinlfict= Enemy.Atk - Ally.Def
         allycrit= dicechance(Ally.critic)
         enecrit= dicechance(Enemy.critic)
         if allycrit==2:
             print("ally deals critical damage")
         else:
             pass
            
         if enecrit==2:
            print('enemy deals critical damage')
         else:
             pass
         
         if truedamage <=0:
             truedamage=1
         else: pass
         if trueinflict <=0:
             trueinflict=1
         else: pass
         damage= enemyhp - truedamage *allycrit
         inflict= allyhp - trueinflict *enecrit
         print(f'{Ally.name} health is {inflict} and the \n {Enemy.name} is {damage}.')
         
         current=currentally_hp(value=inflict)
         some=currentenemy_hp(value=damage)
         if damage <=0 and inflict <=0:
             print('it is a draw')
             objective=False
         elif damage <= 0:
             print('you win')
             objective=False
         elif inflict <=0:
             print('you loss')
             objective=False

   
    else: pass
