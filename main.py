import pygame, sys, time, math, os, pickle
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloonatic_gui import *
from scripts.Ultra_Color import *
from scripts.fight_textures import *
from scripts.gui_init import *
from scripts.enemystats import *
from scripts.fight_club import *
from scripts.playerstats import *
music_playing = False
pygame.init()
if not 'Logbook' in Globals.playerdata['key items']:
    Globals.playerdata['key items'].append('Logbook')
pygame.mixer.music.set_volume(Globals.playerdata['Music_volume']) 
font = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 24)
largefont = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 36)
superfont = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 60)
Globals.playerdata['xpcap'] = Globals.xpcap[Globals.playerdata['level'] - 1]
pc = pygame.Color
cSec = 0
cFrame = 0
FPS = 0
Globals.deltatime = 1
blitext = False
festive = 0
shownthrow = True
# (x, y, ID)
killcounter = 0
Globals.active_dialog = None
clock = pygame.time.Clock()

# Initialize Maps
town = 0
cave = 0
villagehouse1 = 0
townstore = 0
ring = pygame.image.load("graphics\\ring.png")

# Initialize and calculate the FPS
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 11)
men_font = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 24)
logo = pygame.image.load("promotional\\Logo\\basic_logo.png")

    
def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, pc("White"))
    if Globals.playerdata['FPS'] == True:
        window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Dungeon Raider"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)


def count_fps():
    global FPS, clock

    FPS = clock.get_fps()
    if FPS > 0:
        Globals.deltatime = 1 / FPS
def store():
    Globals.scene = 'store'

# Intialzize Battle sprites and commands
def attack():

    PlayerIG.attack1 = True
    Globals.fight_turn = 'enemy'
    Fight.PlayerAttack(Globals.playerdata['curweap'])

def magic():

    Globals.fight_turn = 'magic'

def returntomenu():
    Globals.fight_turn = 'player'

def items():
    Globals.fight_turn = 'items'


FightAtt = Menu.Text(text='Attack', font=Font.Default, color=Color.PaleGoldenrod, pos=(20, 600), tag='fight')

FightMag = Menu.Text(text='Magic', font=Font.Default, color=Color.PaleGoldenrod, pos=(20,600), tag='fight')

FightIte = Menu.Text(text='Use Item', font=Font.Default, color=Color.PaleGoldenrod, pos=(20,600), tag='fight')

FightRun = Menu.Text(text='Run Away', font=Font.Default, color=Color.PaleGoldenrod, pos=(20,600), tag='fight')





def windowRedraw():
    global enemy
    enemy = Enemystats.enemies[Globals.enemy_switch]
    if Globals.start_of_battle == True:
        for enemu in Enemystats.enemies:
            if Globals.scaling:
                enemu.maxhealth = enemu.base_health + (Globals.playerdata['level'] * 5)
                enemu.damage = enemu.base_damage + Globals.playerdata['level']
            else:
                enemu.maxhealth = enemu.base_health
                enemu.damage = enemu.base_damage
        enemy.health = enemy.maxhealth
        Globals.start_of_battle = False
    #to draw a background = win.blit('filename', (x, y))
    window.blit(cave_bg, (0, 0))
    Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
    window.blit(pygame.transform.scale(pygame.transform.rotate(cool_bg, 180), (400, 160)), (255, 180))
    enemy.draw(window)
    PlayerIG.draw(window)


    if Globals.fight_turn == 'player':
        Globals.idea_list = ['attack', 'magic', 'item', 'run']
        #Globals.current_list = 0
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (500, 300)), 270), (0, 180))
        if Globals.fight_currentmove == 'attack':
            window.blit(arrow, (180, 240))
            attx, magx, itex, runx = 100, 60, 60, 60
        elif Globals.fight_currentmove == 'magic':
            window.blit(arrow, (180, 300))
            attx, magx, itex, runx = 60, 100, 60, 60
        elif Globals.fight_currentmove == 'item':
            window.blit(arrow, (210, 360))
            attx, magx, itex, runx = 60, 60, 100, 60
        elif Globals.fight_currentmove == 'run':
            window.blit(arrow, (210, 420))
            attx, magx, itex, runx = 60, 60, 60, 100
        else:
            attx, magx, itex, runx = 60, 60, 60, 60
        FightAtt.Render(window, (attx, 240))
        FightMag.Render(window, (magx, 300))
        FightIte.Render(window, (itex, 360))
        FightRun.Render(window, (runx, 420))
    elif Globals.fight_turn == 'magic':
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (500, 300)), 270), (0, 180))
        Globals.idea_list = []
        #Globals.current_list = 0
        y = 240
        for spells in Globals.playerdata['ownspells']:
            text = font.render(spells + str(" -" + str(Globals.weapons[spells.lower()][2])), True, Color.PaleGoldenrod)
            window.blit(text, (70, y))
            y += 40
            Globals.idea_list.append(spells.lower())
        text = font.render('Return to Menu', True, Color.PaleGoldenrod)
        window.blit(text, (70, y))
        Globals.idea_list.append('Return to Menu')
        if Globals.current_list == 0:
            window.blit(arrow, (70 + (len(Globals.idea_list[0]) * 10) + 30, 240))
        elif Globals.current_list == 1:
            window.blit(arrow, (70 + (len(Globals.idea_list[1]) * 10) + 30, 280))
        elif Globals.current_list == 2:
            window.blit(arrow, (70 + (len(Globals.idea_list[2]) * 10) + 30, 320))
        elif Globals.current_list == 3:
            window.blit(arrow, (70 + (len(Globals.idea_list[3]) * 10) + 30, 360))
        elif Globals.current_list == 4:
            window.blit(arrow, (70 + (len(Globals.idea_list[4]) * 10) + 30, 400))
    elif Globals.fight_turn == 'items':
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (500, 300)), 270), (0, 180))
        Globals.idea_list = []
        #Globals.current_list = 0
        y = 240
        for item in Globals.playerdata['items']:
            text = font.render(item + str(" -" + str(Globals.playerdata[item.lower()])), True, Color.PaleGoldenrod)
            window.blit(text, (70, y))
            y += 40
            Globals.idea_list.append(item.lower())
        text = font.render('Return to Menu', True, Color.PaleGoldenrod)
        window.blit(text, (70, y))
        Globals.idea_list.append('Return to Menu')
        if Globals.current_list == 0:
            window.blit(arrow, (70 + (len(Globals.idea_list[0]) * 10) + 30, 240))
        elif Globals.current_list == 1:
            window.blit(arrow, (70 + (len(Globals.idea_list[1]) * 10) + 30, 280))
        elif Globals.current_list == 2:
            window.blit(arrow, (70 + (len(Globals.idea_list[2]) * 10) + 30, 320))
        elif Globals.current_list == 3:
            window.blit(arrow, (70 + (len(Globals.idea_list[3]) * 10) + 30, 360))
        elif Globals.current_list == 4:
            window.blit(arrow, (70 + (len(Globals.idea_list[4]) * 10) + 30, 400))


    else:
        window.blit(pygame.transform.rotate(cool_bg, 270), (20, 570))


    Fight.display(win = window)
    if Globals.win:
        if not Globals.playerdata['health'] <= 0:
            message = ("You defeated the " + str(enemy.name))
            window.blit(Font.Default.render(message, True, Color.White), (70, 500))
            text = ("You gained " + str(enemy.xp) + " experience!")
            ext = ("You gained " + str(enemy.gold) + " gold!")
            window.blit(Font.Default.render(text, True, Color.White), (70, 400))
            window.blit(Font.Default.render(ext, True, Color.White), (70, 450))
            Globals.fight_count += 1
            if Globals.fight_count > 120:
                Globals.win = False
                Globals.scene = 'game'
                enemy.health = enemy.maxhealth
                enemy.damage = enemy.base_damage
                enemy.dead = False
                Globals.playerdata['gold'] += enemy.gold
                Globals.playerdata['experience']+= enemy.xp
                Globals.fight_turn = 'player'
                Globals.current_list = 0
                if Globals.playerdata['experience'] >= Globals.playerdata['xpcap']:
                    Globals.playerdata['level'] += 1
                    Globals.playerdata['skill points'] += 1
                    Globals.playerdata['experience'] -= Globals.playerdata['xpcap']
                    Globals.playerdata['xpcap'] = Globals.xpcap[Globals.playerdata['level'] - 1]
                if Globals.playerdata['guards_somer_killed'] == True and Globals.playerdata['guards_somerquest'] == 'fight':
                    Globals.storyline_fight = True
                    Globals.playerdata['guards_somerquest'] = "2nd_fight"
                    Globals.enemy_switch = 12
                    Globals.current_list = 0
                    Globals.start_of_battle = True
                    Globals.scene = 'fight'
                    Globals.fight_turn = 'player'
                elif Globals.playerdata['guards_somer_killed'] == True and Globals.playerdata['guards_somerquest'] == '2nd_fight':
                    Globals.active_dialog.text = [("We'll be out of your way...", "")]
                    Globals.playerdata['guards_somerquest'] = "part3"
                    Globals.dialog_open = True

                # RUN CORRECT MUSIC
                if Globals.playerdata['location'] == 'lake':
                    pygame.mixer.music.load("music\\Realm-of-Fantasy_Looping.mp3")
                    pygame.mixer.music.play(-1)
                elif Globals.playerdata['location'] == 'fields':
                    pygame.mixer.music.load("music\\our_mountain.mp3")
                    pygame.mixer.music.play(-1)
                elif Globals.playerdata['location'] == 'southern frontier':

                    pygame.mixer.music.load("music\\bosstheme.mp3")
                    pygame.mixer.music.play(-1)
                elif Globals.playerdata['location'] == 'cave':
                    pygame.mixer.music.load("music\\Evil_Guard.mp3")
                    pygame.mixer.music.play(-1)
                elif Globals.playerdata['location'] == 'northern passage':
                    pygame.mixer.music.load("music\\our_mountain.mp3")
                    pygame.mixer.music.play(-1)
                elif Globals.playerdata['location'] == 'somerberry barracks':
                    pygame.mixer.music.load("music\\somerberry_village.mp3")
                    pygame.mixer.music.play(-1)

                # Try to improve performance
                create_window()

        else:
            window.fill((0, 0, 0))
            Globals.current_list = 0
            window.blit(superfont.render("You Died!", True, Color.Red), (300, 240))
            pygame.display.update()
            time.sleep(1)
            window.fill((0, 0, 0))
            window.blit(superfont.render("Reloading from Last Save Point!", True, Color.White), (10, 240))
            pygame.display.update()
            Globals.win = False
            time.sleep(0.5)
            with open(Globals.filename, "rb") as f:
                Globals.playerdata = pickle.load(f)
            Globals.win = False
            Globals.scene = 'game'
            enemy.health = enemy.maxhealth
            enemy.damage = enemy.base_damage
            enemy.dead = False
            pre_savefile()
            check_terrain()
    clock.tick(40)
    text = (largefont.render(str(Globals.playerdata['energy']), True, Color.Goldenrod))
    window.blit(text, (360, 200))
    x, i = 340, 0
    if Globals.playerdata['energy'] != 4:
        while i != Globals.playerdata['energy']:
            text = largefont.render("|", True, Color.Goldenrod)
            window.blit(text, (x, 240))
            x+= 10
            i+= 1
    else:
        while i != Globals.playerdata['energy']:
            text = largefont.render("|", True, Color.PaleGoldenrod)
            window.blit(text, (x, 240))
            x+= 10
            i+= 1
    text = (largefont.render("/", True, Color.PaleGoldenrod))
    i = 0
    window.blit(font.render("BP:", True, Color.Goldenrod), (0, 0))
    x = 40
    while i != Globals.playerdata['maxenergy']:
        window.blit(text, (x, 0))
        i += 1
        x += 8
    pygame.display.update()



