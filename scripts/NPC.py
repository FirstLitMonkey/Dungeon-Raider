import pygame, random, math
from scripts.Timer import Timer
from scripts.globals import *
from scripts.textures import Tiles
pygame.init()

def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0] / 2) , int(size[1] / 2))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1], tile_size[0], tile_size[1]))
    faces["west"] = west

    return faces

def MoveNPC(npc):
    if npc.walk__:
        npc.facing = random.choice(("south", "east", "north", "west"))
    
    


class NPC():

    AllNPCs = []

    def __init__(self, name, pos, dialog, sprite, tag, walking, walkstyle, story, corner):
        self.name = name
        self.x = pos[0]*32
        self.y = pos[1]*32
        self.dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()
        self.lastLocation = [0, 0]
        self.tag = tag
        self.walk__ = True
        self.story = story
        self.corner = corner


        #Get NPC faces

        self.facing = "south"
        self.faces = get_faces(sprite)

        # Publish

        NPC.AllNPCs.append(self)


    def Render(self, surface):
        
        self.Timer.Update()
        if self.walking:
            move_speed = 100 * Globals.deltatime

            npc_X = (self.x) / Tiles.Size
            npc_Y = (self.y) / Tiles.Size
            if self.facing =="north":
                if not Tiles.Blocked_At((round(npc_X), math.floor(npc_Y))):
                    self.y -= move_speed
            elif self.facing =="south":
                if not Tiles.Blocked_At((round(npc_X), math.ceil(npc_Y))):
                    self.y += move_speed
            elif self.facing == "east":
                if not Tiles.Blocked_At((math.floor(npc_X), round(npc_Y))):
                    self.x -= move_speed
            elif self.facing == "west":
                if not Tiles.Blocked_At((math.ceil(npc_X), round(npc_Y))):
                    self.x += move_speed
        
                

        # Block Tile Npc is on
        location = [round(self.x / Tiles.Size), round(self.y / Tiles.Size)]
        if self.lastLocation in Tiles.Blocked:
            Tiles.Blocked.remove(self.lastLocation)

        if not location in Tiles.Blocked:
            Tiles.Blocked.append(location)
            self.lastLocation = location
        
        
        surface.blit(self.faces[self.facing], (self.x + Globals.camera_x, self.y + Globals.camera_y))

    
class Male1(NPC):

    def __init__(self, name, pos, dialog = None, tag = 'town', walking=False, walkstyle = '', story = 1.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\male1.png"), tag, walking, walkstyle, story, corner)
class Merc(NPC):


    def __init__(self, name, pos, dialog=None, tag='town', walking=False, walkstyle='', story = 1.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\merc.png"), tag, walking, walkstyle, story, corner)

class OldMan(NPC):

    def __init__(self, name, pos, dialog=None,tag='town', walking=False, walkstyle='', story=1.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\oldman.png"), tag, walking, walkstyle, story, corner)
class Michael(NPC):

    def __init__(self, name, pos, dialog=None, tag='town', walking=False, walkstyle='', story=2.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\michael.png"), tag, walking, walkstyle, story, corner)
class Lady(NPC):

    def __init__(self, name, pos, dialog=None, tag='town', walking=False, walkstyle='', story=1.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\lady.png"), tag, walking, walkstyle, story, corner)
class Guard(NPC):
    def __init__(self, name, pos, dialog=None, tag='southern somerberry', walking=False, walkstyle='', story=1.0, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\guard.png"), tag, walking, walkstyle, story, corner)
class Knok(NPC):
    def __init__(self, name, pos, dialog=None, tag='barrack chamber', walking=False, walkstyle='', story=1, corner=(0, 0, 0, 0)):
        super().__init__(name, pos, dialog, pygame.image.load("graphics\\NPC\\knok.png"), tag, walking, walkstyle, story, corner)
class Dialog:

    def __init__(self, text):
        self.page = 0
        self.text = text  # [("Hi"), ("How are you?")]


#




        
        
        
