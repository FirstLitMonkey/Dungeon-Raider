import pygame, random
from scripts.fight_textures import *
from scripts.meloonatic_gui import *



class skeleton():
    
    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [skeleton_Idle]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'scythe'
        self.damage = damage
        self.dead = False
        self.xp = 4
        self.gold = 15
        self.defence = 1
        self.immunity = []
        self.shake = 'right'


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))


    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False


class merc1():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [Merc1]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'sharp sword'
        self.damage = damage
        self.dead = False
        self.xp = 5
        self.gold = 20
        self.defence = 1
        self.immunity = []
        self.shake = 'right'


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))

    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False

class merc2():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [Merc1]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'sharp sword'
        self.damage = damage
        self.dead = False
        self.xp = 6
        self.gold = 40
        self.defence = 1
        self.immunity = []
        self.shake = 'right'
                        # Ability Name, Damage, Cooldown, Special Effects e.g. increase attack, ignore defence, stun target
        self.special = ["Man of Power", 1.8, 3, "None"]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))



    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class bandit():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [Bandit]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'crowbar'
        self.damage = damage
        self.dead = False
        self.xp = 3
        self.gold = 20
        self.defence = 0
        self.immunity = []
        self.shake = 'right'


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))



    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False


class cyclops():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [Cyclops]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'fists'
        self.damage = damage
        self.dead = False
        self.xp = 8
        self.gold = 35
        self.immunity = ['fireball']
        self.shake = 'right'
        self.defence = 2
                                        # Ability Name, Damage, Cooldown, Special Effects e.g. increase attack, ignore defence, stun target
        self.special = ["Stare", 0, 4, ["inflict stun"]]
        self.ultimate = ["Crushing and Gnawing", 3, 8, ["ignore defence"]]
        

    def draw(self, window):
        if not self.dead:
            self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))

    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False


class grass_viper():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [Viper1, Viper1h]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'Poison Fangs'
        self.damage = damage
        self.dead = False
        self.xp = 5
        self.gold = 15
        self.defence = 0
        self.immunity = ['lightning']
        self.shake = 'right'
        self.special = ["Vicious Bite", 1.5, 3, "inflicts poison"]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
            if self.shake == 'right':
                self.x += 1.5
                self.y += 1.5
                if self.x > 605:
                    self.shake = 'left'
            elif self.shake == 'left':
                self.x -= 1.5
                self.y -= 1.5
                if self.x < 595:
                    self.shake = 'right'
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class rock_golem():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [RockGolem1, RockGolem2]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'Rock Face'
        self.damage = damage
        self.dead = False
        self.xp = 8
        self.gold = 10
        self.defence = 2
        self.immunity = ['lightning', 'fireball']
        self.shake = 'right'


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False



class bat():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [bat_img]
        self.custome = 0
        self.x = 600
        self.y = 40
        self.weapon = 'claws'
        self.damage = damage
        self.dead = False
        self.xp = 2
        self.gold = 5
        self.defence = 0
        self.immunity = []
        self.shake = 'right'


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
            if self.shake == 'right':
                self.x += 1.5
                self.y += 1.5
                if self.x > 605:
                    self.shake = 'left'
            elif self.shake == 'left':
                self.x -= 1.5
                self.y -= 1.5
                if self.x < 595:
                    self.shake = 'right'



    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False


class zombie():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [zombie_img, zombie_hurt]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'undead hands'
        self.damage = damage
        self.dead = False
        self.xp = 8
        self.gold = 10
        self.immunity = []
        self.defence = 1
        self.shake = 'right'
                        # Ability Name, Damage, Cooldown, Special Effects e.g. increase attack, ignore defence, stun target
        self.special = ["Walk of the Undead", 2, 5, ["ignore defence","health steal"]]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
            
class michael():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [zombie_img, zombie_hurt]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'Family Sword'
        self.damage = damage
        self.dead = False
        self.xp = 20
        self.gold = 30
        self.immunity = ['heavy sword strike', 'drain']
        self.defence = 4
        self.shake = 'right'
                        # Ability Name, Damage, Cooldown, Special Effects e.g. increase attack, ignore defence, stun target
        self.special = ["Fleeting Blow", 2, 4, ["ignore defence"]]
        self.ultimate = ["Family's Honour", 1, 6, ["remove 100 mag", "increase attack", "health steal"]]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class gideon():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.base_health = maxhealth
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [zombie_img, zombie_hurt]
        self.custome = 0
        self.x = 600
        self.y = 10
        self.weapon = 'Family Sword'
        self.damage = damage
        self.dead = False
        self.xp = 20
        self.gold = 30
        self.immunity = ['heavy sword strike', 'drain']
        self.defence = 1
        self.shake = 'right'
                        # Ability Name, Damage, Cooldown, Special Effects e.g. increase attack, ignore defence, stun target
        self.special = ["Hidden Dagger", 1.8, 3, ["ignore defence"]]
        self.ultimate = ["Dual Sided Blade", 2.5, 8, ["inflict stun", "health steal"]]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False