def nextpage_dialog():
    if Globals.active_dialog.page < len(Globals.active_dialog.text) - 1:
        Globals.active_dialog.page += 1
    else:
        Globals.dialog_open = False
        Globals.active_dialog.page = 0
        avoid = False
        if Globals.active_dialog.text == manStore.dialog and Globals.playerdata['mapinpoltown'] == 'start':
            Globals.playerdata['mapinpoltown'] = 'done'
            Globals.playerdata['key items'].append('Southern Map')
            manStore.dialog = [("You can use any map by going to your inventory", ""), ("Press the 'C' key to access it", ""), ("Then go into your key items!", "You'll find it there!")]
        elif Globals.active_dialog.text == [("Welcome to my Store!", "What are you looking for today?"),]:
            store()
        elif Globals.active_dialog.text == Barkeep.dialog:
            Globals.current_list = 0
            Globals.fight_turn = 'inn'
        elif Globals.active_dialog.text == merc3.dialog and Globals.playerdata['lakemanquest'] == 'part1':
            Globals.acceptsidequest = True
            Globals.playerdata['sidequest'].append('lakeMercQuest')
            Globals.playerdata['lakemanquest'] = 'part2'
            merc3.dialog = [("You see...", ""), ("I owe some other mercernaries money...", "I can't take them on all myself..."), ("I'd be happy to pay you...", "Just meet me at the northeast corner of town... Okay?")]
            
        elif Globals.active_dialog.text == merc3.dialog and Globals.playerdata['lakemanquest'] == 'part2':
            Globals.playerdata['lakemanquest'] = 'part3'
            merc3.tag = 'pol town'
            merc3.x = 30 * 32
            merc3.y = 96
            merc3.dialog = [("You ready to take them on?", ""), ("I've never been more ready!", ""), ("Just let me know when you're ready!", "")]
        elif Globals.active_dialog.text == merc3.dialog and Globals.playerdata['lakemanquest'] == 'part4':
            Globals.camera_x, Globals.camera_y = -597, 103
            merc4.dialog = [("When you paying up?", "You don't want to keep us waiting!"), ("Huh?", ""), ("What's this kid here for?", ""), ("Hahaha!", ""), ("You thought you could just beat us up!", ""), ("You picked a fight with the wrong people!", ""), ("Ronny you take the kid!", "")]
            Globals.active_dialog = Dialog(merc4.dialog)
            Globals.dialog_open = True
            avoid = True
            Globals.playerdata['lakemanquest'] = 'part5'

        elif Globals.active_dialog.text == merc4.dialog and Globals.playerdata['lakemanquest'] == 'part5':
            Globals.enemy_switch = 1
            Globals.current_list = 0
            Globals.scene = 'fight'
            Globals.start_of_battle = True
            Globals.fight_turn = 'player'
            merc4.tag, merc5.tag = 'abcd', 'abcd'
            Globals.playerdata['lakemanquest'] = 'part6'
            merc3.dialog = [("I'm a little bit hurt...", "Head to my home..."), ("I'll pay you there", ""), ("It's the one closest to you from here!", " ")]
        elif Globals.active_dialog.text == merc3.dialog and Globals.playerdata['lakemanquest'] == 'part6':
            merc3.dialog = [("I made some tea...", ""), ("You want some?", ""), ("It's fine...", ""), ("Here take 60 gold...", "It was the savings for paying up..."), ("I owe you a lot more...", "I owed them more than 400 gold!"), ("Come back anytime and you can have tea again!", "I'm sure it will replenish your health and magic!")]
            merc3.tag = 'villagehouse3'
            merc3.x = 5 * 32
            merc3.y = 5 * 32
            Globals.playerdata['lakemanquest'] = 'part7'
            
        elif Globals.playerdata['lakemanquest'] == 'part7' and Globals.active_dialog.text == merc3.dialog:
            merc3.dialog = [("How are you going?", ""), ("Here I made some tea", "You can have some!"), ("You recovered all your health and magic!", "")]
            Globals.playerdata['gold'] += 60
            Globals.playerdata['lakemanquest'] = 'finished'
            Globals.finishsidequest = True
            Globals.playerdata['sidequests'] += 1
            Globals.playerdata['sidequest'].remove('lakeMercQuest')
            
        elif Globals.playerdata['lakemanquest'] == 'finished' and Globals.active_dialog.text == merc3.dialog:
            Globals.playerdata['health'], Globals.playerdata['magic'] = Globals.playerdata['maxhealth'], Globals.playerdata['maxmagic']



        # Pol town Inn Quest relvolving Lost bottle of whiskey
        elif Globals.playerdata['poltowninnquest'] == 'part1' and Globals.active_dialog.text == manPolInnQuest.dialog:
            Globals.acceptsidequest = True
            Globals.playerdata['sidequest'].append('poltowninnquest')
            if 'Bottle of Whiskey' in Globals.playerdata['key items']:
                Globals.playerdata['poltowninnquest'] = 'part3'
                manPolInnQuest.dialog = [("Thank you so much!", ""), ("Here take 50 gold for your trouble!", "")]
                
            else:
                Globals.playerdata['poltowninnquest'] = 'part2'
                manPolInnQuest.dialog = [("I lost my bottle in the fields to the north-west!", ""), ("I really hope you find it soon!", "")]
        elif Globals.playerdata['poltowninnquest'] == 'part2' and Globals.active_dialog.text == manPolInnQuest.dialog:
            if 'Bottle of Whiskey' in Globals.playerdata['key items']:
                Globals.playerdata['poltowninnquest'] = 'part3'
                manPolInnQuest.dialog = [("Thank you so much!", ""), ("Here take 50 gold for your trouble!", "")]
                
            else:
                Globals.playerdata['poltowninnquest'] = 'part2'
                manPolInnQuest.dialog = [("I lost my bottle in the fields to the north-west!", ""), ("I really hope you find it soon!", "")]
        elif Globals.playerdata['poltowninnquest'] == 'part3' and Globals.active_dialog.text == manPolInnQuest.dialog:
            Globals.playerdata['poltowninnquest'] = 'finished'
            Globals.finishsidequest = True
            Globals.playerdata['sidequests'] += 1
            Globals.playerdata['sidequest'].remove('poltowninnquest')
            Globals.playerdata['gold'] += 50
            Globals.playerdata['key items'].remove("Bottle of Whiskey")
            manPolInnQuest.dialog = [("Ay!", ""), ("How you going my friend!", "")]



                                
        elif Globals.playerdata['storyline'] == 1.0 and manHouseLake.dialog == Globals.active_dialog.text:
            manHouseLake.dialog = [("It's odd thing, the world...", "You know I think I don't remember you"), ("But you are traveller...", " "), ("Evident by the blade on your back...", "I have a task for you to complete"), ("I'll pay with gold...", "You interested?")]
            Globals.playerdata['storyline'] = 1.1
        elif Globals.playerdata['storyline'] == 1.1 and manHouseLake.dialog == Globals.active_dialog.text:
            manHouseLake.dialog = [("Caught your interest, did I?", "hahaha"), ("Money is a dangerous thing you know!", " "),  ("Let's get down to business...", "You see...", " A little while ago, something was stolen from me"), ("Just a little thing", "But it means the world to me"), ("It's sort of like a ring...", "Some nasty mercenaries took it from me..."), ("50 gold to get it back...", "Bring it to me and you'll get your gold")]
            Globals.playerdata['storyline'] = 1.2
        elif Globals.playerdata['storyline'] == 1.2 and manHouseLake.dialog == Globals.active_dialog.text:
            manHouseLake.dialog = [("Hmm..", "No luck?"), ("Reckon you should probably try the town", "Someone there is bound to know!", "Just look for the shadiest people you can find!"), ("I really hope you find my ring soon!", " ")]
            Globals.questart = True
            man2.dialog = [("What do you want!", "Seriously go away!"), ("Mercenaries?", "Rings?"), ("What is this some kind of joke to you!", " "), ("Look...", "I need some soothing apples...."), ("Then you'll get your information!", "I swear!")]
            Globals.playerdata['storyline'] = 1.3
        elif Globals.playerdata['storyline'] == 1.3 and man2.dialog == Globals.active_dialog.text:
            Globals.questart = True
            if Globals.playerdata['soothing apples'] < 1:
                man2.dialog = [("All you have to get is a soothing apple...", "I'll be happy to deal with you then..."), ("Go leave", "Before anyone realises anything!")]
                Globals.playerdata['storyline'] = 1.4
            else:
                man2.dialog = [("Thank you so much!", "Really thanks!"), ("Oh yes...", " "), ("Nearly forgot...", "A couple of days ago, some mercs came to me...", "They told to me get them a ring from some old guy"), ("Gave it to them...", "Got paid...", "They left through the cave"), ("Don't know why", "must be pretty tough blokes to do that!")]
                Globals.playerdata['storyline'] = 1.5
        elif Globals.playerdata['storyline'] == 1.4 and man2.dialog == Globals.active_dialog.text:
            if Globals.playerdata['soothing apples'] < 1:
                man2.dialog = [("All you have to get is a soothing apple...", "I'll be happy to deal with you then..."), ("Go leave", "Before anyone realises anything!")]
                Globals.playerdata['storyline'] = 1.4
            else:
                man2.dialog = [("Thank you so much!", "Really thanks!"), ("Oh yes...", " "), ("Nearly forgot...", "A couple of days ago, some mercs came to me...", "They told to me get them a ring from some old guy"), ("Gave it to them...", "Got paid...", "They left through the cave"), ("Don't know why", "must be pretty tough blokes to do that!")]
                Globals.playerdata['storyline'] = 1.5
        elif Globals.playerdata['storyline'] == 1.5 and man2.dialog == Globals.active_dialog.text:
            man2.dialog = [("Thanks for my apple!", ""), ("The mercenaries went through the cave...", "If you are still looking for them")]
            merc1.dialog = [("Go away...", ""), ("Now", ""), ("What do you mean ring?", "Old dude?"), ("I gonna cut your throat out!", "")]
            Globals.playerdata['storyline'] = 1.6
            Globals.questfinish = True
            Globals.playerdata['quests'] += 1
        elif Globals.playerdata['storyline'] == 1.6 and merc1.dialog == Globals.active_dialog.text:
            Globals.playerdata['storyline'] = 1.7
            Globals.storyline_fight = True
            Globals.enemy_switch = 1
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            merc1.tag = 'crushtown'
            location = [round(merc1.x / Tiles.Size), round(merc1.y / Tiles.Size)]
            Tiles.Blocked.remove(location)
        elif Globals.playerdata['storyline'] == 1.7 and merc2.dialog == Globals.active_dialog.text:
            Globals.playerdata['storyline'] = 1.8
            Globals.storyline_fight = True
            Globals.enemy_switch = 2
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            Globals.idea_list = ["attack"]
            Globals.current_list = 0
            merc2.dialog = [("Do you wish to spare the mercenary?", "")]
            

        elif Globals.playerdata['storyline'] == 1.8 and merc2.dialog == Globals.active_dialog.text:
            Globals.playerdata['storyline'] = 1.9
            Globals.playerdata['ownweapons'].append("Sharp Sword")
            Globals.playerdata['curweap'] = "Sharp Sword"
            location = [round(merc2.x / Tiles.Size), round(merc2.y / Tiles.Size)]
            Tiles.Blocked.remove(location)
            manHouseLake.dialog = [("What!", "You managed to get my ring!",), ("Those mercenaries were really tough...", ""), ("Perhaps the exemplars weren't so sucessful...", "Your powers are still there..."), ("I suppose I must return you your 50 gold.", " "), ("I cannot tell you more...", "Even if it pains me to not do so..."), ("Head to Somerberry Village and visit the old Polen...", "He won't be happy to see you but he will tell you ", "more..."), ("Hmm...", ""), ("This ring was originally owned by a man named ", "Khar", ""), ("True magician he was...", ""), ("He would've wanted you to have it...", "He's been waiting for you a long time")]
            Globals.answers = 2
            Globals.answer1 = 'Kill the mercenary'
            Globals.answer2 = "Spare him"
            Globals.answer_response = ['kill','spare']
            Globals.fight_turn = 'yes or no'
            Globals.fight_currentmove = 'kill'
            Globals.current_list = 0
            Globals.queryid = 'merc1_killing'









        elif Globals.playerdata['storyline'] == 1.9 and Globals.active_dialog.text == [(""), ("The mercenary smiles with gratitude and relief", ""),
                                                                                       ("He grabs the small ring and hands it too you", ""),
                                                ("He also gives you his sharp sword", ""), ("It seems likes sparing him turned out better", "")]:
            merc2.tag = "mercenary's tent"
            merc2.x = 96
            merc2.y = 32
            merc2.dialog = [("...", ""), ("..", ""), ("I've moved on now...", ""), ("I've given up my life of crime...", ""), ("All thanks to you of course!", ""), ("If you ever need any help...", ""), ("Just know I'll be there for you", "")]
        elif Globals.playerdata['storyline'] == 1.9 and Globals.active_dialog.text == [(""), ("The mercenary's eyes freeze...", ""),
                                                ("You grab his sharp sword and brandish it", ""), ("You stab him through the chest", ""),
                                                ("His body falls limp and a small ring drops", "You take it...")]:
            merc2.tag = 'deathhouse'
        elif Globals.playerdata['storyline'] == 1.9 and manHouseLake.dialog == Globals.active_dialog.text:
            Globals.playerdata['storyline'] = 2
            specialtext = largefont.render(("You got Khar's Ring"), True, Color.White)
            specialtext2 = font.render("", True, Color.White)
            blitext = True
            manHouseLake.dialog = [("Head to Somerberry village", "Polen will be waiting for you"), ("It is to the north of here...", "Good luck finding it!")]
            Globals.playerdata['accessories'].append("Khar's Ring")
            Globals.playerdata['gold'] += 50
            Globals.questfinish = True
            Globals.playerdata['quests'] += 1
        elif michael.dialog == Globals.active_dialog.text and Globals.playerdata['michael_quests'] == 0.0:
            Globals.answers = 2
            Globals.answer1 = "I'll help!"
            Globals.answer2 = "You're a waste of time!"
            Globals.answer_response = ['help', 'leave']
            Globals.fight_turn = 'yes or no'
            Globals.fight_currentmove = 'help'
            Globals.current_list = 0
            Globals.queryid = 'help_michael?'
            if Globals.playerdata['michael_refusal'] == True:
                Globals.answers = 2
                Globals.answer2 = "Get out of my way... Or else you will pay"
        elif Globals.playerdata['michael_quests'] == 0.1 and Globals.active_dialog.text == [(""), ("Thank you so much!", "Suppose I should tell you what I need help with!")]:
            michael.x, michael.y = 13 * 32, 32
            michael.dialog = [("Glad you could help!", ""), ("But it seems like you can't continue the story", "now"),
                      ("You know...", ""), ("If you snoop around town...", "You might be able to find out where they are", "keeping my family's shield")]
        elif Globals.playerdata['gideon_quests'] == 0.1 and Globals.playerdata['michael_quests'] == -1 and Globals.active_dialog.text == [(""), ("!!!", ""), ("Sure!!!", ""), ("I'll get out of your way", "")]:
            michael.x, michael.y = 13 * 32, 32
            michael.dialog = [("I promise I won't get in your way!", "")]
        elif Globals.playerdata['michael_quests'] == 0.0 and Globals.active_dialog.text == [(""), ("Oh...", ""), ("Maybe you can help me some other time?", ""), ("I promise it won't be a waste of time", "")]:
            michael.dialog = [("Hey!", ""), ("Have you changed your mind?", "")]
        elif Globals.playerdata['cutscenes']["guard greet somerberry"] == 1.1 and Globals.active_dialog.text == guard1.dialog:
            guard2.x, guard2.y = 17 * 32, 3 *32
            deadKid.tag = 'deathtown'
            guard1.dialog = [("What are you looking at?", ""), ("Keep your nose in your own business", ""), ("Then we won't have any problems!", ""), ("Hahaha", "")]
            Globals.active_dialog = Dialog(guard1.dialog)
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_south.map")
            Globals.dialog_open = True
            avoid = True
            Globals.playerdata['cutscenes']['guard greet somerberry'] = 1.2
        elif Globals.playerdata['cutscenes']["guard greet somerberry"] == 1.2 and Globals.active_dialog.text == guard1.dialog:
            Globals.playerdata['cutscenes']['guard greet somerberry'] = 1.3
            guard1.tag = 'somerberry barracks dungeon'
            guard1.x, guard1.y = 32 * 8, 32 * 3
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_south.map")
        # Command of Somerberry Sidequest
        elif Globals.playerdata['guards_somerquest'] == "part1" and Globals.active_dialog.text == merc6.dialog:
            merc6.dialog = [("Knok and his cronies are set up in the Barracks", ""), ("I mean, where else would those pussies be?", "")]
            Globals.playerdata['guards_somerquest'] = "part2"
            Globals.acceptsidequest = True
            Globals.playerdata['sidequest'].append('guards_somerquest')
        elif Globals.playerdata['guards_somerquest'] == 'part2' and Globals.active_dialog.text == [("Get out of here scum!", "")]:
            Globals.answers = 3
            Globals.answer1 = "Bribe the Guards with 100 gold    "
            Globals.answer2 = "Dispatch them, with your blades    "
            Globals.answer3 = "Leave them"
            Globals.answer_response = ['bribe', 'fight', 'leave']
            Globals.fight_turn = 'yes or no'
            Globals.fight_currentmove = 'bribe'
            Globals.current_list = 0
            Globals.queryid = 'bribe_bar_somer_guards'
        elif Globals.playerdata['guards_somerquest'] == 'part3' and Globals.active_dialog.text == [(""), ("Alright...", ""), ("Boys, let's scram", "")]:
            
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_barracks.map")
            guard4.x, guard5.x, guard6.x, guard7.x = 8 * 32, 9 * 32,  4 * 32, 13 * 32,
            guard4.y, guard5.y, guard6.y, guard7.y = 25 * 32, 25 * 32, 18 * 32, 18 * 32
            guard4.tag, guard5.tag, guard6.tag, guard7.tag = 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry'
        elif Globals.playerdata['guards_somerquest'] == 'part2' and Globals.active_dialog.text == [(""), ("Let's fight, you filthly little vermin!", "")]:
            Globals.fight_turn = 'nil'
            Globals.storyline_fight = True
            Globals.enemy_switch = 12
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.playerdata['guards_somer_killed'] = True
            Globals.playerdata['guards_somerquest'] = "fight"
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            pygame.mixer.music.load("music\\storming_the_barracks.mp3")
        elif Globals.playerdata['guards_somerquest'] == "part3" and Globals.active_dialog.text == [("We'll be out of your way...", "")]:
            guard4.tag, guard5.tag, guard6.tag, guard7.tag = 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry'
            guard4.x, guard5.x, guard6.x, guard7.x = 8 * 32, 9 * 32, 4 * 32, 13 * 32,
            guard4.y, guard5.y, guard6.y, guard7.y = 25 * 32, 25 * 32, 18 * 32, 18 * 32
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_barracks.map")
        elif Globals.playerdata['guards_somerquest'] == "part3" and (Globals.active_dialog.text == guard4.dialog or Globals.active_dialog.text == guard5.dialog):
            Globals.storyline_fight = True
            Globals.enemy_switch = 12
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            Globals.playerdata['guards_somerquest'] = 'part4'
            guard4.y, guard5.y = 8 * 32, 8 * 32
        elif Globals.playerdata['guards_somerquest'] == 'part4' and (Globals.active_dialog.text == guard6.dialog or Globals.active_dialog.text == guard7.dialog):
            Globals.storyline_fight = True
            Globals.enemy_switch = 12
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            Globals.playerdata['guards_somerquest'] = 'part5'
            guard6.tag, guard7.y, guard7.x = 'deathtown', 4 * 32, 7 * 32,
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_barracks_entry.map")
        elif Globals.playerdata['guards_somerquest'] == 'part5' and (Globals.active_dialog.text == guard4.dialog or Globals.active_dialog.text == guard5.dialog):
            Globals.storyline_fight = True
            Globals.enemy_switch = 12
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            Globals.playerdata['guards_somerquest'] = 'part6'
            guard4.tag, guard5.tag = "deathtown", "deathtown"
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_barracks_entry.map")
        elif Globals.playerdata['guards_somerquest'] != 'part4' and (Globals.active_dialog.text == guard7.dialog):
            Globals.storyline_fight = True
            Globals.enemy_switch = 12
            Globals.current_list = 0
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
            guard7.tag = 'deathtown'
            Map_Engine.loading(window, ring)
            pygame.display.update()
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_barracks_entry.map")
        elif Globals.playerdata['guards_somerquest'] == "part7" and Globals.active_dialog.text == guard1.dialog:
            Globals.storyline_fight = True
            Globals.enemy_switch = 13
            Globals.current_list = 0
            Globals.playerdata['guards_somerquest'] = "part8"
            guard1.dialog = [("*Cough*   *Cough*", ""), ("The torturer is at his knees and at your mercy:", "")]
            Globals.start_of_battle = True
            Globals.scene = 'fight'
            Globals.fight_turn = 'player'
        elif Globals.playerdata['guards_somerquest'] == "part8" and Globals.active_dialog.text == guard1.dialog:
            Globals.answers = 2
            Globals.answer1 = "Kill the Torturer...     "
            Globals.answer2 = "Leave him for others to find...    "
            Globals.answer_response = ['kill', 'save']
            Globals.fight_turn = 'yes or no'
            Globals.fight_currentmove = 'kill'
            Globals.current_list = 0
            Globals.queryid = 'kill_torturer?'
        elif Globals.playerdata['guards_somerquest'] == "part8" and Globals.active_dialog.text == [(""),("You stab him through the chest...", ""), ("He will kill no more...", "")]:
            guard1.tag = 'deathtown'
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_dungeons.map")
            Globals.playerdata['guards_somerquest'] = 'part9'
        elif Globals.playerdata['guards_somerquest'] == "part8" and Globals.active_dialog.text == [(""), ("You push the torturer against the wall so that", "you can pass...")]:
            guard1.y = 32
            guard1.dialog = [("The torturer is unconscious...", "")]
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\somerberry_dungeons.map")
            Globals.playerdata['guards_somerquest'] = 'part9'
        elif Globals.playerdata['guards_somerquest'] == 'part10' and Globals.active_dialog.text == commanderKnok.dialog:
            commanderKnok.dialog = [("That an army is only as good as its commander!", "")]
            commanderKnok.facing = "south"
            Globals.playerdata['guards_somerquest'] = 'part11'
            Globals.active_dialog = Dialog(commanderKnok.dialog)
            Globals.dialog_open = True
            avoid = True
        elif Globals.playerdata['guards_somerquest'] == 'part11' and Globals.active_dialog.text == commanderKnok.dialog:
            Globals.scene = "fight"
            Globals.current_list = 0
            Globals.enemy_switch = 14
            Globals.fight_turn = 'player'
            Globals.storyline_fight = True
            Globals.start_of_battle = True
            Globals.playerdata['guards_somerquest'] = "part12"
            commanderKnok.dialog = [("Heh...", ""), ("You are powerful...", ""), ("I hope we see one another yet again", "")]
        elif Globals.playerdata['guards_somerquest'] == "part12" and Globals.active_dialog.text == commanderKnok.dialog:
            commanderKnok.tag = 'crushtown'
            Tiles.Blocked = []
            terrain = Map_Engine.load_map("maps\\final_barrack_room.map")
            Globals.playerdata['guards_somerquest'] = 'part13'
            guard2.tag, guard3.tag = 'deathtown', 'deathtown'
            lady1.dialog = [("Good Day!", ""), ("Knok's guards appear to have vanished overnight!", "")]
            lady2.dialog = [("Hi", ""), ("Stay at the inn!", ""), ("The guards can't bother you any more!", "")]
            merc6.dialog = [("Knok's gone!", ""), ("The whole village is happy!", ""), ("The others won't admit it...", ""), ("But I know it was you...", ""), ("Here take my blade!", ""), ("And I can teach you the defensive strike if you",  "return to me again")]
        elif Globals.playerdata['guards_somerquest'] == 'part13' and merc6.dialog == Globals.active_dialog.text:
            Globals.playerdata['ownweapons'].append("Mercenary's Sword")
            merc6.dialog = [("Would you like me to teach you the defensive", "strike magic technique?"), ("It will remove all previous strikes!", "")]
            Globals.playerdata['guards_somerquest'] = "part14"
            Globals.playerdata['curweap'] = "Mercenary's Sword"
        elif Globals.playerdata['guards_somerquest'] == 'part14' and merc6.dialog == Globals.active_dialog.text:
            Globals.answers = 2
            Globals.answer1 = "Learn Defensive Strike "
            Globals.answer2 = "Do Not Learn Defensive Strike   "
            Globals.answer_response = ['learn', 'leave']
            Globals.fight_turn = 'yes or no'
            Globals.fight_currentmove = 'learn'
            Globals.current_list = 0
            Globals.queryid = 'learn_defensive'
        # Lost Little Bear in the Somerberry Village


        elif Globals.playerdata['little_lost_bear'] == "part1" and Globals.active_dialog.text == guard9.dialog:
            Globals.playerdata['little_lost_bear'] = "part2"
            Globals.acceptsidequest = True
            Globals.playerdata['sidequest'].append('little_lost_bear')
            if "Fluffy Bear" in Globals.playerdata['key items']:
                guard9.dialog = [("Thank you so much!", ""), ("Here - take the treasure room key!", "")]
                Globals.playerdata['little_lost_bear'] = 'part3'
            else:
                guard9.dialog = [("Hopefully you find it soon!", "")]
        elif Globals.playerdata['little_lost_bear'] == "part2" and Globals.active_dialog.text == guard9.dialog:
            if "Fluffy Bear" in Globals.playerdata['key items']:
                guard9.dialog = [("Thank you so much!", ""), ("Here - take the treasure room key!", "")]
                Globals.playerdata['little_lost_bear'] = 'part3'
            else:
                guard9.dialog = [("Hopefully you find it soon!", "")]
        elif Globals.playerdata['little_lost_bear'] == "part3" and Globals.active_dialog.text == guard9.dialog:
            Globals.playerdata['little_lost_bear'] = "finished"
            Globals.finishsidequest = True
            Globals.playerdata['sidequests'] += 1
            Globals.playerdata['sidequest'].remove('little_lost_bear')
            Globals.playerdata['key items'].append("Treasure Room Key")
            Globals.playerdata['key items'].remove("Fluffy Bear")

        
        if not avoid:   
            Globals.active_dialog.text = None
            Globals.npcname = ''


        #Unpause any NPCs

        for npc in NPC.AllNPCs:
            if not npc.Timer.active:
                npc.Timer.Start()
