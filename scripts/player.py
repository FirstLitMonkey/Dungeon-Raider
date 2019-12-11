import pygame
from scripts.NPC import*
pygame.init()

class Player:
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        sprite = pygame.image.load("graphics\\character\\player.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]


        #Get Player Face

        self.faces = get_faces(sprite)


    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)
        
        
        