class magicalcannon():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.maxhealth = maxhealth
        self.base_health = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [mag_cannon, mag_cannon_hurt]
        self.custome = 0
        self.x = 520
        self.y = -50
        self.weapon = 'cannon blast'
        self.defence = 0
        self.damage = damage
        self.dead = False
        self.xp = 8
        self.gold = 12
        self.immunity = []
        self.shake = 'right'
        self.special = ["Supercharged Blast", 1.5, 3, ["None"]]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class somerberry_guard():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.maxhealth = maxhealth
        self.base_health = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [somer_guard]
        self.custome = 0
        self.x = 600
        self.y = 0
        self.weapon = 'cannon blast'
        self.defence = 2
        self.damage = damage
        self.dead = False
        self.xp = 5
        self.gold = 25
        self.immunity = []
        self.special = ["Gut Drenching Blow", 2.5, 3, ["ignore defence"]]


    def draw(self, window):
        if not self.dead:
            self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class somerberry_torturer():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.maxhealth = maxhealth
        self.base_health = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [somer_guard]
        self.custome = 0
        self.x = 600
        self.y = 0
        self.weapon = 'torturers knife'
        self.defence = 1
        self.damage = damage
        self.dead = False
        self.xp = 12
        self.gold = 35
        self.immunity = ['heavy sword strike']
        self.special = ["Drain Life", 2, 4, ["ignore defence", 'health steal']]
        self.ultimate = ["Cannibilism", 3, 5, ["health steal"]]


    def draw(self, window):
        if not self.dead:
            self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False


class commander_knok():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.maxhealth = maxhealth
        self.base_health = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [knok_battle]
        self.custome = 0
        self.x = 600
        self.y = 0
        self.weapon = 'Steel Greatsword'
        self.defence = 1
        self.damage = damage
        self.dead = False
        self.xp = 12
        self.gold = 100
        self.immunity = []
        self.special = ["Morale", 0.8, 3, ["recover 10"]]
        self.ultimate = ["Death Be Upon You", 2, 4, ["remove 50 mag", "ignore defence"]]


    def draw(self, window):
        if not self.dead:
            self.custome = 0
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
class orc():

    def __init__(self, name, maxhealth, damage):
        self.name = name
        self.maxhealth = maxhealth
        self.base_health = maxhealth
        self.health = maxhealth
        self.base_damage = damage
        self.idle = [orc_image, orc_hurt]
        self.custome = 0
        self.x = 600
        self.y = 0
        self.weapon = 'Orc Axe'
        self.defence = 1
        self.damage = damage
        self.dead = False
        self.xp = 7
        self.gold = 10
        self.immunity = []
        self.special = ["Orc Blood Fury", 2, 4, ["ignore defence"]]


    def draw(self, window):
        if not self.dead:
            if self.health >= self.maxhealth/2:
                self.custome = 0
            else:
                self.custome = 1
            window.blit(self.idle[self.custome], (self.x, self.y))
            win_health = (str(self.health) + "/" + str(self.maxhealth))
            window.blit(Font.Default.render(win_health, True, Color.White), (700, 0))
    def Dead_(self):
        if self.health <= 0:
            self.dead = True
            self.health = self.maxhealth
        else:
            self.dead = False
magicalCannonIG = magicalcannon("Magical Cannon", 35, 15)            
Merc1IG = merc1("Mercenary", maxhealth = 140, damage = 8)
skeletonIG = skeleton(name = "Skeleton", maxhealth = 120, damage = 5)
Merc2IG = merc2("Mercenary Leader", maxhealth = 250, damage = 12)
banditIG = bandit("Bandit", maxhealth = 100, damage = 8)
cyclopsIG = cyclops("Cyclops", maxhealth = 220, damage = 13)
grass_viperIG = grass_viper("Grass Viper", maxhealth=60, damage=17)
rock_golemIG = rock_golem("Baby Rock Golem", maxhealth=180, damage=3)
batIG = bat("Flying Bat", maxhealth=40, damage=4)
zombieIG = zombie("Zombie", maxhealth=90, damage=8)
michaelIG = michael("Michael, House Leader", maxhealth=345, damage=9)
gideonIG = gideon("Gideon, Thief Commander", maxhealth=220, damage=19)
somerberryguardIG = somerberry_guard("Corrupt Guard", maxhealth=125, damage=9)
somer_torturerIG = somerberry_torturer("Torturer", maxhealth=250, damage=4)
knokIG = commander_knok("Commander Knok", maxhealth=330, damage=8)
orcIG = orc("Orc Assaulter", maxhealth=130, damage=10)

class Enemystats():
    enemies = [skeletonIG, Merc1IG, Merc2IG,
               banditIG, cyclopsIG, grass_viperIG,
               rock_golemIG, batIG, zombieIG,
               michaelIG, gideonIG, magicalCannonIG,
               somerberryguardIG, somer_torturerIG,
               knokIG, orcIG,
               ]