create_window()
# Create NPCs and Player
player = Player("Billy")
player_w, player_h = player.width, player.height
player_x = (window_width /2 - player_w /2 - Globals.camera_x) / Tiles.Size
player_y = (window_height /2 - player_h /2 - Globals.camera_y) / Tiles.Size

man1 = Male1(name="James", pos=(20, 20), dialog=[("Hello!", ("Welcome to POL TOWN"),("How are you?")), ("Did you know monsters live in the cave?", " ") ],
             tag='pol town', walking=True
             )

man2 = Male1(name="Harry", pos=(12, 8), dialog=[("What do you want?", "Just Please leave me alone!"), ("Why must you bully me?", "What did I do to you")],
            tag = 'pol town', walking=True             )
cavemanquest = Male1(name="John", pos =(20, 18), dialog = [('What?!', 'What are you doing strolling around here?'), ('Monsters live here...', 'You should leave while you can'), ('Or not...', 'Just make sure you use your weapons')],
                     tag = 'cave', walking=True)

manStore = Male1(name="Store Joe", pos=(3, 5), dialog=[("Welcome to the Store!", "What are you going to buy!"), ("I brought some gold today too!", ""), ("...", ""), ("You're a traveller!", ""), ("Here take a map. I have one spare", "It's only of the south, though", "They are nasty, those mapmakers")],
                 tag='townstore', walking=True)

StoreKeep = Male1(name="StoreKeep", pos=(6, 17), dialog=[("Welcome to my Store!", "What are you looking for today?"),],
                tag='townstore', walking=True)
StoreKeep = Male1(name="StoreKeep", pos=(7, 3), dialog=[("Welcome to my Store!", "What are you looking for today?"),],
                tag='somerberry store', walking=True)
TentKeep = Male1(name="StoreKeep", pos=(7, 2), dialog=[("Welcome to my Store!", "What are you looking for today?"),],
                tag='frontier market tent', walking=True)
manHouseLake = OldMan(name='Polas', pos=(6, 10), dialog=[("Hmm...", " "), ("Have I seen you before?", " "), ("Say what's your name?", " "), ("Is that so?", "...")],
                     tag='lakehouse', walking=True)
                
merc1 = Merc(name="Low merc", pos=(1, 36), dialog=[("Go away, you skinny thing", "And I mean it... ", "You don't want to fight me")],
             tag='cave', walking=True)

merc2 = Merc(name="Merc Leader", pos=(70, 60), dialog=[("How did you manage my friend?", ""), ("Oh well..", ""), ("Guess I'll have to deal with you myself", "Get ready to die scum!")],
             tag='lake', walking=True)

merc3 = Merc(name='Kolen', pos=(36, 10), dialog=[("What do you want", ""), ("What are you looking at?", ""), ("You're a warrior...", "I might need some help")],
             tag='lake', walking=True, story = 2)

merc4 = Merc(name='merc4', pos=(34, 3), dialog=[("Hmp!", "")], tag='pol town',
             walking=True, story=1.8)
merc5 = Merc(name='merc5', pos=(34, 5), dialog=[("We'd better get our money soon!", "")], tag='pol town',
             walking=True, story=1.8)
merc6 = Merc(name='Kaiden', pos=(11, 45), dialog=[("Heh...", ""), ("You best watch out for those guards", ""), ("They're gonna jump you - ", "once Knok, their commander finds about you", ""), ("They cleaned me up, broke a few bones and ", "now I can't do anything"), ("I'm stuck in this hell-hole, watching others ", "suffer"), ("If you want to help...", ""), ("For that kid...", ""), ("Take out Knok...", "")],
            tag='southern somerberry', walking=True, story=1)

manHouse4 = Male1(name='Mas', pos =(7, 4), dialog=[("Hmm...", ""), ("It is I, Mas the master swordsman!", ""), ("I must teach you my ways!", ""), ("In battle you may use your equiped weapon!", ""), ("Or your owned spells and magic!", ""), ("You can use 'a' or 'd' to increment your BP!", ""), ("Your BP increases your damage of your strikes!", ""), ("You gain 1 BP every turn with a max of 4BP", ""), ("You won't gain BP if you used more than 1 though...", ""), ("Mas has taught well!", "")],
                  tag='villagehouse4', walking=True, story=1)

Barkeep = OldMan(name='Barkeep', pos=(13, 1), dialog=[("You look new", ""), ("Don't listen to the rest of them. They're too drunk!", ""), ("So would you like a drink?", "Or do you want to room to sleep in?")],
                 tag='villageinn', walking=True, story=1)
manInn = Male1(name='John', pos=(6, 2), dialog=[("Hello!", ""), ("Welcome to Pol Town!", ""), ("The drinks here are brillant!", "")],
               tag='villageinn', walking=True, story=1)
mercInn = Merc(name='Mercenary', pos=(13, 10), dialog=[("Hmp!", ""), ("You don't want to know me!", ""), ("And neither do the rest of you!", "")],
               tag='villageinn', walking=True, story=1)
mercTentSite = Merc(name='Resting Hunter', pos=(38, 13), dialog=[("G'day mate.", ""), ("Crushtown's to the right...", ""),("Better be careful - Those pesky orc are", "attacking more frequently"),
                    ("Stock up on supplies before you head off.", "You can get do that in the big tent...")], tag='southern frontier', walking=True, story=1)
manPolInnQuest = Male1(name='Steven', pos=(13, 8), dialog=[("Hmm...", ""), ("Have you been to the fields?", ""), ("I lost my bottle of whiskey", ""), ("If you find it, then can you give it to me", "")],
                       tag='villageinn', walking=True, story=1)

michael = Michael(name='Michael', pos=(12, 1), dialog=[("Hello there!", ""), ("You look like a traveller!", ""), ("I'm afarid I have to ask something of you...", ""),
                                                       ("But I do have something to offer...", ""), ("It's my family's shield", ""),
                                                       ("I'd be happy to give it to you now!", "If you agree to help me with my conundrum")],
                  tag='northern passage', walking=True, story=1)
lady1 = Lady(name='Michelle', pos=(16, 24), dialog=[("Good morning!", ""), ("I would recommend you stay away from the guards", "")],
             tag='southern somerberry', walking=True, story=1)
lady2 = Lady(name='Kate', pos=(14, 46), dialog=[("You really shouldn't have come here", ""), ("The situation only seems to get worse everyday", ""), ("Knok's guards are constantly becoming more ", "violent everyday"), ("No one else will tell you this...", ""),
                                                ("But there was kid...", "And he went missing when he starting snooping", "around the barracks"), ("Rumour is that they tied to a post in the forest", "")],
             tag='southern somerberry', walking=True, story=1)
polen = OldMan(name='Polen', pos=(21, 55), dialog=[("You should really piss off...", "")],
               tag='southern somerberry', walking=True, story=1)
guard1 = Guard(name='Town Guard', pos=(10, 55), dialog=[("Think you can just walk around like that", ""), ("That's just disrespect!",""), ("...", ""),
                ("How about you say something, you little brat", ""), ("...", ""), ("Think we going to need to teach this one a", "few manners...", ""),
                ("Come with us back to the barracks!", "")],
                tag ='southern somerberry', walking=False, story=1)
guard1.facing = "south"
deadKid = Male1(name="hurt kid", pos=(11, 52), dialog=[("nil", "")],
            tag='southern somerberry', walking=True, story=1)
guard2 = Guard(name='Town Guard', pos=(12, 55), dialog=[("What do you want?", ""), ("You have a problem, you take it the boss", ""), ("He's right ahead, in our barracks!", "")],
               tag='southern somerberry', walking=True, story=1)
guard3 = Guard(name='Town Guard', pos=(12, 3), dialog=[("Our barracks are right ahead", ""), ("We'll fix you up if you go there!", "")],
               tag='southern somerberry', walking=True, story=1)
#Guards in the barracks - re-used inside the actual dungeon
guard4 = Guard(name='Barrack Guard', pos=(12, 13), dialog=[("Get out of here scum!", "")],
               tag='somerberry barracks', walking=True, story=1)
guard5 = Guard(name='Barrack Guard', pos=(13, 13), dialog=[("Get out of here scum!", "")],
               tag='somerberry barracks', walking=True, story=1)
guard6 = Guard(name='Barrack Guard', pos=(11, 12), dialog=[("Get out of here scum!", "")],
               tag='somerberry barracks', walking=True, story=1)
guard7 = Guard(name='Barrack Guard', pos=(14, 12), dialog=[("Get out of here scum!", "")],
               tag='somerberry barracks', walking=True, story=1)
guard8 = Guard(name='Off-Duty Guard', pos=(13, 30), dialog=[("Hey...", ""), ("Don't let anyone know I told you this...", ""), ("Once you get up the end of this corridor, to your", "left will be a door"), ("Through there is our weapons stash", ""), ("Take what you need", "Knok's a parasite to this whole village!")],
               tag='somerberry barracks entry', walking=True, story=1)
guard9 = Guard(name='Barrack Guard', pos=(7, 8), dialog=[("Have you seen a little bear?", ""), ("It's my daughter's favourite", ""), ("The others stole it for torture today", ""), ("If you find it, I'll be forever grateful!", "")],
               tag='east barrack wing', walking=True, story=1)
commanderKnok = Knok(name='Commander Knok', pos=(10, 3), dialog=[("So...", ""), ("You defeated my army here...", ""), ("I must congrulate you on your victory...", ""), ("But you must realise...", "")],
               tag='barrack chamber', walking=False, story=1)
guard10 = Guard(name='Supply Guard', pos=(22, 9), dialog=[("I'm here protecting the town's supplies", ""), ("You know", ""), ("From the orcs", "")],
                tag='lower crushtown', walking=False, story=1)
commanderKnok.facing = "north"
commanderKnok.walk__ = False
guard1.walk__ = False
# South - East
# West - North
# Initialize Music
pygame.mixer.music.load("music\\Khar's_Theme.mp3")
pygame.mixer.music.play(-1)

# Initialize Sounds

btnSound = pygame.mixer.Sound("sounds\\button_click.wav")

# INITIALIZE CHESTS

Chest1 = chests((12, 8),tag='cave', number=1)
Chest2= chests((39, 13), tag='pol town', number=2, rewards=[15, 'gold'])
chest3 = chests((2, 3), tag ='villagehouse1', number=3, rewards=[1, 'magic jam'])
chest4 = chests((71, 35), tag='lake', number=4, rewards=[20, 'gold'])
chest5 = chests((25, 58), tag='lake', number=5, rewards=['Wooden Spear', 'weapon'])
chest6 = chests((5, 1), tag='villagehouse2', number=6, rewards=[1, 'soothing apples'])
chest7 = chests((1, 32), tag='fields', number=7, rewards=[40, 'gold'])
chest8 = chests((46, 8), tag='fields', number=8, rewards=['Wooden Shield', 'shield'])
chest9 = chests((58, 18), tag='fields', number=9, rewards=["Bottle of Whiskey", 'key item'])
chest10 = chests((3, 58), tag='southern frontier', number=10, rewards=['Iron Dagger', 'weapon'])
chest11 = chests((3, 20), tag='somerberry barracks entry', number=11, rewards=[2, 'soothing apples'])
chest12 = chests((15, 20), tag='somerberry barracks entry', number=12, rewards=[2, 'magic jam'])
chest13 = chests((26, 1), tag='southern somerberry', number=13, rewards=[50, 'gold'])
chest14 = chests((16, 9), tag='west barrack wing', number=14, rewards=['Dungeon Key', 'key item'])
chest15 = chests((2, 4), tag='east barrack wing', number=15, rewards=['Welded Shield', 'shield'])
chest16 = chests((1, 2), tag='east barrack wing', number=16, rewards=['Welded Sword', 'weapon'])
chest17 = chests((3, 4), tag='somerberry barracks dungeon', number=17, rewards=["Fluffy Bear", "key item"])
chest18 = chests((6, 12), tag='east barrack wing', number=18, rewards=[35, "gold"])
chest19 = chests((14, 1), tag='somerberry barracks dungeon', number=19, rewards=[5, 'magic jam'])
chest20 = chests((16, 1), tag='somerberry barracks dungeon', number=20, rewards=[5, 'soothing apples'])
chest21 = chests((18, 1), tag='somerberry barracks dungeon', number=21, rewards=[150, 'gold'])
chest22 = chests((12, 1), tag="somerberry barracks", number=22, rewards=["Iron-Tipped Spear", 'weapon'])
chest23 = chests((13, 15), tag='barrack puzzle room', number=23, rewards=["Barrack Chest Key", 'key item'])

# INITIALIZE SIGNS

sign1 = signs((23, 21), tag='pol town', info=[("Welcome to the INN", ""), ("Drink away your problems", "")])
sign2 = signs((18, 23), tag='pol town', info=[("Welcome to POL TOWN", ""), ("<- To the Lake", ""), ("-> To the Cave", "")])
sign3 = signs((20, 1), tag='pol town', info=[("Welcome to POL TOWN", ""), ("<- To the Fields", "        -Somberberry Village"), ("-> To the Northern Frontier", "      -Crushtown")])
sign4 = signs((8, 64), tag='southern frontier', info=[("!WARNING!", ""), ("BE CAREFUL OF CLIFFS", ""), ("ROCKS PRONE TO FALLING!", ""), ("<- to Pol Town", "")])
sign5 = signs((16, 1), tag='southern somerberry', info=[("Somerberry Guard Barracks", "")])
sign6 = signs((10, 8), tag='somerberry barracks dungeon', info=[("<- Torture Room", ""), ("-> Treasure Room", "")])
sign7 = signs((17, 3), tag='lower crushtown', info=[("Beware Orc Ambushes!", "Right Ahead!")])


innsign = hangingsigns((22, 19), tag='pol town', image=inn_sign)

# INITIALIZE DOORS

door1 = doors((3, 7), tag='somerberry barracks dungeon', key="Dungeon Key", map_name='maps\\somerberry_dungeons.map')
door2 = doors((16, 7), tag='somerberry barracks dungeon', key="Treasure Room Key", map_name='maps\\somerberry_dungeons.map')
door3 = doors((12, 3), tag='somerberry barracks', key="Barrack Chest Key", map_name='maps\\somerberry_barracks.map')
# INITIALIZE SLABS

slab1 = slabs(pos=(8, 5), tag='west barrack wing', button_pos=(16, 1), btag = "west barrack wing", 
              map_name='maps\\west_barrack_wing.map')
slab2 = slabs(pos=(16, 12), tag='west barrack wing', button_pos=(3, 15), btag = "west barrack wing", 
              map_name='maps\\west_barrack_wing.map')
slab3 = slabs(pos=(3, 3), tag='somerberry barracks', button_pos=(12, 5), btag = "barrack puzzle room",
              map_name='maps\\barrack_puzzle_room.map')
slab4 = slabs(pos=(5, 4), tag='barrack puzzle room', button_pos=(15, 0), btag= "somerberry barracks",
              map_name='maps\\somerberry_barracks.map')
slab5 = slabs(pos=(3, 13), tag='barrack puzzle room', button_pos=(8, 0), btag="somerberry barracks",
              map_name='maps\\somerberry_barracks.map')
slab6 = slabs(pos=(11, 22), tag='barrack puzzle room', button_pos=(3, 18), btag='barrack puzzle room',
              map_name='maps\\barrack_puzzle_room.map')
slab7 = slabs(pos=(12, 23), tag='barrack puzzle room', button_pos=(4, 15), btag="east barrack wing",
              map_name='maps\\east_barrack_wing.map')

# INITIALIZE TREES
# Tree meausurements have 1 tile added to x and 4 tiles added to y
# Pol Town
tree1 = trees((5, 5), tag='pol town')
tree2 = trees((20, 32), tag='pol town')
# Fields
tree3 = trees((2, 2), tag='fields')
tree4 = trees((57, 16.8), tag='fields')
tree5 = trees((58, 17), tag='fields')
tree6 = trees((64, 17), tag='fields')
tree7 = trees((53, 17.5), tag='fields')
tree8 = trees((62, 17.5), tag='fields')
tree9 = trees((56, 20), tag='fields')
tree10 = trees((53, 20.5), tag='fields')
tree11 = trees((58, 20.5), tag='fields')
tree12 = trees((57, 21.8), tag='fields')
# Northern Frontier
tree13 = trees((-0.5, 63), tag='southern frontier')
tree14 = trees((-0.5, 64), tag='southern frontier')
tree15 = trees((-0.5, 65), tag='southern frontier')
tree16 = trees((-0.5, 66), tag='southern frontier')

