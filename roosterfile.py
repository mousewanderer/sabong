# file for character stuff
import random, time, json, pygame

#info chicken file
import infoChicken
from infoChicken import ally_hp, ene_hp, currentally_hp, currentenemy_hp

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
    

def select():
    classes = {
        'q': Normal,
        'w': FighterR,
        'r': GunRooster,
        'p': MilitaryR,
        'v': assrooster,
        'u': kungfu,
        'h': shaolinR,
        'K': knighted,
        'jg': sniper,
        'gy': roosterslay
    }
    thing = random.choice(list(classes.keys()))
    player_class = classes[thing]
    print(player_class.intro())
    return player_class


class rooster:
    def __init__(self, x, y, name, health, Def, Atk, critical):
        self.name = name
        self.health = health
        self.Atk = Atk
        self.Def = Def
        self.critical = str(critical * 100) + '%'
        self.critic = critical
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0: idle, 1: attack, 2: hurt, 3: dead
        self.update_time = pygame.time.get_ticks()
        
        # Load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        # Load attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        # Load hurt images
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'img/{self.name}/Hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        # Load death images
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'img/{self.name}/Death/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # Handle animation
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            # If the animation has run out then reset back to the start
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def idle(self):
        # Set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        # Deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.Atk + rand
        target.health -= damage
        # Run enemy hurt animation
        target.hurt()
        # Check if target has died
        if target.health < 1:
            target.health = 0
            target.alive = False
            target.death()
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        # Set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # Set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # Set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.health = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

    def intro(self):
        value = f'I am a {self.name} \n I have a {self.health} of hp'
        value2 = f'\nI have {self.Atk} damage and {self.Def} defense with {self.critical} critical chance'
        result = value + value2
        return result

    def get_hpally(self):
        hp = self.health
        file = 'allyhp.json'
        with open(file, 'w') as f:
            json.dump(hp, f)

    def get_hpeme(self):
        hp = self.health
        file = 'enehp.json'
        with open(file, 'w') as f:
            json.dump(hp, f)



Normal=rooster(name='rooster',health=100,Def=3,Atk=5,critical=.05)

FighterR=rooster(name='fighter rooster',health=140,Def=5,Atk=6,critical=0.1)

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
#ally value
ally_value_x = 200
ally_value_y= 260

Ally=select()

if ally 

#enemy value
enemy_value_x = 550
enemy_value_y = 270

Enemy=select()
"""
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
"""
