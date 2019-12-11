from scripts.fight_textures import *
from scripts.fight_club import *
from scripts.Ultra_Color import *
import pygame, time
clock = pygame.time.Clock()

class player():
    def __init__(self, height, width):
        self.name = "Player"
        self.x = 50
        self.y = 10
        self.height = height
        self.width = width
        self.vel = 10
        self.moving = True
        self.walkcount = 0
        self.idle = True
        self.runninganime = False
        self.attack1 = False
        self.hattack = False
        self.attackcount = 0
        self.ownedweapons = ["Rusty Sword"]
        self.curweap = "Rusty Sword"
        self.dead = False
        self.fireballatt = False


        
    def draw(self, win):
        if Globals.weapons[Globals.playerdata['curweap'].lower()][2] == "sword": sets, setID = att1ProR, 1
        elif Globals.weapons[Globals.playerdata['curweap'].lower()][2] == "spear": sets, setID = att1Spear, 2
        elif Globals.weapons[Globals.playerdata['curweap'].lower()][2] == "axe": sets, setID = att1Axe, 3
        if self.walkcount + 1 >= 24:
            self.walkcount = 0
        if self.idle == True and self.attack1 == True:
            if Globals.anime_turn != 0:
                self.x = 490
                win.blit(sets[self.attackcount // 3], (self.x, self.y))
                self.attackcount += 1
                if self.attackcount + 1 >= 18:
                    Globals.anime_turn -= 1
                    self.attackcount = 0
                    self.runninganime = False
                    self.walkcount = 0
            else:
                self.attack1 = False
                self.attackcount = 0
                self.runninganime = False
                self.walkcount = 0
                win.blit(Idle[setID], (self.x, self.y))
                self.x = 50
                self.y = 10
                    
        elif self.idle == True and self.hattack == True:
            self.x = 490
            win.blit(attHProR[self.attackcount // 3], (self.x, self.y))
            self.attackcount += 1
            if self.attackcount + 1 >= 39:
                self.hattack = False
                self.attackcount = 0
                self.runninganime = False
                self.walkcount = 0
                win.blit(Idle[setID], (self.x, self.y))
                self.x = 50
                self.y = 10
        elif self.idle == True and self.fireballatt == True:
            self.x = 50
            win.blit(attFire[self.attackcount // 4], (480, 0))
            win.blit(Idle[0], (self.x, self.y))
            self.attackcount += 1
            if self.attackcount + 1 >= 12:
                self.fireballatt = False
                self.attackcount = 0
                self.walkcount = 0
                
                    
            
                
        else:
            win.blit(Idle[setID], (self.x, self.y))
            self.attackcount = 0
        win_health = ('Health: ' + str(Globals.playerdata['health']) + "/" + str(Globals.playerdata['maxhealth']))
        win_magic = ('Magic: ' + str(Globals.playerdata['magic']) + '/' + str(Globals.playerdata['maxmagic']))
        win_weapon = ('Equiped Weapon: ' + str(Globals.playerdata['curweap']))
        win.blit(Font.Default.render(win_health, True, Color.Black), (400, 220))
        win.blit(Font.Default.render(win_magic, True, Color.Black), (400, 250))
        win.blit(Font.Default.render(win_weapon, True, Color.Black), (300, 280))

           


                
            