# INITIALIZE GUI
is_running = True

johnnyboi = 0
terrain = 0
# CHECK TERRAIN
def check_terrain():
    global terrain
    if Globals.playerdata['location'] == 'pol town' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\town.map")
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'southern frontier' and Globals.switch == True:
        if Globals.playerdata['merc1_death'] == False:
            terrain = Map_Engine.load_map("maps\\northern_frontt.map")
        else:
            terrain = Map_Engine.load_map("maps\\northern_front.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'cave' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\cave.map")
        Globals.camera_xmove, Globals.camera_ymove = False, False
        Globals.switch = False
    elif Globals.playerdata['location'] == 'villagehouse1' and Globals.switch == True or Globals.playerdata['location'] == 'villagehouse2' and Globals.switch:
        terrain = Map_Engine.load_map("maps\\villagehouse1.map")
        Globals.camera_y, Globals.camera_x = 169, 143,
        Globals.camera_xmove, Globals.camera_ymove = False, False
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'villagehouse3' and Globals.switch: 
        terrain = Map_Engine.load_map("maps\\villagehouse2.map")
        Globals.camera_y, Globals.camera_x = 145, 300,
        Globals.camera_xmove, Globals.camera_ymove = False, False
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'villagehouse4' and Globals.switch:
        terrain = Map_Engine.load_map("maps\\villagehouse3.map")
        Globals.camera_y, Globals.camera_x = 145, 300
        Globals.camera_xmove, Globals.camera_ymove = False, False
        Globals.switch = False
        create_window()
    elif Globals.playerdata['location'] == 'villageinn' and Globals.switch:
        terrain = Map_Engine.load_map("maps\\inn.map")
        Globals.camera_y, Globals.camera_x = 203, 333
        Globals.camera_xmove, Globals.camera_ymove = False, False
        Globals.switch = False
        create_window()
    elif Globals.playerdata['location'] == 'townstore' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\townshop.map")
        Globals.camera_y, Globals.camera_x = 190, -150
        Globals.camera_xmove, Globals.camera_ymove = False, False
        Globals.idea_list = 'soothing apple'
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'lake' and Globals.switch == True: 
        terrain = Map_Engine.load_map("maps\\lake.map")
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'lakehouse' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\laketown.map")
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'fields' and Globals.switch == True: 
        terrain = Map_Engine.load_map("maps\\fields.map")
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'northern passage' and Globals.switch == True:
        passage = Map_Engine.load_map("maps\\passage.map")
        terrain = passage
        create_window()
        Globals.switch = False
    elif Globals.playerdata['location'] == 'southern somerberry' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_south.map")
        Globals.switch = False
        if Globals.playerdata['cutscenes']["guard greet somerberry"] == 0.0:   
            Globals.playerdata['cutscenes']["guard greet somerberry"] = 1.1
            Globals.active_dialog = Dialog(guard1.dialog)
            Globals.dialog_open = True
    elif Globals.playerdata['location'] == 'somerberry barracks' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_barracks.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'somerberry barracks entry' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_barracks_entry.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'west barrack wing' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\west_barrack_wing.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'east barrack wing' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\east_barrack_wing.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'somerberry barracks dungeon' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_dungeons.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'barrack chamber' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\final_barrack_room.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'somerberry barrack corridor' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\barrack_corridor.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'barrack puzzle room' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\barrack_puzzle_room.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'somerberry store' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_store.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'somerberry inn' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\somerberry_inn.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'frontier market tent' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\frontier_market.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == 'lower crushtown' and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\crushtown_lower.map")
        Globals.switch = False
    elif Globals.playerdata['location'] == "mercenary's tent" and Globals.switch == True:
        terrain = Map_Engine.load_map("maps\\merc_tent.map")
        Globals.switch = False
    if Globals.play_music:
        pygame.mixer.music.load(Globals.music[Globals.playerdata['location']])
        pygame.mixer.music.play(-1)
        Globals.play_music = False

# Manage Savefiles
def pre_savefile():
    Tiles.Blocked = []
    terrain = 0
    Globals.win = False
    Globals.scene = "game"
    Globals.camera_x, Globals.camera_y = Globals.playerdata['preloca'][0], Globals.playerdata['preloca'][1]
    deletable = []
    # Initialize Correct dialog for storyline
    if Globals.playerdata['storyline'] > 1.5:
        man2.dialog = [("Thanks for my apple!", ""), ("The mercenaries went through the cave...", "If you are still looking for them")]
        merc1.dialog = [("Go away...", ""), ("Now", ""), ("What do you mean ring?", "Old dude?"), ("I gonna cut your throat out!", "")]
    if Globals.playerdata['storyline'] > 1.6:
        merc1.tag = 'crushtown'
    if Globals.playerdata['storyline'] > 1.8:
        manHouseLake.dialog = [("What!", "You managed to get my ring!",), ("Those mercenaries were really tough...", ""), ("Perhaps the wakunjra weren't so sucessful...", "Your powers are still there..."), ("I suppose I must return you your 50 gold.", " "), ("I cannot tell you more...", "Even if it pains me to not do so..."), ("Head to Somerberry Village and visit the old Polen...", "He won't be happy to see you but he will tell you ", "more..."), ("Hmm...", ""), ("This ring was originally owned by a man named ", "Khar", ""), ("True magician he was...", ""), ("He would've wanted you to have it...", "He's been waiting for you a long time")]
    if Globals.playerdata['storyline'] >= 1.9:
        merc2.tag = "mercenary's tent"
        merc2.x = 96
        merc2.y = 32
        merc2.dialog = [("...", ""), ("..", ""), ("I've moved on now...", ""), ("I've given up my life of crime...", ""), ("All thanks to you of course!", ""), ("If you ever need any help...", ""), ("Just know I'll be there for you", "")]
    if Globals.playerdata['storyline'] > 1.9:
        manHouseLake.dialog = [("Head to Somerberry village", "Polen will be waiting for you"), ("It is to the north of here...", "Good luck finding it!")]
    # Initialize correct dialog for lakemanquest
    if Globals.playerdata['lakemanquest'] == 'part3':
        merc3.tag = 'pol town'
        merc3.x = 30 * 32
        merc3.y = 96
        merc3.dialog = [("You ready to take them on?", ""), ("I've never been more ready!", ""), ("Just let me know when you're ready!", "")]
    elif Globals.playerdata['lakemanquest'] == 'part6':
        merc3.tag = 'pol town'
        merc3.x = 30 * 32
        merc3.y = 96
        merc3.dialog = [("I'm a little bit hurt...", "Head to my home..."), ("I'll pay you there", ""), ("It's the one closest to you from here!", " ")]
    elif Globals.playerdata['lakemanquest'] == 'finished':
            merc4.tag, merc5.tag = 'abcd', 'abcd'
            merc3.tag, merc3.x, merc3.y = 'villagehouse3', 5*32, 5*32
            merc3.dialog = [("How are you going?", ""), ("Here I made some tea", "You can have some!"), ("You recovered all your health and magic!", "")]
    # Initialize correct dialog for pol town inn quest
    if Globals.playerdata['poltowninnquest'] == 'part3':
                                        
        manPolInnQuest.dialog = [("Thank you so much!", ""), ("Here take 50 gold for your trouble!", "")]

    elif Globals.playerdata['poltowninnquest'] == 'part2':
        manPolInnQuest.dialog = [("I lost my bottle in the fields to the north-west!", ""), ("I really hope you find it soon!", "")]
    elif Globals.playerdata['poltowninnquest'] == 'finished':
        manPolInnQuest.dialog = [("Ay!", ""), ("How you going my friend!", "")]
    if Globals.playerdata['mapinpoltown'] == 'done':
        manStore.dialog = [("I bought some jams today", "")]
    if Globals.playerdata['michael_quests'] == 0.1:
        michael.dialog = [("Glad you could help!", ""), ("I think you should start looking around in town...", ""), ("Somebody there is bound to know something", "")]
        michael.x, michael.y = 13 * 32, 32
    if Globals.playerdata['michael_quests'] == -1:
        michael.dialog = [("Hey!", ""), ("Have you changed your mind?", "")]
    if Globals.playerdata['gideon_quests'] == 0.1:
        michael.x, michael.y = 13 * 32, 32
    if Globals.playerdata['cutscenes']['guard greet somerberry'] == 1.3:
        guard2.x, guard2.y = 17 * 32, 3 *32
        deadKid.tag = 'deathtown'
        guard1.tag = 'somerberry barracks dungeon'
        guard1.x, guard1.y = 32 * 8, 32 * 3
        guard1.dialog = [("Hey!", ""), ("Thought I told you not to mess with us", ""), ("Guess I'll have to kill you, just like that kid", "")]
    # Guards of Somerberry Quest
    test_1= Globals.playerdata['guards_somerquest'].split("t")
    test_1 = int(test_1[1])
    if test_1 >= 2:
        merc6.dialog = [("Knok and his cronies are set up in the Barracks", ""), ("I mean, where else would those pussies be?", "")]
    if test_1 >= 3:
        guard4.tag, guard5.tag, guard6.tag, guard7.tag = 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry', 'somerberry barracks entry'
        guard4.x, guard5.x, guard6.x, guard7.x = 8 * 32, 9 * 32, 4 * 32, 13 * 32,
        guard4.y, guard5.y, guard6.y, guard7.y = 25 * 32, 25 * 32, 19 * 32, 19 * 32
    if test_1 >= 4:
        guard4.y, guard5.y, guard6.y, guard7.y = 8 * 32, 8 * 32, 19 * 32, 19 * 32
    if test_1 >= 5:
        guard6.tag = 'deathtown'
        guard7.x =  7 * 32
        guard7.y = 4 * 32
    if test_1 >= 6:
        guard4.tag, guard5.tag, = 'deathtown', 'deathtown',
    if test_1 >= 7:
        guard1.tag = 'somerberry barracks dungeon'
        guard1.x, guard1.y = 32 * 8, 32 * 3
    if test_1 >= 8:
        guard1.dialog = [("*Cough*  *Cough*", ""), ("The torturer is at his knees and at your mercy:", "")]
    if test_1 >= 9:
        guard1.tag = 'deathtown'
    if test_1 >= 11:
        commanderKnok.dialog = [("Heh...", ""), ("You are powerful...", ""), ("I hope we see one another yet again", "")]
    if test_1 >=12:
        commanderKnok.tag = 'crushtown'
        guard2.tag, guard3.tag = 'deathtown'
        lady1.dialog = [("Good Day!", ""), ("Knok's guards appear to have vanished overnight!", "")]
        lady2.dialog = [("Hi", ""), ("Stay at the inn!", ""), ("The guards can't bother you any more!", "")]
        merc6.dialog = [("Knok's gone!", ""), ("The whole village is happy!", ""), ("The others won't admit it...", ""), ("But I know it was you...", ""), ("Here take my blade!", ""), ("And I can teach you the defensive strike", "if you return to me again")]
    if test_1 >= 13:
        merc6.dialog = [("Would you like me to teach you the defensive", "strike magic technique?"), ("It will remove all previous strikes!", "")]
    Globals.switch = True


    circle = pygame.image.load("graphics\\gui\\circle.png")

    # Main Game Loop

    pygame.mixer.music.set_volume(Globals.playerdata['Music_volume']) 
