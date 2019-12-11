from scripts.globals import *
from scripts.Ultra_Color import *
import pygame, math, pickle


circle = pygame.image.load("graphics\\gui\\circle.png")
superfont = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 60)
supererfont = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 80)
superfont1 = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 36)
clock = pygame.time.Clock()
window_width, window_height = 800, 600
window_title = "Dungeon Raider Animated"
pygame.display.set_caption(window_title)
window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
is_running = True
Globals.idea_list = ["action1", "cancel", "pause", "run"]
locked_up = False
banned = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_RETURN, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

class options_convert:
    def convertable(converted):
        if converted == 304:
            return "shift"
        elif converted == 27:
            return "esc"
        elif converted == 301:
            return "caps"
        elif converted == 9:
            return "tab"
        elif converted == 13:
            return "enter"
        elif converted == 303:
            return "shift"
        elif converted == 306:
            return "lctrl"
        elif converted == 307:
            return "ratl"
        elif converted == 308:
            return "latl"
        elif converted == 32:
            return "space"
        elif converted == 273:
            return "up"
        elif converted == 274:
            return "down"
        elif converted == 275:
            return "right"
        elif converted == 276:
            return "left"
        elif converted == 8:
            return "bspce"
        else:
            return str(chr(converted))
    
while is_running:
    window.fill((0, 0, 0))
    action1 = options_convert.convertable(Globals.actions['action1'])
    cancel = options_convert.convertable(Globals.actions['cancel'])
    pause = options_convert.convertable(Globals.actions['pause'])
    run = options_convert.convertable(Globals.actions['run'])
                                          
    if Globals.idea_list[Globals.current_list] == 'action1':
        window.blit(pygame.transform.scale(circle, (100, 57)), (466, 105))
        window.blit(superfont1.render(action1, True, Color.DarkGoldenrod), (500 - (len(action1) * 5), 100))
        window.blit(superfont1.render(cancel, True, Color.White), (500 - (len(cancel) * 5), 150))
        window.blit(superfont1.render(pause, True, Color.White), (500 - (len(pause) * 5), 200))
        window.blit(superfont1.render(run, True, Color.White), (500 - (len(run) * 5), 250))
    elif Globals.idea_list[Globals.current_list] == 'cancel':
        window.blit(pygame.transform.scale(circle, (100, 57)), (466, 155))
        window.blit(superfont1.render(action1, True, Color.White), (500 - (len(action1) * 5), 100))
        window.blit(superfont1.render(cancel, True, Color.DarkGoldenrod), (500 - (len(cancel) * 5), 150))
        window.blit(superfont1.render(pause, True, Color.White), (500 - (len(pause) * 5), 200))
        window.blit(superfont1.render(run, True, Color.White), (500 - (len(run) * 5), 250))
    elif Globals.idea_list[Globals.current_list] == 'pause':
        window.blit(pygame.transform.scale(circle, (100, 57)), (466, 205))
        window.blit(superfont1.render(action1, True, Color.White), (500 - (len(action1) * 5), 100))
        window.blit(superfont1.render(cancel, True, Color.White), (500 - (len(cancel) * 5), 150))
        window.blit(superfont1.render(pause, True, Color.DarkGoldenrod), (500 - (len(pause) * 5), 200))
        window.blit(superfont1.render(run, True, Color.White), (500 - (len(run) * 5), 250))
    elif Globals.idea_list[Globals.current_list] == 'run':
        window.blit(pygame.transform.scale(circle, (100, 57)), (466, 255))
        window.blit(superfont1.render(action1, True, Color.White), (500 - (len(action1) * 5), 100))
        window.blit(superfont1.render(cancel, True, Color.White), (500 - (len(cancel) * 5), 150))
        window.blit(superfont1.render(pause, True, Color.White), (500 - (len(pause) * 5), 200))
        window.blit(superfont1.render(run, True, Color.DarkGoldenrod), (500 - (len(run) * 5), 250))        
    window.blit(superfont.render(str("ACTION"), True, Color.White), (200, 100))
    window.blit(superfont.render(str("CANCEL"), True, Color.White), (200, 150))
    window.blit(superfont.render(str("PAUSE"), True, Color.White), (200, 200))
    window.blit(superfont.render(str("RUN"), True, Color.White), (200, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if locked_up == True:
                if not event.key in banned:
                    if event.key == Globals.actions['cancel']:
                        locked_up = False
                    if not event.key in Globals.actions.values():
                        Globals.actions[Globals.idea_list[Globals.current_list]] = event.key
                        locked_up = False
                        circle = pygame.image.load("graphics\\gui\\circle.png")

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if not locked_up:
                    Globals.current_list -= 1
                    if Globals.current_list <= -1:
                        Globals.current_list = len(Globals.idea_list) - 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if not locked_up:
                    Globals.current_list += 1
                    if Globals.current_list >= len(Globals.idea_list):
                        Globals.current_list = 0
            elif event.key == Globals.actions['action1'] and not locked_up:
                locked_up = True
                circle = pygame.image.load("graphics\\gui\\circle_highlight.png")
                break
            elif event.key == Globals.actions['cancel']:
                with open('files\\controls', 'wb') as f:
                    pickle.dump(Globals.actions, f)
                Globals.repeat = True
                import main.py
            

    pygame.display.update()