pre_savefile()
is_running = True
Character_speed = 100
while is_running:
    # Render Background

    # Choose correct terrain and location

    



    
    check_terrain()
    if Globals.playerdata['location'] not in Globals.playerdata['discovered locations']:
        Globals.playerdata['discovered locations'].append(Globals.playerdata['location'])


    # clear the window
    window.fill((0, 0, 0))
    # check for keyboard and mouse inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            # cancel input button
            if event.key == pygame.K_c and Globals.scene != 'fight':
                if Globals.scene != 'inventory':
                    Globals.scene = 'inventory'
                    Globals.fight_turn = 'invent'
                    Globals.current_list = 0
                else: Globals.scene = 'game'
            # pause input button
            if event.key == Globals.actions['pause'] and Globals.scene != 'fight':
                if Globals.scene != 'menu': Globals.scene, Globals.current_list, = "menu", 0
                else: Globals.scene, Globals.switch = 'game', True
                    
            # up arrow input button
            if event.key == pygame.K_w and not Globals.dialog_open or event.key == pygame.K_UP and not Globals.dialog_open:
                if Globals.scene == 'game' and not Globals.fight_turn == 'inn' and not Globals.fight_turn == 'yes or no':
                    Globals.camera_ymove = 1
                    Character_speed = 200

                elif Globals.scene == 'fight' or Globals.scene == 'store' or Globals.scene == 'inventory' or Globals.fight_turn == 'inn' or Globals.scene == 'menu' or Globals.fight_turn == 'yes or no'  or Globals.scene == 'logbook':
                    if not Globals.current_list - 1 < 0:
                        Globals.current_list -= 1
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                    else:
                        Globals.current_list = len(Globals.idea_list) - 1
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                elif Globals.scene == 'skill tree':
                    if Globals.fight_turn == 'select':
                        if Globals.current_list[0] != 0:
                            if Globals.current_list[0] == 1:
                                if Globals.current_list[1] >= 1:
                                    Globals.current_list[1] -= 1
                                    if Globals.current_list[1] >= 3:
                                        Globals.current_list[1] -= 1
                                        
                            Globals.current_list[0] -= 1

            # down arrow input button
            elif event.key == pygame.K_s and not Globals.dialog_open or event.key == pygame.K_DOWN and not Globals.dialog_open:
                if Globals.scene == 'game'  and not Globals.fight_turn == 'inn' and not Globals.fight_turn == 'yes or no':
                    Globals.camera_ymove = 2
                    Character_speed = 200

                elif Globals.scene == 'fight' or Globals.scene == 'store' or Globals.scene == 'inventory' or Globals.fight_turn == 'inn' or Globals.scene == 'menu' or Globals.fight_turn == 'yes or no' or Globals.scene == 'logbook':
                    if not Globals.current_list + 1 > len(Globals.idea_list) - 1:
                        Globals.current_list += 1
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                    else:
                        Globals.current_list = 0
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                elif Globals.scene == 'skill tree':
                    if Globals.fight_turn == 'select':
                        if Globals.current_list[0] != 2:
                            if Globals.current_list[0] == 0:
                                if Globals.current_list[1] == 4: Globals.current_list[1] = 6
                                elif Globals.current_list[1] == 3: Globals.current_list[1] = 5
                                elif Globals.current_list[1] == 2: Globals.current_list[1] = 3
                                elif Globals.current_list[1] == 1: Globals.current_list[1] = 2
                                else: Globals.current_list[1] = 0
                            Globals.current_list[0] += 1

            # left arrow input button
            elif event.key == pygame.K_a and not Globals.dialog_open or event.key == pygame.K_LEFT and not Globals.dialog_open and not Globals.fight_turn == 'yes or no':
                if Globals.scene == 'game':
                    Globals.camera_xmove = 1
                    Character_speed = 200
                    
                elif Globals.scene == 'fight' and Globals.fight_turn == 'player' or Globals.scene == 'fight' and Globals.fight_turn == 'magic':
                    Globals.playerdata['energy'] -= 1
                    if 0 >= Globals.playerdata['energy']:
                        Globals.playerdata['energy'] = 1
                elif Globals.scene == 'skill tree':
                    if Globals.fight_turn == 'select':
                        if Globals.current_list[1] != 0:
                            Globals.current_list[1] -= 1
                    elif Globals.fight_turn == 'surity':
                        Globals.fight_currentmove = "yes"
            # right arrow input button
            elif event.key == pygame.K_d and not Globals.dialog_open or event.key == pygame.K_RIGHT and not Globals.dialog_open and not Globals.fight_turn == 'yes or no':
                if Globals.scene == 'game':
                    Globals.camera_xmove = 2
                    Character_speed = 200

                elif Globals.scene == 'fight' and Globals.fight_turn == 'player' or Globals.scene == 'fight' and Globals.fight_turn == 'magic':
                    Globals.playerdata['energy'] += 1
                    if Globals.playerdata['maxenergy'] < Globals.playerdata['energy']:
                        Globals.playerdata['energy'] = Globals.playerdata['maxenergy']
                elif Globals.scene == 'skill tree':
                    if Globals.fight_turn == 'select':
                        if Globals.current_list[0] != 6:
                            if not (Globals.current_list[0] == 0 and Globals.current_list[1] == 4):
                                Globals.current_list[1] += 1
                    elif Globals.fight_turn == 'surity':
                        Globals.fight_currentmove = "no"

            # running input button
            if event.key == pygame.K_LSHIFT or event.key == Globals.actions['run']:
                Character_speed = 400
            # cancel input button
            if event.key == Globals.actions['cancel']:
                if Globals.fight_turn == 'magic':
                    returntomenu()
                elif Globals.fight_turn == 'items':
                    returntomenu()
                elif Globals.scene == 'options':
                    Globals.scene == 'menu'
                elif Globals.scene == 'inventory':
                    Globals.fight_turn == 'inventory'
                elif Globals.scene == 'help':
                    Globals.scene = 'menu'
                elif Globals.scene == 'map':
                    Globals.scene = 'inventory'
                    Globals.fight_turn = 'key_items'
                if Globals.dialog_open:
                        nextpage_dialog()
            # The ACTION button. The most annoying piece of crap
            if event.key == pygame.K_RETURN or event.key == Globals.actions['action1']:
                if Globals.scene == 'game':
                    if Globals.fight_turn == 'inn':
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                        if Globals.fight_currentmove == 'return':
                            Globals.active_dialog = Dialog([(""), ("Hmp", "See you sometime, maybe?")])
                            Globals.dialog_open = True
                        elif Globals.fight_currentmove == 'inn':
                            if Globals.playerdata['location'] == 'somerberry inn' and int(Globals.playerdata['guards_somerquest'].split("t")[1]) <= 12:
                                gold_amount = 100
                            else: gold_amount = 50
                            if Globals.playerdata['gold'] >= gold_amount:
                                Globals.playerdata['gold'] -= gold_amount
                                Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
                                Globals.active_dialog = Dialog([(""), ("Have a good sleep?", "See you around!"), ("You recovered all of your health and magic!", "")])
                                Globals.dialog_open = True
                                
                            else:
                                Globals.active_dialog = Dialog([(""), ("You should get some more gold...", "I'll need " + str(gold_amount) +" for a room")])
                                Globals.dialog_open = True
                        elif Globals.fight_currentmove == 'drink':
                            if Globals.playerdata['gold'] >= 5:
                                Globals.playerdata['magic'] += 5
                                Globals.playerdata['gold'] -= 5
                                if Globals.playerdata['magic'] > Globals.playerdata['maxmagic']:
                                    Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
                                    Globals.active_dialog = Dialog([(""), ("Go home", "You don't want anymore")])
                                    Globals.dialog_open = True
                                else:
                                    Globals.active_dialog = Dialog([(""), ("Have a nice time...", ""), ("There's always more!", "")])
                                    Globals.dialog_open = True
                        Globals.fight_turn = 'player'
                        Globals.scene = 'game'
                        Globals.current_list = 0
                    elif Globals.fight_turn == 'yes or no':
                        Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                        Globals.checkquery(Globals.queryid, Globals.fight_currentmove)
                        print(Globals.queryid)
                        print(Globals.fight_currentmove)
                        print(Globals.fight_turn)
                        Globals.current_list = 0
                        Globals.scene = 'game'
                        
                            
                  
                    if Globals.dialog_open:
                        nextpage_dialog()

                    else:
                        # If dialog isn't open
                        for npc in NPC.AllNPCs:
                            #Is Player within Speech boundaries
                            # Player Coords are by tile
                            # NPC Coords are by pixels

                            npc_x = npc.x / Tiles.Size
                            npc_y = npc.y / Tiles.Size
                            if player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y -2 and player_y <= npc_y + 2 and npc.tag == Globals.playerdata['location']:
                                #Player is next to NPC - Are they facing them?
                                if player.facing == 'north' and npc_y < player_y:
                                    Globals.dialog_open = True
                                    Globals.npcname = npc.name
                                    Globals.active_dialog = Dialog(npc.dialog)
                                    npc.Timer.Pause()
                                    npc.walking = False
                                    break
                                elif player.facing == 'south' and npc_y > player_y:
                                    Globals.dialog_open = True
                                    Globals.npcname = npc.name
                                    Globals.active_dialog = Dialog(npc.dialog)
                                    npc.Timer.Pause()
                                    npc.walking = False
                                    break
                                elif player.facing == 'east' and npc_x < player_x:
                                    Globals.dialog_open = True
                                    Globals.npcname = npc.name
                                    Globals.active_dialog = Dialog(npc.dialog)
                                    npc.Timer.Pause()
                                    npc.walking = False
                                    break
                                elif player.facing == 'west' and npc_x > player_x:
                                    Globals.dialog_open = True
                                    Globals.npcname = npc.name
                                    Globals.active_dialog = Dialog(npc.dialog)
                                    npc.Timer.Pause()
                                    npc.walking = False
                                    break
                        for chest in chests.Allchests:
                            chest_x = chest.x / Tiles.Size
                            chest_y = chest.y / Tiles.Size
                            if chest.tag == Globals.playerdata['location']:
                                if player_x >= chest_x - 1 and player_x <= chest_x + 1 and player_y >= chest_y -1 and player_y <= chest_y + 2:
                                    # Player is next to chest - Are they facing it?
                                    
                                    if player.facing == 'north' and chest_y < player_y:
                                        
                                        chests.chest_open(chest)

                                    elif player.facing == 'south' and chest_y > player_y:
                                        
                                        chests.chest_open(chest)

                                    elif player.facing == 'east' and chest_x < player_x:
                                        
                                        chests.chest_open(chest)

                                    elif player.facing == 'west' and chest_x > player_x:
                                        
                                        chests.chest_open(chest)
                        for chest in signs.Allsigns:
                            chest_x = chest.x / Tiles.Size
                            chest_y = chest.y / Tiles.Size
                            if chest.tag == Globals.playerdata['location']:
                                if player_x >= chest_x - 1 and player_x <= chest_x + 1 and player_y >= chest_y -1 and player_y <= chest_y + 2:
                                    # Player is next to chest - Are they facing it?
                                    
                                    if player.facing == 'north' and chest_y < player_y:

                                        signs.sign_open(chest)

                                    elif player.facing == 'south' and chest_y > player_y:

                                        signs.sign_open(chest)

                                    elif player.facing == 'east' and chest_x < player_x:
           
                                        signs.sign_open(chest)

                                    elif player.facing == 'west' and chest_x > player_x:
           
                                        signs.sign_open(chest)

                        # Opening the slab with some buttons
                        for chest in slabs.Allslabs:
                            chest_x = chest.butx / Tiles.Size
                            chest_y = chest.buty / Tiles.Size
                            if chest.but_tag == Globals.playerdata['location']:
                                if player_x >= chest_x - 1 and player_x <= chest_x + 1 and player_y >= chest_y -1 and player_y <= chest_y + 2:
                                    # Player is next to chest - Are they facing it?
                                    
                                    if player.facing == 'north' and chest_y < player_y:

                                        slabs.open_button(chest)
                                       
                                        Tiles.Blocked = []
                                        terrain = Map_Engine.load_map(chest.map)

                                    elif player.facing == 'south' and chest_y > player_y:

                                        slabs.open_button(chest)
                                        
                                        Tiles.Blocked = []
                                        terrain = Map_Engine.load_map(chest.map)


                                    elif player.facing == 'east' and chest_x < player_x:
           
                                        slabs.open_button(chest)
                                        
                                        Tiles.Blocked = []
                                        terrain = Map_Engine.load_map(chest.map)


                                    elif player.facing == 'west' and chest_x > player_x:
           
                                        slabs.open_button(chest)
                                       
                                        Tiles.Blocked = []
                                        terrain = Map_Engine.load_map(chest.map)
                        # Opening the slab with some buttons
                        for chest in doors.Alldoors:
                            chest_x = chest.x / Tiles.Size
                            chest_y = chest.y / Tiles.Size
                            if chest.tag == Globals.playerdata['location']:
                                if player_x >= chest_x - 1 and player_x <= chest_x + 1 and player_y >= chest_y -1 and player_y <= chest_y + 2:
                                    # Player is next to chest - Are they facing it?
                                    
                                    if player.facing == 'north' and chest_y < player_y:

                                        doors.door_open(chest)
                                        if chest.key in Globals.playerdata['key items']:
                                            Tiles.Blocked = []
                                            terrain = Map_Engine.load_map(chest.map)

                                    elif player.facing == 'south' and chest_y > player_y:

                                        doors.door_open(chest)
                                        if chest.key in Globals.playerdata['key items']:
                                            Tiles.Blocked = []
                                            terrain = Map_Engine.load_map(chest.map)



                                    elif player.facing == 'east' and chest_x < player_x:
           
                                        doors.door_open(chest)
                                        if chest.key in Globals.playerdata['key items']:
                                            Tiles.Blocked = []
                                            terrain = Map_Engine.load_map(chest.map)



                                    elif player.facing == 'west' and chest_x > player_x:
           
                                        doors.door_open(chest)
                                        if chest.key in Globals.playerdata['key items']:
                                            Tiles.Blocked = []
                                            terrain = Map_Engine.load_map(chest.map)


                            


                elif Globals.scene == 'fight':
                    if Globals.playerdata['realm'] == 'normal':
                        if Globals.fight_currentmove == 'attack' and Globals.fight_turn == 'player':
                            attack()
                        elif Globals.fight_currentmove == 'magic' and Globals.fight_turn == 'player':
                            magic()
                        elif Globals.fight_currentmove == 'item'  and Globals.fight_turn == 'player':
                            items()
                        elif Globals.fight_currentmove == 'run'  and Globals.fight_turn == 'player':
                            if not Globals.storyline_fight:
                                Globals.scene = 'game'
                                enemy.health = enemy.maxhealth
                                if Globals.playerdata['location'] == 'lake':
                                    pygame.mixer.music.load("music\\Realm-of-Fantasy_Looping.mp3")
                                    pygame.mixer.music.play(-1)
                                elif Globals.playerdata['location'] == 'fields':
                                    pygame.mixer.music.load("music\\our_mountain.mp3")
                                    pygame.mixer.music.play(-1)
                                elif Globals.playerdata['location'] == 'southern frontier':

                                    pygame.mixer.music.load("music\\bosstheme.mp3")
                                    pygame.mixer.music.play(-1)
                                elif Globals.playerdata['location'] == 'cave':
                                    pygame.mixer.music.load("music\\Evil_Guard.mp3")
                                    pygame.mixer.music.play(-1)
                                elif Globals.playerdata['location'] == 'northern passage':
                                    pygame.mixer.music.load("music\\our_mountain.mp3")
                                    pygame.mixer.music.play(-1)
                            else:
                                blitext = True
                                specialtext = font.render("You can't run away from this!", True, Color.White)
                                specialtext2 = font.render("", True, Color.White)
                                
                        elif Globals.fight_turn == 'magic':
                            if Globals.current_list == len(Globals.idea_list) -1:
                                Globals.current_list = 0
                                returntomenu()
                            else:
                                spells = Globals.idea_list[Globals.current_list]
                                if Globals.playerdata['magic'] >= Globals.weapons[spells][2]:
                                    i = 0
                                    while i < 100:
                                        i+= 1
                                    if spells == 'heavy sword strike' or 'strike' in spells:
                                        PlayerIG.hattack = True
                                    elif spells == 'fireball':
                                        PlayerIG.fireballatt = True
                                    PlayerIG.attackcount = 0  
                                    Globals.fight_turn = 'enemy'
                                    Globals.playerdata['magic'] -= Globals.weapons[spells][2]
                                    Fight.PlayerAttack(spells)
                                else:
                                    blitext = True
                                    specialtext = font.render("You have no magic!", True, Color.White)
                                    specialtext2 = font.render("", True, Color.White)
                        elif Globals.fight_turn == 'items':
                            if Globals.current_list == len(Globals.idea_list) -1:
                                Globals.current_list = 0
                                returntomenu()
                            else:
                                item = Globals.idea_list[Globals.current_list]
                                if Globals.playerdata[item] >= 1:
                                    if item == 'soothing apples':
                                        Globals.playerdata['health'] += 50
                                        if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                            Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                        specialtext = men_font.render(str('''You ate a soothing apple and '''), True, Color.White)
                                        specialtext2 = men_font.render("now you recovered 50 health!", True, Color.White)
                                    elif item == 'magic jam':
                                        Globals.playerdata['magic'] += 30
                                        if Globals.playerdata['magic'] > Globals.playerdata['maxmagic']:
                                            Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
                                        specialtext = men_font.render(str('''You drank some magic jam and '''), True, Color.White)
                                        specialtext2 = men_font.render("now you recovered 30 magic!", True, Color.White)
                                    elif item == 'fruit jam':
                                        Globals.playerdata['magic'] += 30
                                        Globals.playerdata['health'] += 30
                                        if Globals.playerdata['magic'] > Globals.playerdata['maxmagic']:
                                            Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
                                        if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                            Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                        specialtext = men_font.render(str('''You drank some fruit jam and '''), True, Color.White)
                                        specialtext2 = men_font.render("now you recovered 30 magic and health!", True, Color.White)
                                    elif item == "mushed berries":
                                        Globals.playerdata['health'] += 20
                                        if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                            Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                        specialtext = men_font.render(str('''You ate some mushed berries and '''), True, Color.White)
                                        specialtext2 = men_font.render("now you recovered 20 health!", True, Color.White)
                                    Globals.fight_turn = 'enemy'
                                    Globals.playerdata[item] -= 1
                                    Fight.EnemyAttack(enemy.weapon)
                                else:
                                    specialtext = men_font.render(str("You have none!"), True, Color.White)
                                blitext = True
                elif Globals.scene == 'store':
                    if len(Globals.idea_list) -1 == Globals.current_list:
                        Globals.scene = 'game'
                    elif Globals.playerdata['gold'] >= Globals.itemcost[Globals.fight_currentmove]:
                        Globals.playerdata['gold'] -= Globals.itemcost[Globals.fight_currentmove]
                        Globals.playerdata[Globals.fight_currentmove] += 1
                        specialtext = font.render(str("You sucessfuly bought one!"), True, Color.White)
                        specialtext2 = font.render("", True, Color.White)
                        if Globals.fight_currentmove not in Globals.playerdata['items']: Globals.playerdata['items'].append(Globals.fight_currentmove)
                        blitext = True
                    else:
                        specialtext = font.render(str("You don't have enough gold!"), True, Color.White)
                        specialtext2 = font.render("", True, Color.White)
                        blitext = True
        
                
                elif Globals.scene == 'inventory':
                    if len(Globals.idea_list) == 0:
                        inventory_switch()
                    else:
                        if Globals.fight_turn == 'invent':
                            if Globals.current_list == 0:
                                Globals.fight_turn = 'weapons'
                                Globals.current_list = 0
                            elif Globals.current_list == 1:
                                Globals.fight_turn = 'shields'
                                Globals.current_list = 0
                            elif Globals.current_list == 2:
                                Globals.fight_turn = 'accessories'
                                Globals.current_list = 0
                            elif Globals.current_list == 3:
                                Globals.fight_turn = 'key_items'
                                Globals.current_list = 0
                            elif Globals.current_list == 4:
                                Globals.fight_turn = 'use_items'
                                Globals.current_list = 0
                            elif Globals.current_list == 5:
                                Globals.scene = 'skill tree'
                                Globals.fight_turn = 'select'
                                Globals.current_list = [0, 0]
                        elif Globals.fight_turn == 'weapons':
                            if Globals.weapons[Globals.idea_list[Globals.current_list].lower()][2] == ("sword" or "spear"): local = 0
                            elif Globals.weapons[Globals.idea_list[Globals.current_list].lower()][2] == "axe": local = 1
                            elif Globals.weapons[Globals.idea_list[Globals.current_list].lower()][2] == "bow": local = 2
                            elif Globals.weapons[Globals.idea_list[Globals.current_list].lower()][2] == "magic": local = 3
                            if Globals.playerdata['skills'][0][local] == True:
                                Globals.playerdata['curweap'] = Globals.idea_list[Globals.current_list]
                            Globals.fight_turn = 'invent'
                        elif Globals.fight_turn == 'shields':
                            Globals.playerdata['curshield'] = Globals.idea_list[Globals.current_list]
                            Globals.fight_turn = 'invent'
                        elif Globals.fight_turn == 'key_items':
                            if Globals.idea_list[Globals.current_list] == 'Southern Map':
                                Globals.scene = 'map'
                                Globals.fight_turn = 'south'
                            elif Globals.idea_list[Globals.current_list] == 'Logbook':
                                Globals.scene = 'logbook'
                                Globals.current_list = 0
                            else:
                                Globals.fight_turn = 'invent'
                        elif Globals.fight_turn == 'accessories':
                            Globals.playerdata['accessory'] = Globals.idea_list[Globals.current_list]
                            Globals.fight_turn = 'invent'
                        elif Globals.fight_turn == 'use_items':
                            if Globals.fight_currentmove == 'soothing apples':
                                if Globals.playerdata['soothing apples'] > 0:
                                    Globals.playerdata['health'] += 50
                                    if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                        Globals.playerdata['health'] = Globals.playerdata['maxhealth']

                                    Globals.playerdata['soothing apples'] -= 1

                                else:
                                    Globals.fight_turn = 'invent'
                            elif Globals.fight_currentmove == 'magic jam':
                                if Globals.playerdata['magic jam'] > 0:
                                    Globals.playerdata['magic'] += 30
                                    if Globals.playerdata['magic'] > Globals.playerdata['maxmagic']:
                                        Globals.playerdata['magic'] = Globals.playerdata['maxmagic']

                                    Globals.playerdata['magic jam'] -= 1

                                else:
                                    Globals.fight_turn = 'invent'
                            elif item == 'fruit jam':
                                if Globals.playerdata['fruit jam'] > 0:
                                    Globals.playerdata['magic'] += 30
                                    Globals.playerdata['magic'] += 30
                                    Globals.playerdata['health'] += 30
                                    if Globals.playerdata['magic'] > Globals.playerdata['maxmagic']:
                                        Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
                                    if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                        Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                    Globals.playerdata['fruit jam'] -= 1
                                else:
                                    Globals.fight_turn = 'invent'
                            elif item == "mushed berries":
                                if Globals.playerdata['mushed berries'] > 0:
                                    Globals.playerdata['health'] += 20
                                    if Globals.playerdata['health'] > Globals.playerdata['maxhealth']:
                                        Globals.playerdata['health'] = Globals.playerdata['maxhealth']
                                    Globals.playerdata['mushed berries'] -= 1
                                else:
                                    Globals.fight_turn = 'invent'
                            else:
                                Globals.fight_turn = 'invent'
                elif Globals.scene == 'help':
                    Globals.scene = 'menu'
                elif Globals.scene == 'map':
                    Globals.scene = 'inventory'
                    Globals.fight_turn = 'key_items'
                elif Globals.scene == 'logbook':
                    Globals.scene = 'inventory'
                    Globals.fight_turn = 'key_items'
                elif Globals.scene == 'menu':
                    Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
                    if Globals.fight_currentmove == 'save':
                        Globals.playerdata['preloca'] = [Globals.camera_x, Globals.camera_y]
                        print("You have successfully saved the game")
                        blitext = True
                        specialtext = font.render("You succesfully saved the game", True, Color.White)
                        specialtext2 = font.render("", True, Color.White)
                        with open(Globals.filename, 'wb') as f:
                            pickle.dump(Globals.playerdata, f)
                        create_window()
                    elif Globals.fight_currentmove == 'help':
                        Globals.scene = 'help'
                    elif Globals.fight_currentmove == 'play':
                        Globals.scene = 'game'
                    elif Globals.fight_currentmove == 'options':
                        Globals.scene = 'options'
                    elif Globals.fight_currentmove == 'exit':
                        is_running = False
                elif Globals.scene == 'skill tree':
                    if Globals.fight_turn == "select":
                        if Globals.playerdata['skills'][Globals.current_list[0]][Globals.current_list[1]] == False:
                            x = 0
                            if Globals.current_list[0] == 2:
                                x = Globals.current_list[1] - 1
                            elif Globals.current_list[0] == 1:
                                if Globals.current_list[1] >= 1 and Globals.current_list[1] <= 3: x = Globals.current_list[1] - 1
                                elif Globals.current_list[1] <= 6: x = Globals.current_list[1] - 2
                            else: 
                                Globals.fight_turn = "reject"
                            try:
                                if Globals.playerdata['skills'][Globals.current_list[0] - 1][x] == True:
                                    if Globals.skill_class[Globals.current_list[0]][Globals.current_list[1]] == 2:
                                        Globals.prev_choice = Globals.fight_currentmove
                                        Globals.fight_turn = 'surity'
                                        Globals.fight_currentmove = 'yes'
                                    elif Globals.skill_class[Globals.current_list[0]][Globals.current_list[1]] == 1:
                                        Globals.fight_turn = "reject"
                                else: Globals.fight_turn = "unlock prior"
                            except KeyError: pass
                        elif Globals.playerdata['skills'][Globals.current_list[0]][Globals.current_list[1]] == True:
                            Globals.fight_turn = 'rejection'
                    elif Globals.fight_turn == "surity":
                        if Globals.fight_currentmove == 'yes':
                            if Globals.playerdata['skill points'] > 0:
                                Globals.playerdata['skills'][Globals.current_list[0]][Globals.current_list[1]] = True
                                Globals.fight_turn = 'congrats'
                                Globals.playerdata['skill points'] -= 1
                            else:
                                Globals.fight_turn = 'not enough'
                        else:
                            Globals.fight_turn = 'select'
                    elif Globals.fight_turn == 'rejection': Globals.fight_turn = "select"
                    elif Globals.fight_turn == 'reject' : Globals.fight_turn = "select"
                    elif Globals.fight_turn == 'unlock prior' : Globals.fight_turn = "select"
                    elif Globals.fight_turn == 'not enough': Globals.fight_turn = 'select'
                    elif Globals.fight_turn == 'congrats': Globals.fight_turn = 'select'











        elif event.type == pygame.KEYUP:
            myList = pygame.key.get_pressed()
            if not myList[pygame.K_w] and not myList[pygame.K_s]:
                Globals.camera_ymove = 0
            if not myList[pygame.K_a] and not myList[pygame.K_d]:
                Globals.camera_xmove = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   # Left Click


                # Handle Button Click Events
                for btn in Menu.Button.All:

                    if btn.Tag[0] == Globals.scene and btn.Rolling:

                        if btn.Command is not None:
                            btnSound.play()
                            time.sleep(0.3)
                            btn.Command() # Run Button Event
                            
                        btn.Rolling = False
                        break # Exit Loop





    


    # RENDER SCENE

    if Globals.scene == "game":


        # Logic

        if Globals.camera_ymove == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += Character_speed * Globals.deltatime
                if Globals.playerdata['location'] in Globals.enemyLocation and Globals.scene == 'game':
                    if random.randint(1, Globals.enemyLocation[Globals.playerdata['location']]) == 20:
                        Globals.scene = 'fight'
                        Globals.fight_turn = 'player'
                        Fight.prefight()
                
            player.facing = "north"
        elif Globals.camera_ymove == 2:
            if not Tiles.Blocked_At((round(player_x),math.ceil(player_y))):
                Globals.camera_y -= Character_speed * Globals.deltatime
                if Globals.playerdata['location'] in Globals.enemyLocation and Globals.scene =='game':
                    if random.randint(1, Globals.enemyLocation[Globals.playerdata['location']]) == 20:
                        Globals.scene = 'fight'
                        Globals.fight_turn = 'player'
                        Fight.prefight()
                        
            player.facing = "south"
        if Globals.camera_xmove == 1:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += Character_speed * Globals.deltatime
                if Globals.playerdata['location'] in Globals.enemyLocation and Globals.scene == 'game':
                    if random.randint(1, Globals.enemyLocation[Globals.playerdata['location']]) == 20:
                        Globals.scene = 'fight'
                        Globals.fight_turn = 'player'
                        Fight.prefight()
                        
            player.facing = "east"
        elif Globals.camera_xmove == 2:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= Character_speed * Globals.deltatime
                if Globals.playerdata['location'] in Globals.enemyLocation and Globals.scene == 'game':
                    if random.randint(1, Globals.enemyLocation[Globals.playerdata['location']]) == 20:
                        Globals.scene = 'fight'
                        Globals.fight_turn = 'player'
                        Fight.prefight()
                        
            player.facing = "west"

        player_x = (window_width / 2-player_w / 2-Globals.camera_x) / Tiles.Size

        player_y = (window_height /2 - player_h /2 - Globals.camera_y) / Tiles.Size



        # Render Pause Button


        # Render Terrain Grid
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        player.render(window, ((window_width /2 - player_w /2),(window_height /2 - player_h /2)))
        # Render Non-Playable Characters
        for npc in NPC.AllNPCs:
            if npc.tag == Globals.playerdata['location'] and Globals.playerdata['storyline'] >= npc.story:
                npc.Render(window)

        
        # Render Chests      
        for chest in chests.Allchests:
            if chest.tag == Globals.playerdata['location']:
                location = [chest.x /32, chest.y / 32]
                Tiles.Blocked.append(location)
                try:
                    if Globals.playerdata['chests'][chest.number]:
                        i = 1
                    else:
                        i = 0
                    window.blit(gold_chest[i], (chest.x + Globals.camera_x, chest.y + Globals.camera_y))
                except KeyError:
                    pass
        # Render signs
        for chest in signs.Allsigns:
            if chest.tag == Globals.playerdata['location']:
                location = [chest.x /32, chest.y / 32]
                Tiles.Blocked.append(location)
                window.blit(sign_img, (chest.x + Globals.camera_x, chest.y + Globals.camera_y))
        # render inn signs
        for chest in hangingsigns.Allsigns:
            if chest.tag == Globals.playerdata['location']:
                window.blit(chest.img, (chest.x + Globals.camera_x + 2, chest.y + Globals.camera_y))

        # render chests
        for chest in trees.Alltrees:
            if chest.tag == Globals.playerdata['location']:
                
                location = [round((chest.x + 16) /32), round((chest.y + 66) / 32)]
                Tiles.Blocked.append(location)
                window.blit(tree_img, (chest.x + Globals.camera_x, chest.y + Globals.camera_y))
        # render doors
        for door in doors.Alldoors:
            if door.tag == Globals.playerdata['location']:
                
                location = [round((door.x) /32), round((door.y) / 32)]
                Tiles.Blocked.append(location)
                window.blit(locked_door, (door.x + Globals.camera_x, door.y + Globals.camera_y))
        # render slabs and their buttons
        for data in slabs.Allslabs:
            if data.tag == Globals.playerdata['location']:
                
                location = [round((data.x) /32), round((data.y) / 32)]
                Tiles.Blocked.append(location)
                window.blit(slabImg, (data.x + Globals.camera_x, data.y + Globals.camera_y))
            if data.but_tag == Globals.playerdata['location']:
                location = [round((data.butx) /32), round((data.buty) / 32)]
                Tiles.Blocked.append(location)
                window.blit(buttonImg, (data.butx + Globals.camera_x, data.buty + Globals.camera_y))
            

            



            
        if Globals.dialog_open:
            window.blit(Dialog_background, (window_width / 2 - Dialog_background_width / 2, window_height - Dialog_background_height - 2))
            window.blit(font.render(Globals.npcname, True, Color.Black), (140, 530))
                # Render Text to Dialog
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.text[Globals.active_dialog.page]

                for line in lines:  # draw text to screen
                    window.blit(Font.Default.render(line, True, Color.White), (130, (window_height - Dialog_background_height + 20) + 5 + (lines.index(line)) * 25))
                if Globals.playerdata["cavequest1"] == 'part 1' and cavemanquest.dialog == Globals.active_dialog.text:
                    cavemanquest.dialog = [("What!?", "Oh it's just you")]
                    Globals.playerdata["cavequest1"] = 'finished'


        if Globals.fight_turn == 'inn':
            window.blit(Dialog_background, (window_width / 2 - Dialog_background_width / 2, window_height - Dialog_background_height - 2))
            window.blit(Font.Default.render("Stay at Inn", True, Color.Black), (150, 400))
            window.blit(Font.Default.render("Order a Drink", True, Color.Black), (150, 430))
            window.blit(Font.Default.render("Do nothing", True, Color.Black), (150, 460))
            Globals.idea_list = ['inn', 'drink', 'return']
            if Globals.current_list == 0:
                window.blit(arrow, (280, 400))
            elif Globals.current_list == 1:
                window.blit(arrow, (280, 430))
            elif Globals.current_list == 2:
                window.blit(arrow, (280, 460))
            Globals.camera_ymove = False
            Globals.camera_xmove = False
        elif Globals.fight_turn == 'yes or no':
            window.blit(Dialog_background, (window_width /2 - Dialog_background_width / 2, window_height - Dialog_background_height -2))
            if Globals.answers == 4:
                window.blit(Font.Default.render(Globals.answer4, True, Color.Black), (150, 490))
            if Globals.answers >= 3:
                window.blit(Font.Default.render(Globals.answer3, True, Color.Black), (150, 460))
            if Globals.answers >= 2:
                window.blit(Font.Default.render(Globals.answer2, True, Color.Black), (150, 430))
            if Globals.answers >= 1:
                window.blit(Font.Default.render(Globals.answer1, True, Color.Black), (150, 400))
            Globals.idea_list = Globals.answer_response
            if Globals.current_list == 0:
                x_length = len(Globals.answer1) * 5
                window.blit(arrow, (280 + x_length, 400))
            elif Globals.current_list == 1:
                x_length = len(Globals.answer2) * 5
                window.blit(arrow, (280 + x_length, 430))
            elif Globals.current_list == 2:
                x_length = len(Globals.answer3) * 5
                window.blit(arrow, (280 + x_length, 460))
            elif Globals.current_list == 3:
                x_length = len(Globals.answer4) * 5
                window.blit(arrow, (280 + x_length, 490))
            Globals.camera_ymove = False
            Globals.camera_xmove = False
            
            
            

            # Process Menu
    elif Globals.scene == "menu":
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg,(600, 400)), 270), (window_width / 2 - 400 / 2, 80))
        window.blit(Font.Default.render("Play", True, Color.Black), (320, 180))
        window.blit(Font.Default.render("Help", True, Color.Black), (320, 210))
        window.blit(Font.Default.render("Options", True, Color.Black), (320, 240))
        window.blit(Font.Default.render("Save", True, Color.Black), (320, 270))
        window.blit(Font.Default.render("Exit", True, Color.Black), (320, 300))
        
        Globals.idea_list = ['play', 'help', 'options', 'save', 'exit']
        if Globals.current_list == 0:
            window.blit(arrow, (450, 182))
        elif Globals.current_list == 1:
            window.blit(arrow, (450, 212))
        elif Globals.current_list == 2:
            window.blit(arrow, (450, 242))
        elif Globals.current_list == 3:
            window.blit(arrow, (450, 272))
        elif Globals.current_list == 4:
            window.blit(arrow, (450, 302))
        Globals.camera_ymove = False
        Globals.camera_xmove = False
        window.blit(Font.Large.render("Dungeon Raider", True, Color.White), (200, 10))
        window.blit(logo, (45, 400))
        

                

    elif Globals.scene == 'options':

        for btn in Menu.Button.All:
            if btn.Tag[0] == 'options':
                btn.Render(window)
        window.blit(logo, (420 - logo.get_size()[0] / 2, window_height - logo.get_size()[1]))
        menuFPS.Render(window)
        menuVol.Render(window)
    elif Globals.scene == 'inventory':
        window.blit(Sky, (0, 0))
        Globals.idea_list = []
        Globals.idea_list.append(Globals.playerdata['curweap'])
        Globals.idea_list.append(Globals.playerdata['curshield'])
        
        Globals.idea_list.append(Globals.playerdata['accessory'])
        Globals.idea_list.append("key_items")
        Globals.idea_list.append("use_items")
        Globals.idea_list.append("skill_tree")
        for btn in Menu.Button.All:
            if btn.Tag[0] == 'inventory':
                btn.Render(window)
        window.blit(pygame.transform.scale(Idle[0], (500, 370)), (-100, 0))
        window.blit(pygame.transform.scale(text_background, (450, 185)), (300, 0))

        window.blit(men_font.render(str("Gold: " + str(Globals.playerdata['gold'])), True, Color.PaleGoldenrod),(340, 60))
        message = str("Health: " + str(Globals.playerdata['health']))
        mess = str("/" + str(Globals.playerdata['maxhealth']))
        messy = message + mess
        window.blit(men_font.render(messy, True, Color.PaleGoldenrod), (500, 30))
        message = ('Level: ' + str(Globals.playerdata['level']))
        window.blit(men_font.render(message, True, Color.PaleGoldenrod), (480, 60))
        message = ('Exp to next: ' + str(Globals.playerdata['xpcap'] - Globals.playerdata['experience']))
        window.blit(men_font.render(message, True, Color.PaleGoldenrod), (560, 60))
        message = ('Magic: ' + str(Globals.playerdata['magic']) + '/' + str(Globals.playerdata['maxmagic']))
        window.blit(men_font.render(message, True, Color.PaleGoldenrod), (340, 30))
        window.blit(men_font.render(str("Equiped Weapon: " + str(Globals.playerdata['curweap'])), True, Color.PaleGoldenrod), (340, 100))
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (600, 450)), 270), (300, 170))
        if Globals.fight_turn == 'invent':
            text = ('Weapon: ' + str(Globals.playerdata['curweap']))
            window.blit(men_font.render(text, True, Color.Gold), (380, 280))
            text2 = ('Shield: ' + str(Globals.playerdata['curshield']))
            window.blit(men_font.render(text2, True, Color.Gold), (380, 320))
            text3 = ('Accessory: ' + str(Globals.playerdata['accessory']))
            window.blit(men_font.render(text3, True, Color.Gold), (380, 360))
            text4 = ('View Key Items')
            window.blit(men_font.render(text4, True, Color.Gold), (380, 400))
            text4 = ('Use your items')
            window.blit(men_font.render(text4, True, Color.Gold), (380, 440))
            text4 = ('Skill Tree')
            window.blit(men_font.render(text4, True, Color.Gold), (380, 480))
        elif Globals.fight_turn == 'weapons':

            window.blit(men_font.render(str("Equip which weapon?"), True, Color.Gold), (380, 240))
            y = 280
            Globals.idea_list = []
            for weap in Globals.playerdata['ownweapons']:
                window.blit(men_font.render(weap, True, Color.Gold), (380, y))
                y += 40
                Globals.idea_list.append(weap)
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
            window.blit(pygame.transform.scale(cool_bg, (350, 125)), (0, 380))
            if len(Globals.itemdescrip[Globals.fight_currentmove]) > 40:
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove][0:39], True, Color.PaleGoldenrod)
                length = len(Globals.itemdescrip[Globals.fight_currentmove])
                text2 = font.render(Globals.itemdescrip[Globals.fight_currentmove][40:length], True, Color.PaleGoldenrod)
            else:                       
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.PaleGoldenrod)
                text2 = font.render("", True, Color.PaleGoldenrod)
            window.blit(text, (15, 400))
            window.blit(text2, (15, 430))

            
        elif Globals.fight_turn == 'shields':

            window.blit(men_font.render(str("Equip which shield?"), True, Color.Gold), (380, 240))
            y = 280
            Globals.idea_list = []
            for shield in Globals.playerdata['ownshield']:
                window.blit(men_font.render(shield, True, Color.Gold), (380, y))
                y += 40
                Globals.idea_list.append(shield)
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
            window.blit(pygame.transform.scale(cool_bg, (350, 125)), (0, 380))
            if len(Globals.itemdescrip[Globals.fight_currentmove]) > 40:
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove][0:39], True, Color.PaleGoldenrod)
                length = len(Globals.itemdescrip[Globals.fight_currentmove])
                text2 = font.render(Globals.itemdescrip[Globals.fight_currentmove][40:length], True, Color.PaleGoldenrod)
            else:                       
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.PaleGoldenrod)
                text2 = font.render("", True, Color.PaleGoldenrod)
            window.blit(text, (15, 400))
            window.blit(text2, (15, 430))

            
        elif Globals.fight_turn == 'accessories':
            window.blit(men_font.render(str("Equip which accesory?"), True, Color.Gold), (380, 240))
            y = 280
            Globals.idea_list = []
            for access in Globals.playerdata['accessories']:
                window.blit(men_font.render(access, True, Color.Gold), (380, y))
                y += 40
                Globals.idea_list.append(access)
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
            window.blit(pygame.transform.scale(cool_bg, (350, 125)), (0, 380))
            if len(Globals.itemdescrip[Globals.fight_currentmove]) > 40:
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove][0:39], True, Color.PaleGoldenrod)
                length = len(Globals.itemdescrip[Globals.fight_currentmove])
                text2 = font.render(Globals.itemdescrip[Globals.fight_currentmove][40:length], True, Color.PaleGoldenrod)
            else:                       
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.PaleGoldenrod)
                text2 = font.render("", True, Color.PaleGoldenrod)
            window.blit(text, (15, 400))
            window.blit(text2, (15, 430))

            
        elif Globals.fight_turn == 'key_items':
            Globals.idea_list = []
            window.blit(font.render("Key Items:", True, Color.PaleGoldenrod), (380, 240))
            y = 280
            for item in Globals.playerdata['key items']:
                text = font.render(item, True, Color.PaleGoldenrod)
                window.blit(text, (380, y))
                y += 40
                Globals.idea_list.append(item)
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
            window.blit(pygame.transform.scale(cool_bg, (350, 125)), (0, 380))
            if len(Globals.itemdescrip[Globals.fight_currentmove]) > 40:
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove][0:39], True, Color.PaleGoldenrod)
                length = len(Globals.itemdescrip[Globals.fight_currentmove]) 
                text2 = font.render(Globals.itemdescrip[Globals.fight_currentmove][39:length], True, Color.PaleGoldenrod)
            else:                       
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.PaleGoldenrod)
                text2 = font.render("", True, Color.PaleGoldenrod)
            window.blit(text, (15, 400))
            window.blit(text2, (15, 430))

            
        elif Globals.fight_turn =='use_items':
            Globals.idea_list = []
            #Globals.current_list = 0
            window.blit(font.render("Use which item?", True, Color.PaleGoldenrod), (380, 240))
            y = 280
            for item in Globals.playerdata['items']:
                text = font.render(item + str(" -" + str(Globals.playerdata[item.lower()])), True, Color.PaleGoldenrod)
                window.blit(text, (380, y))
                y += 40
                Globals.idea_list.append(item.lower())
            window.blit(font.render(str("Return to Menu"), True, Color.PaleGoldenrod), (380, y))
            Globals.idea_list.append("Return to Menu")
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
            window.blit(pygame.transform.scale(cool_bg, (350, 125)), (0, 380))
            if len(Globals.itemdescrip[Globals.fight_currentmove]) > 40:
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove][0:39], True, Color.PaleGoldenrod)
                length = len(Globals.itemdescrip[Globals.fight_currentmove]) 
                text2 = font.render(Globals.itemdescrip[Globals.fight_currentmove][40:length], True, Color.PaleGoldenrod)
            else:                       
                text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.PaleGoldenrod)
                text2 = font.render("", True, Color.PaleGoldenrod)
            window.blit(text, (15, 400))
            window.blit(text2, (15, 430))
            
        y = 280
        if len(Globals.idea_list) > 0:
            if Globals.current_list == 0:
                window.blit(arrow, (380 + len(Globals.idea_list[0]) * 10 + 90, y))
        if len(Globals.idea_list) > 1:
            if Globals.current_list == 1:
                y = 320
                window.blit(arrow, (380 + len(Globals.idea_list[1]) * 10 + 90, y))
        if len(Globals.idea_list) > 2:
            if Globals.current_list == 2:
                y = 360
                window.blit(arrow, (380 + len(Globals.idea_list[2]) * 10 + 90, y))
        if len(Globals.idea_list) > 3:
            if Globals.current_list == 3:
                y = 400
                window.blit(arrow, (380 + len(Globals.idea_list[2]) * 10 + 90, y))
        if len(Globals.idea_list) > 4:
            if Globals.current_list == 4:
                y = 440
                window.blit(arrow, (380 + len(Globals.idea_list[2]) * 10 + 90, y))
        if len(Globals.idea_list) > 5:
            if Globals.current_list == 5:
                y = 480
                window.blit(arrow, (380 + len(Globals.idea_list[2]) * 10 + 90, y))

    elif Globals.scene == 'fight':
        if Globals.playerdata['realm'] == 'normal':
            windowRedraw()
    elif Globals.scene == 'map':
        if Globals.fight_turn == 'south':
            window.blit(Sky, (0, 0))
            window.blit(pygame.transform.scale(cool_bg, (500, 300)), (0, 0))
    elif Globals.scene == 'logbook':
        window.fill((0, 0, 0))
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (600, 200)), 270), (0, 0))
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (800, 800)), 90), (180, 0))
        window.blit(font.render("Quest:", True, Color.Black), (40, 30))
        y = 80
        Globals.idea_list = []
        if Globals.playerdata['storyline'] >= 0.0:
            window.blit(font.render("Chapter 1", True, Color.Black), (40, y))
            y += 30
            Globals.idea_list.append("Chapter 1")
        for quest in Globals.list_of_quests:
            if not Globals.playerdata[quest] == 'part1':
                if quest == "poltowninnquest": rendering = "Lost Whiskey"
                elif quest == 'guards_somerquest': rendering = "Command of Somer"
                elif quest == 'lakemanquest' : rendering = "Mercenary Payment"
                elif quest == 'little_lost_bear' : rendering = "Torturous Bear"
                window.blit(font.render(rendering, True, Color.Black), (40, y))
                y += 30
                Globals.idea_list.append(quest)
        window.blit(font.render("DETAILS:", True, Color.Black), (220, 20))
        
        y = 60
        if Globals.idea_list[Globals.current_list] == "Chapter 1":
            for storyline in [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
                if storyline <= Globals.playerdata['storyline']:
                    window.blit(font.render(Globals.chapter1[storyline], True, Color.Black), (220, y))
                    y +=30 
        elif Globals.idea_list[Globals.current_list] == "poltowninnquest":
            for storyline in ['part2', 'part3', 'finished']:
                if Globals.playerdata['poltowninnquest'] == storyline:
                    window.blit(font.render(Globals.poltowninnquest_details[storyline][0], True, Color.Black), (220, y))
                    y +=30
                    window.blit(font.render(Globals.poltowninnquest_details[storyline][1], True, Color.Black), (220, y))
        elif Globals.idea_list[Globals.current_list] == "guards_somerquest":
            test = Globals.playerdata['guards_somerquest'].split("t")[1]
            for storyline in [2, 3, 4, 7, 8]:
                if int(test) >= storyline:
                    window.blit(font.render(Globals.guards_somerquest[storyline][0], True, Color.Black), (220, y))
                    y +=30
                    window.blit(font.render(Globals.guards_somerquest[storyline][1], True, Color.Black), (220, y))
                    if not Globals.guards_somerquest[storyline][1] == "":
                        y +=30
                    window.blit(font.render(Globals.guards_somerquest[storyline][2], True, Color.Black), (220, y))
                    if not Globals.guards_somerquest[storyline][2] == "":
                        y +=30
        elif Globals.idea_list[Globals.current_list] == "lakemanquest":
            for storyline in ['part2']:
                if Globals.playerdata['lakemanquest'] == storyline:
                    window.blit(font.render(Globals.lakemanquest[storyline][0], True, Color.Black), (220, y))
        elif Globals.idea_list[Globals.current_list] == "little_lost_bear":
            for storyline in ['part2', 'part3', 'finished']:
                if Globals.playerdata['lakemanquest'] == storyline:
                    window.blit(font.render(Globals.lakemanquest[storyline][0], True, Color.Black), (220, y))
                    y +=30
                    window.blit(font.render(Globals.guards_somerquest[storyline][1], True, Color.Black), (220, y))
                    y +=30
        
        
    elif Globals.scene == 'store':
        window.blit(Sky, (0, 0))
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (500, 300)), 270), (0, 180))
        window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (500, 200)), 180), (0, -15))
        text = font.render('Welcome to the ' + str(Globals.playerdata['location']), True, Color.PaleGoldenrod)
        window.blit(text, (35, 30))
        Globals.idea_list = []
        #Globals.current_list = 0
        y = 240
        Globals.idea_list = []
        for item in Globals.storelist[Globals.playerdata['location']]:
            text = font.render(item + str(" - " + str(Globals.itemcost[item]) ), True, Color.PaleGoldenrod)
            window.blit(text, (70, y))
            y += 40
            Globals.idea_list.append(item.lower())
        text = font.render('Return to Menu', True, Color.PaleGoldenrod)
        window.blit(text, (70, y))
        Globals.idea_list.append('Return to Menu')
        if not Globals.current_list > len(Globals.idea_list) -1:
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list]
        else:
            Globals.fight_currentmove = Globals.idea_list[0]
        if Globals.current_list == 0:
            window.blit(arrow, (70 + (len(Globals.idea_list[0]) * 10) + 30, 240))
        elif Globals.current_list == 1:
            window.blit(arrow, (70 + (len(Globals.idea_list[1]) * 10) + 30, 280))
        elif Globals.current_list == 2:
            window.blit(arrow, (70 + (len(Globals.idea_list[2]) * 10) + 30, 320))
        elif Globals.current_list == 3:
            window.blit(arrow, (70 + (len(Globals.idea_list[3]) * 10) + 30, 360))
        elif Globals.current_list == 4:
            window.blit(arrow, (70 + (len(Globals.idea_list[4]) * 10) + 30, 400))
        if not Globals.current_list == len(Globals.idea_list) - 1:
            window.blit(pygame.transform.rotate(pygame.transform.scale(cool_bg, (400, 200)), 180), (300, 185))
            text = font.render(Globals.itemdescrip[Globals.fight_currentmove], True, Color.Goldenrod)
            window.blit(text, (300, 225))
            text = font.render("You currently have " + str(Globals.playerdata[Globals.fight_currentmove]), True, Color.Goldenrod)
            window.blit(text, (300, 250))
        text = font.render(str("Gold: " + str(Globals.playerdata['gold'])), True, Color.Goldenrod)
        window.blit(text, (30, 70))
    elif Globals.scene == 'help':
        window.fill((0, 0, 0))
        window.blit(pygame.transform.scale(cool_bg, (800, 600)), (0, 0))
        text = superfont.render(str("Welcome to the help menu!"), True, Color.White)
        window.blit(text, (40, 0))
        text = font.render(str("Use WASD to move around the world!        Enemies appear randomly across the world!"), True, Color.PaleGoldenrod)
        window.blit(text, (40, 70))
        text = font.render(str("Attack enemies using magic abilities and weapons. Use BP  to increment the amount of"), True, Color.PaleGoldenrod)
        
        window.blit(text, (40, 90))
        text = font.render(str("damage you deal!"), True, Color.PaleGoldenrod)
        window.blit(text, (40, 110))
        text = largefont.render("Storyline Help", True, Color.Black)
        window.blit(text, (40, 140))
        text_2 = font.render("", True, Color.PaleGoldenrod)
        if Globals.playerdata['storyline'] == 1:
            text = font.render("Try visiting the lake for help. There might be someone there who knows what to do", True, Color.White)
            location = font.render("Lake", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.1 or Globals.playerdata['storyline'] == 1.2:
            text = font.render("Maybe keep trying to talk to the old man in the house. He might have more to say", True, Color.White)
            location = font.render("Lake House", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.3:
            text = font.render("There's sure to be someone in Pol Town who knows what happened. Try talking to shady", True, Color.White)
            text_2 = font.render("people", True, Color.White)
            location = font.render("Pol Town", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.4:
            text = font.render("It seems that you found someone who knows something. Now you need to find a soothing", True, Color.White)
            text_2 = font.render("apple", True, Color.White)
            location = font.render("Pol Town", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.5:
            text = font.render("Return the soothing apple to the man in Pol Town", True, Color.White)
            location = font.render("Pol Town", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.6:
            text = font.render("You now know that the mercs went through the cave. You should hurry, they might still", True, Color.White)
            text_2 = font.render("be there", True, Color.White)
            location = font.render("Cave", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.7:
            text = font.render("Looks like they were guarding something. You should probably take a look", True, Color.White)
            location = font.render("Lake", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.8:
            text = font.render("Try talking to the merc you defeated. He's probably got the ring", True, Color.White)
            location = font.render("Lake", True, Color.Red)
        elif Globals.playerdata['storyline'] == 1.9:
            text = font.render("Head back to the old man's house, you have to return the ring", True, Color.White)
            location = font.render("Lake", True, Color.Red)
        elif Globals.playerdata['storyline'] == 2:
            text = font.render("It seems that there is more to discover. You should give the old man Polen a visit.", True, Color.White)
            text_2 = font.render("If you want, you don't have to... You seem to have a lot of time to kill", True, Color.White)
            location = font.render("Somerberry Village", True, Color.Red)
        window.blit(text, (40, 180))
        window.blit(text_2, (40, 200))
        window.blit(font.render("Storyline Location:", True, Color.Black), (400, 400))
        window.blit(location, (575, 400))
    elif Globals.scene == 'skill tree':
        
        y = 100
        Globals.idea_list = [["swords and polearms", "axes", "bows", "staves and magic", "shields"], 
                    ["knighthood", "double stance", "blood rage", "standard quiver", "critical eye", "stamina", "solid"],
                    ["health drain", "magic drain", "savagery", "large quiver", "weak-point", "even-weight", "parry"]]
        window.blit(font.render("SP: " + str(Globals.playerdata['skill points']), True, Color.White), (15, 30))
        for z in Globals.idea_list[0]:
            if Globals.playerdata['skills'][0][Globals.idea_list[0].index(z)] == True: sprite = unlocked
            else: sprite = locked
            j = len(Globals.idea_list[0])
            window.blit(symbols[Globals.idea_list[0].index(z)], (((700 / j) * Globals.idea_list[0].index(z) + 96), 2))
            window.blit(sprite, ((700 / j) * (Globals.idea_list[0].index(z) + 1) -48, y))
            if Globals.current_list == [0, Globals.idea_list[0].index(z)]: window.blit(ring_sel, ((700 / j) * (Globals.idea_list[0].index(z) + 1) -22, y+32))
        y +=135
        for z in Globals.idea_list[1]:
            if Globals.playerdata['skills'][1][Globals.idea_list[1].index(z)] == True: sprite = unlocked
            else: sprite = locked
            check = Globals.idea_list[1].index(z)
            if check == 0: x, stx, endx = 42, 140, 90
            elif check == 1: x, stx, endx = 142, 140, 190
            elif check == 2: x, stx, endx = 232, 280, 280
            elif check == 3: x, stx, endx = 322, 420, 370
            elif check == 4: x, stx, endx = 422, 420, 470
            elif check == 5: x, stx, endx = 512, 560, 560
            elif check == 6: x, stx, endx = 652, 700, 700   
            pygame.draw.line(window, Color.White, (stx, y-39), (endx, y))
            j = len(Globals.idea_list[0])
            window.blit(sprite, (x, y))
            if Globals.current_list == [1, Globals.idea_list[1].index(z)]: window.blit(ring_sel, (x + 26, y+32))
        y +=135
        for z in Globals.idea_list[2]:
            if Globals.playerdata['skills'][2][Globals.idea_list[2].index(z)] == True: sprite = unlocked
            else: sprite = locked
            check = Globals.idea_list[2].index(z)
            if check == 0: x = 42
            elif check == 1: x = 142
            elif check == 2: x = 232
            elif check == 3: x = 322
            elif check == 4: x = 422
            elif check == 5: x = 512
            elif check == 6: x = 652   
            pygame.draw.line(window, Color.White, (x + 48, y-39), (x + 48, y))
            j = len(Globals.idea_list[0])
            window.blit(sprite, (x, y))
            if Globals.current_list == [2, Globals.idea_list[2].index(z)]: window.blit(ring_sel, (x + 26, y+32))
        window.blit(pygame.transform.scale(cool_bg, (750, 150)), (20, 480))
        if Globals.fight_turn == "select":
            Globals.fight_currentmove = Globals.idea_list[Globals.current_list[0]][Globals.current_list[1]]
            
            text = font.render(Globals.fight_currentmove.capitalize(), True, Color.Red)
            window.blit(text, (70, 510))
            text = font.render(Globals.skill_info[Globals.fight_currentmove], True, Color.Black)
            window.blit(text, (85, 540))
            if Globals.playerdata['skills'][Globals.current_list[0]][Globals.current_list[1]]: text = font.render("You have already unlocked this", True, Color.White)
            else:
                if Globals.skill_class[Globals.current_list[0]][Globals.current_list[1]] == 2: text = font.render("Spend a skill point to unlock this", True, Color.Blue)
                else: text = font.render("Complete a mission to unlock this", True, Color.Red)
            window.blit(text, (450, 510))
        elif Globals.fight_turn == 'surity':
            window.blit(font.render("YES", True, Color.Black), (80, 540))
            window.blit(font.render("NO", True, Color.Black), (220, 540))
            window.blit(font.render("Are you sure you want to spend one skill point on unlocking " + Globals.prev_choice.capitalize(), True, Color.Black), (75, 500))
            if Globals.fight_currentmove == "yes": x = 130
            else: x = 270
            window.blit(ring_sel, (x, 540))
        elif Globals.fight_turn == 'rejection': window.blit(font.render("You have already unlocked this skill", True, Color.Black), (80, 520))
        elif Globals.fight_turn == 'reject': window.blit(font.render("You need to complete a special mission in order to unlock it", True, Color.Black), (80, 520))
        elif Globals.fight_turn == "unlock prior": window.blit(font.render("You need to unlock the skill prior", True, Color.Black), (80, 520))
        elif Globals.fight_turn == 'congrats': window.blit(font.render("You unlocked " + str(Globals.prev_choice.capitalize()), True, Color.Black), (80, 520))
        elif Globals.fight_turn == "not enough": window.blit(font.render("You need a skill point in order to unlock this", True, Color.Black), (80, 520))
    show_fps()
    
    if Globals.questart:
        text = superfont.render("Storyline Quest started!", True, Color.White)
        window.blit(text, (30, 30))
        text = largefont.render(str(Globals.playerdata['quests']) + "/2 storyline quests completed", True, Color.White)
        window.blit(text, (30, 100))
        
        johnnyboi += Globals.deltatime
        if johnnyboi >= 2:
            Globals.questart = False
            johnnyboi = False
    if Globals.questfinish:
        text = superfont.render("Storyline Quest completed!", True, Color.White)
        window.blit(text, (30, 30))
        text = largefont.render(str(Globals.playerdata['quests']) + "/2 storyline quests completed", True, Color.White)
        window.blit(text, (30, 100))
        text = superfont.render("Completed Chapter " + str(round(Globals.playerdata['storyline'] - 1, 1)), True, Color.Goldenrod)
        window.blit(text, (200, 250))
        johnnyboi += Globals.deltatime
        if johnnyboi >= 2:
            Globals.questfinish = False
            johnnyboi = 0
    if blitext:
        window.blit((specialtext), (350, 500))
        window.blit((specialtext2), (350, 530))
        johnnyboi += Globals.deltatime
        if johnnyboi >= 3:
            blitext = False
            johnnyboi = 0
    if shownthrow and Globals.scene == 'game':
        text = largefont.render(Globals.playerdata['location'].upper(), True, Color.White)
        window.blit(text, (0, 30))
        festive += Globals.deltatime
        if festive >= 2:
            shownthrow = False
            festive = 0
    if Globals.acceptsidequest:
        text = largefont.render("Side quest started!", True, Color.White)
        text2 = largefont.render(str(Globals.playerdata['sidequests']) + "/ 2", True, Color.White)
        text3 = largefont.render("You have " + str(len(Globals.playerdata['sidequest'])) + " active sidequests!", True, Color.White)
        window.blit(text, (40, 30))
        window.blit(text2, (40, 100))
        window.blit(text3, (40, 170))
        festive += Globals.deltatime
        if festive >= 2:
            Globals.acceptsidequest = False
            festive = 0
    elif Globals.finishsidequest:
        text = largefont.render("Side quest complete!", True, Color.White)
        text2 = largefont.render(str(Globals.playerdata['sidequests']) + "/ 2", True, Color.White)
        text3 = largefont.render("You have " + str(len(Globals.playerdata['sidequest'])) + " active sidequests!", True, Color.White)
        window.blit(text, (40, 30))
        window.blit(text2, (40, 100))
        window.blit(text3, (40, 170))
        festive += Globals.deltatime
        if festive >= 2:
            Globals.finishsidequest = False
            festive = 0


    pygame.display.update()

    clock.tick()

    count_fps()

    benefit_health = 0
    benefit_magic = 0
    maxhealth = Startup.healthchart[Globals.playerdata['level']] + 10
    maxmagic = Startup.manachart[Globals.playerdata['level']] + 3
    # Check if the player has skills unlocked?
    if Globals.playerdata['skills'][1][5]: maxmagic += math.ceil(maxmagic/20) # Stamina Skill + 5% Max Magic
    if Globals.playerdata['skills'][1][6]: maxhealth += math.ceil(maxhealth/20) # Solid Skill + 5% Max Health
    if Globals.playerdata['accessory'] == "Khar's Ring":
        benefit_health = 20
        benefit_magic = 10
    Globals.playerdata['maxhealth'] = maxhealth + benefit_health
    Globals.playerdata['maxmagic'] = maxmagic + benefit_magic
          
    # 40 + lvl(1) * sqrt(40 -20)) + 5    
    for enemy in Enemystats.enemies:
        if Globals.scaling:
                enemy.maxhealth = enemy.base_health + (Globals.playerdata['level'] * 5)
                enemy.damage = enemy.base_damage + Globals.playerdata['level']
        else:
            enemy.maxhealth = enemy.base_health
            enemy.damage = enemy.base_damage
    # check if you are on transferrable block

    # check if you are on transferrable block

    if Globals.playerdata['location'] == 'pol town':
        if Globals.camera_x <= -860 and Globals.camera_y <= -960:
            Map_Engine.open_new_map(True, 330, 230, 'cave', window, ring)
            shownthrow = True

        elif Globals.camera_x <= -165 and Globals.camera_x >= -178 and Globals.camera_y <= -132 and Globals.camera_y >= -164:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'villagehouse1', window, ring)
        elif Globals.camera_x <= - 162 and Globals.camera_x >= -184 and Globals.camera_y >= 2 and Globals.camera_y <= 34:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'villagehouse2', window, ring)
        elif Globals.camera_x <= -320 and Globals.camera_x >= -352 and Globals.camera_y >= 2 and Globals.camera_y <= 34:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'villagehouse3', window, ring)
        elif Globals.camera_x <= -320 and Globals.camera_x >= -352 and Globals.camera_y >= -164 and Globals.camera_y <= -132:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'villagehouse4', window, ring)
        elif Globals.camera_x <= -150 and Globals.camera_x >= -180 and Globals.camera_y <= -290 and Globals.camera_y >= -320:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'townstore', window, ring)
        elif Globals.camera_x <= -320 and Globals.camera_x >= -352 and Globals.camera_y <= -290 and Globals.camera_y >= -320:
            Map_Engine.open_new_map(False, Globals.camera_x, Globals.camera_y, 'villageinn', window, ring)
            Barkeep.x, Barkeep.y = 13 *32, 32
            Barkeep.tag = 'villageinn'
            Barkeep.dialog = [("You look new", ""), ("Don't listen to the rest of them. They're too drunk!", ""), ("So would you like a drink?", "Or do you want to room to sleep in?")]
        elif Globals.camera_x >= 330 and Globals.camera_y >= -893 and Globals.camera_y <= -873:
            Map_Engine.open_new_map(True, -1958, 250, 'lake', window, ring)
            shownthrow = True
        elif Globals.camera_x <= -475 and Globals.camera_y >= 100 and Globals.playerdata['lakemanquest'] == 'part3':
            Globals.camera_xmove, Globals.camera_ymove = False, False
            Globals.active_dialog = Dialog(merc3.dialog)
            Globals.dialog_open = True
            Globals.playerdata['lakemanquest'] = 'part4'
            merc3.dialog = [("Let's beat 'em to the pulp!", "")]
        elif Globals.camera_y >= 235 and Globals.camera_x >= 255  and Globals.camera_x <= 320:
            Map_Engine.open_new_map(True, -2430, -910, 'fields', window, ring)
            shownthrow = True
        elif Globals.camera_y >= 232 and Globals.camera_x >= -770 and Globals.camera_x <= -670:
            Map_Engine.open_new_map(True, 215, -1860, 'southern frontier', window, ring)
            shownthrow = True
        


    elif Globals.playerdata['location'] == 'cave':
        if Globals.camera_x >= 335 and Globals.camera_y >= 235:
            Map_Engine.open_new_map(True, -840, -940, 'pol town', window, ring)
            shownthrow = True
        elif Globals.camera_x >= 340 and Globals.camera_y >= -895 and Globals.camera_y <= -860:
            Map_Engine.open_new_map(True, -1920, -1855, 'lake', window, ring)
            shownthrow = True


    elif Globals.playerdata['location'] == 'villagehouse1' or Globals.playerdata['location'] == 'villagehouse2':

       if Globals.camera_x <= 148 and Globals.camera_y >= 140 and Globals.camera_y <= 160:
           Map_Engine.open_new_map(False, -246, -26, 'pol town', window, ring)
    elif Globals.playerdata['location'] == 'villagehouse3' or Globals.playerdata['location'] == 'villagehouse4':

        if Globals.camera_x >= 330 and Globals.camera_y >= 130 and Globals.camera_y <=160:
            Map_Engine.open_new_map(False, -246, -26, 'pol town', window, ring)          
    elif Globals.playerdata['location'] == 'townstore':
       if Globals.camera_x <= -205 and Globals.camera_y >= 172 and Globals.camera_y <= 182:
           Map_Engine.open_new_map(False, -230, -300, 'pol town', window, ring)
    elif Globals.playerdata['location'] == 'lake':
        if Globals.camera_x <= -1958 and Globals.camera_y >= 265:
            Map_Engine.open_new_map(True, 300, -880, 'pol town', window, ring)
            shownthrow = True
        elif Globals.camera_x <= -1638 and Globals.camera_y <= -806 and Globals.camera_y >= -826:
            Map_Engine.open_new_map(False, 330, 210, 'lakehouse', window, ring)
        elif Globals.camera_x <= -1945 and Globals.camera_y >= -1880 and Globals.camera_y <= -1848:
            Map_Engine.open_new_map(True, 300, -875, 'cave', window, ring)
            shownthrow = True
        elif Globals.camera_x >= -810 and Globals.camera_y >= 255 and Globals.camera_x <= -750:
            Map_Engine.open_new_map(True, 0, -900, 'fields', window, ring)
            shownthrow = True
    elif Globals.playerdata['location'] == 'villageinn':
        if Globals.camera_x >= 340 and Globals.camera_y >= 190 and Globals.camera_y <= 222:
            Map_Engine.open_new_map(False, -310, -310, 'pol town', window, ring)
            shownthrow = True
    elif Globals.playerdata['location'] == 'lakehouse':
        if Globals.camera_x >= 359 and Globals.camera_y >= 190 and Globals.camera_y <= 225:
            Map_Engine.open_new_map(False, -1600, -800, 'lake', window, ring)
    elif Globals.playerdata['location'] == 'fields':
        if Globals.camera_x <= 32 and Globals.camera_x >= -31 and Globals.camera_y <= -927 and Globals.camera_y >= -960:
            Map_Engine.open_new_map(True, -765, 230, 'lake', window, ring)
        elif Globals.camera_x <= -2410 and Globals.camera_x >= -2442 and Globals.camera_y <= -927 and Globals.camera_y >= -960:
            Map_Engine.open_new_map(True, 285, 220, 'pol town', window, ring)
        elif Globals.camera_x <= -2430 and Globals.camera_x >= -2462 and Globals.camera_y <= 230 and Globals.camera_y >= 161:
            Map_Engine.open_new_map(True, 300, -945, 'northern passage', window, ring)
    elif Globals.playerdata['location'] == 'southern frontier':
        if Globals.camera_x <= 250 and Globals.camera_x >= 186 and Globals.camera_y <= -1892:
            Map_Engine.open_new_map(True, -720, 200, 'pol town', window, ring)
        elif Globals.camera_x >= 350 and Globals.camera_y <= -102 and Globals.camera_y >= -170:
            Map_Engine.open_new_map(True, 0, -364, 'northern passage', window, ring)
        elif Globals.camera_x <= -930 and Globals.camera_y >= 100 and Globals.camera_x >= -1000 and  Globals.camera_y <= 140:
            Map_Engine.open_new_map(False, 140, -10, 'frontier market tent', window, ring)
        elif Globals.camera_x <= -1160 and Globals.camera_y >= -258 and Globals.camera_y <= -226:
            Map_Engine.open_new_map(False, 300, 80, 'lower crushtown', window, ring)
        elif Globals.camera_x <= -250 and Globals.camera_x >= -280 and Globals.camera_y >= 95 and Globals.camera_y <= 132:
            Map_Engine.open_new_map(False, 270, 210, "mercenary's tent", window, ring)
    elif Globals.playerdata['location'] == 'northern passage':
        if Globals.camera_x <= 340 and Globals.camera_x >= 310 and Globals.camera_y <= -930 and Globals.camera_y >= -962:
            Map_Engine.open_new_map(True, -2400, 200, 'fields', window, ring)
        elif Globals.camera_x <= -35 and Globals.camera_x >= -70 and Globals.camera_y <= -350 and Globals.camera_y >= -380:
            Map_Engine.open_new_map(True, 340, 80, 'southern frontier', window, ring)
        elif Globals.camera_x >= -18 and Globals.camera_x <= 18 and Globals.camera_y >= 262:
            Map_Engine.open_new_map(True, 49, -1557, 'southern somerberry', window, ring)
            shownthrow = True
    elif Globals.playerdata['location'] == 'southern somerberry' :
        if Globals.camera_x <= 63 and Globals.camera_x >= 31 and Globals.camera_y <= -1562:
            Map_Engine.open_new_map(True, 0, 240, 'northern passage', window, ring)
        elif Globals.camera_x <= -62 and Globals.camera_x >= -126 and Globals.camera_y >= 260:
            Map_Engine.open_new_map(False, -32, -590, 'somerberry barracks', window, ring)
        elif Globals.camera_x <= -62 and Globals.camera_x >= -126 and Globals.camera_y >= -821 and Globals.camera_y <= -770:
            Map_Engine.open_new_map(False, 140, -10, 'somerberry store', window, ring)
        elif Globals.camera_x <= -62 and Globals.camera_x >= -126 and Globals.camera_y >= -1000 and Globals.camera_y <= -968:
            Map_Engine.open_new_map(False, 140, 200, 'somerberry inn', window, ring)
            Barkeep.x, Barkeep.y = 2 * 32, 10 * 32
            Barkeep.tag = 'somerberry inn'
            if int(Globals.playerdata['guards_somerquest'].split("t")[1]) <= 12:
                Barkeep.dialog = [("Times are tough...", ""), ("Taxes are high, so prices are high too...", ""), ("I can give you a room for 100 flat, no less", "")]
            else: Barkeep.dialog = [("Well the taxes are gone!", ""), ("Fancy a room for 50 gold?", ""), ("Or a drink?", "")]
    elif Globals.playerdata['location'] == 'somerberry barracks':
        if Globals.camera_x <= 0 and Globals.camera_x >= -64 and Globals.camera_y <=-600:
            Map_Engine.open_new_map(False, -94, 230, 'southern somerberry', window, ring)
        elif Globals.camera_x <= 0 and Globals.camera_x >= -64 and Globals.camera_y >= -120 and Globals.camera_y <=-60:
            Map_Engine.open_new_map(True, 96, -900, 'somerberry barracks entry', window, ring)
        elif Globals.camera_x <= -328 and Globals.camera_y <= 128 and Globals.camera_y >= 96:
            Map_Engine.open_new_map(True, 296, 200, 'somerberry barrack corridor', window, ring)
        elif Globals.camera_x >= 255 and Globals.camera_y <= 128 and Globals.camera_y >= 96:
            Map_Engine.open_new_map(True, -10, 200, 'barrack puzzle room', window, ring)
    elif Globals.playerdata['location'] == 'somerberry barracks entry':
        if Globals.camera_x <= 126 and Globals.camera_x >= 62 and Globals.camera_y <= -916:
            Map_Engine.open_new_map(True, -32, -140, 'somerberry barracks', window, ring)
        elif Globals.camera_x <= 32 and Globals.camera_y >= -60 and Globals.camera_y <= -30:
            Map_Engine.open_new_map(False, 330, 200, 'west barrack wing', window, ring)
        elif Globals.camera_x >= 160 and Globals.camera_y <= 155 and Globals.camera_y >= 120:
            Map_Engine.open_new_map(False, -120, 130, 'east barrack wing', window, ring)
        elif Globals.camera_x <= 126 and Globals.camera_x >= 62 and Globals.camera_y >= 225:
            if Globals.playerdata['guards_somerquest'] == "part6":
                Globals.camera_y = 200
                if "Dungeon Key" in Globals.playerdata['key items']:
                    Globals.active_dialog = Dialog([("The door is locked...", ""), ("But you opened it with the Dungeon Key!", "")])
                    Globals.playerdata['guards_somerquest'] = 'part7'
                else:
                    Globals.active_dialog = Dialog([("The door is locked...", ""), ("You need to find a key!", "")])
                Globals.dialog_open = True
            else:
                Map_Engine.open_new_map(False, 60, -270, 'somerberry barracks dungeon', window, ring)
    elif Globals.playerdata['location'] == 'west barrack wing': 
        if Globals.camera_x >= 348 and Globals.camera_y >= 200:
            Map_Engine.open_new_map(False, 40, -45, 'somerberry barracks entry', window, ring)
    elif Globals.playerdata['location'] == 'east barrack wing': 
        if Globals.camera_x <= -130 and Globals.camera_y >= 118 and Globals.camera_y <= 150:
            Map_Engine.open_new_map(False, 100, 150, 'somerberry barracks entry', window, ring)
    elif Globals.playerdata['location'] == 'somerberry barracks dungeon': 
        if Globals.camera_x <= 92 and Globals.camera_x >= 28 and Globals.camera_y <= -284:
            Map_Engine.open_new_map(False, 96, 220, 'somerberry barracks entry', window, ring)
        elif Globals.camera_x >= 250 and Globals.camera_y <= 282 and Globals.camera_y >= 224:
            Map_Engine.open_new_map(False, -78, -110, 'barrack chamber', window, ring)
    elif Globals.playerdata['location'] == 'barrack chamber':
        if Globals.playerdata['guards_somerquest'] == "part9":
            if Globals.camera_y >= 40:
                Globals.active_dialog.text = commanderKnok.dialog
                Globals.dialog_open = True
                Globals.playerdata['guards_somerquest'] = 'part10'
                Globals.camera_y = 120
                Globals.camera_xmove = False
                Globals.camera_ymove =False
                pygame.mixer.music.load("music\\Commander_Knok.mp3")
                pygame.mixer.music.play(-1)
        if Globals.camera_x >= -96 and Globals.camera_x <= -62 and Globals.camera_y <= -125:
            Map_Engine.open_new_map(False, 266, -200, 'somerberry barracks dungeon', window, ring)
        elif Globals.camera_x <= -200 and Globals.camera_y <= -120:
            Map_Engine.open_new_map(False, 238, 220, 'somerberry barrack corridor', window, ring)
    elif Globals.playerdata['location'] == 'somerberry barrack corridor':
        if Globals.camera_x >= 225 and Globals.camera_x <= 250 and Globals.camera_y >= 225:
            Map_Engine.open_new_map(False, -216, -100, 'barrack chamber', window, ring)
        elif Globals.camera_x >= 270 and Globals.camera_y >= 225:
            Map_Engine.open_new_map(True, -280, 108, 'somerberry barracks', window, ring)
        elif Globals.camera_x <= 230 and Globals.camera_x >= 200 and Globals.camera_y <= -220: 
            Map_Engine.open_new_map(True, -330, -126, 'somerberry barracks', window, ring)    
    elif Globals.playerdata['location'] == 'barrack puzzle room':
        if Globals.camera_x <= -37 and Globals.camera_y >= 194:
            Map_Engine.open_new_map(True, 230, 110, 'somerberry barracks', window, ring)
    elif Globals.playerdata['location'] == 'somerberry store':
        if Globals.camera_x <= 160 and Globals.camera_x >= 128 and Globals.camera_y <= -32:
            Map_Engine.open_new_map(False, -30, -820, 'southern somerberry', window, ring)
    elif Globals.playerdata['location'] == 'somerberry inn':
        if Globals.camera_x <= 161 and Globals.camera_x >= 120 and Globals.camera_y >= 220:
            Map_Engine.open_new_map(False, -980, -30, 'southern somerberry', window, ring)
    elif Globals.playerdata['location'] == 'frontier market tent':
        if Globals.camera_x >= 125 and Globals.camera_x <= 160 and Globals.camera_y <= -32:
            Map_Engine.open_new_map(False, -960, 80, 'southern frontier', window, ring)
    elif Globals.playerdata['location'] == 'lower crushtown':
        if Globals.camera_x >= 332 and Globals.camera_y >= 63 and Globals.camera_y <= 98:
            Map_Engine.open_new_map(False, -1100, -240, 'southern frontier', window, ring)
    elif Globals.playerdata['location'] == "mercenary's tent":
        if Globals.camera_x >= 250 and Globals.camera_x <= 290 and Globals.camera_y <= 188:
            Map_Engine.open_new_map(False, -260, 80, 'southern frontier', window, ring)
print(Globals.camera_x)
print(Globals.camera_y)


pygame.quit()
sys.exit()
