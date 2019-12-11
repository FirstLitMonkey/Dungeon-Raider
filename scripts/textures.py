import pygame
from scripts.globals import *


pygame.init()

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky
dialog_background = pygame.image.load("graphics\\gui\\text_bg.png")
Dialog_background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
Dialog_background.blit(dialog_background, (0, 0))
Dialog_background_width, Dialog_background_height = Dialog_background.get_size()
del dialog_background
# Chest Sprites
gold_chest1 = pygame.image.load("graphics\\Immobile\\Chests\\gold_chest1.png")
gold_chest2 = pygame.image.load("graphics\\Immobile\\Chests\\gold_chest2.png")
gold_chest = [gold_chest1, gold_chest2]
del gold_chest1, gold_chest2
# Door Sprites
locked_door = pygame.image.load("graphics\\Immobile\\locked_jail_door.png")

# Slab Sprites
buttonImg = pygame.image.load("graphics\\Immobile\\button.png")
slabImg = pygame.image.load("graphics\\Immobile\\slab.png")


text_background = pygame.image.load("graphics\\gui\\cool_bg.png")


sign_img = pygame.image.load("graphics\\Tiles\\sign.png")
# Skill Tree Sprites
locked = pygame.transform.scale(pygame.image.load("graphics\\Immobile\\locked.png"), (96, 96))
unlocked = pygame.transform.scale(pygame.image.load("graphics\\Immobile\\unlocked.png"), (96, 96))
symbols = [pygame.transform.scale(pygame.image.load('graphics\\Immobile\\sword_pole.png'), (96, 96)),
    pygame.transform.scale(pygame.image.load('graphics\\Immobile\\axe.png'), (96, 96)),
    pygame.transform.scale(pygame.image.load('graphics\\Immobile\\bows.png'), (96, 96)),
    pygame.transform.scale(pygame.image.load('graphics\\Immobile\\scroll.png'), (96, 96)), 
    pygame.transform.scale(pygame.image.load('graphics\\Immobile\\shield.png'), (96, 96))]
ring_sel = pygame.image.load('graphics\\ring_select.png')
# Hanging Sign Sprites
hang_sign = pygame.image.load("graphics\\Tiles\\hang_sign.png")
inn_sign = pygame.image.load("graphics\\Tiles\\inn_sign.png")
shop_sign = pygame.image.load("graphics\\Tiles\\shop_sign.png")
weap_sign = pygame.image.load("graphics\\Tiles\\weap_sign.png")
# Tree Sprites
tree_img = pygame.image.load("graphics\\Tiles\\plants\\tree.png")


class Tiles:
    Size = 32


    Blocked = []

    Blocked_Types = ["3", "4", "5", '9', '10', '12', '13', '14',
                     '15', '16','20', '21', '22', '23', '24', '25',
                     '26', '27', '28', '29', '30', '31', '32', '34', '37',
                     '38', '39', '40', '41', '42', '44', '46', '47', '48',
                     '49', '50', '51', '52', '53', '54', '55', '56', '58',
                     '60', '61', '62', '64', '65', '66', '67', '68', '70'
                     ]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False




        
    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    Grass = Load_Texture("graphics\\Tiles\\plants\\grass.png", Size)

    Stone = Load_Texture("graphics\\Tiles\\stone.png", Size)

    Water = Load_Texture("graphics\Tiles\\plants\\water.png", Size)

    SkyB = Load_Texture("graphics\\Tiles\\block_sky.png", Size)

    FenceG = Load_Texture("graphics\\Tiles\\plants\\grass_fence.png", Size)

    NorthEntry = Load_Texture ("graphics\\Tiles\\entrance.png", Size)

    SouthEntry = pygame.transform.rotate(NorthEntry, 180)

    EastEntry = pygame.transform.rotate(NorthEntry, 90)

    WestEntry = pygame.transform.rotate(NorthEntry, 270)

    Table2 = Load_Texture("graphics\\Tiles\\table2.png", Size)

    Southwater = Load_Texture("graphics\\Tiles\\plants\\water_edge_s.png", Size)

    Northwater = Load_Texture("graphics\\Tiles\\plants\\water_edge_n.png", Size)

    Eastwater = Load_Texture("graphics\\Tiles\\plants\\water_edge_e.png", Size)

    Westwater = Load_Texture("graphics\\Tiles\\plants\\water_edge_w.png", Size)

    Roof = Load_Texture("graphics\\Tiles\\roof_piece.png", Size)

    HouseStairs = Load_Texture("graphics\\Tiles\\house_stairs.png", Size)

    Housefloor = Load_Texture("graphics\\Tiles\\woodenfloor.png", Size)

    HouseTable = Load_Texture("graphics\\Tiles\\table.png", Size)

    Houseplant = Load_Texture("graphics\\Tiles\\woodenplant.png", Size)

    housetablen = Load_Texture("graphics\\Tiles\\cornertablen.png", Size)

    housetablee = Load_Texture("graphics\\Tiles\\cornertablee.png", Size)
    housetables = Load_Texture("graphics\\Tiles\\cornertables.png", Size)
    housetablew = Load_Texture("graphics\\Tiles\\cornertablew.png", Size)
    
    house_stone_wall = Load_Texture("graphics\\Tiles\\stonewall.png", Size)
    
    stone_roof = Load_Texture("graphics\\Tiles\\stone_roof.png", Size)
    
    wood_roof = Load_Texture("graphics\\Tiles\\wood_roof.png", Size)
    
    wood_roof2 = Load_Texture("graphics\\Tiles\\wood_roof2.png", Size)
    
    blank_stone_wall_side = Load_Texture("graphics\\Tiles\\blank_stone_wall.png", Size)
    blankflip_stone_wall_side = pygame.transform.rotate(blank_stone_wall_side, 180)
    grass_stone_wall_side = Load_Texture("graphics\\Tiles\\plants\\grass_stone_wall.png", Size)
    grassflip_stone_wall_side = pygame.transform.rotate(grass_stone_wall_side, 180)
    stone_cliff = Load_Texture("graphics\\Tiles\\rock_cliff.png", Size)
    stone_path = Load_Texture("graphics\\Tiles\\rock_path.png", Size)
    stone_stairs = Load_Texture("graphics\\Tiles\\stone_stairs.png", Size)
    Stone_path = Load_Texture("graphics\\Tiles\\stone_path.png", Size)

    Stone_cliff = Load_Texture("graphics\\Tiles\\stone_cliff.png", Size)

    Rock_stairs = Load_Texture("graphics\\Tiles\\stairs_rocks.png", Size)

    platform = Load_Texture("graphics\\Tiles\\platform.png", Size)

    top_water_bridge = Load_Texture("graphics\\Tiles\\plants\\top_water_bridge.png", Size)

    bottom_water_bridge = Load_Texture("graphics\\Tiles\\plants\\bottom_water_bridge.png", Size)

    fenced_left = Load_Texture("graphics\\Tiles\\plants\\fence_end_left.png", Size)

    fenced_right = Load_Texture("graphics\\Tiles\\plants\\fence_end_right.png", Size)

    grass_fence_straight = Load_Texture("graphics\\Tiles\\plants\\grass_fence_straight.png", Size)
    
    
    stone_cliff_loop = Load_Texture("graphics\\Tiles\\rock_cliff_loop.png", Size)

    left_wooden_door = Load_Texture("graphics\\Tiles\\left_door.png", Size)
    right_wooden_door = Load_Texture("graphics\\Tiles\\right_door.png", Size)
    # Guards and Castles of the Land
    bars = Load_Texture("graphics\\Tiles\\some_tiles.jpg", Size)
    sewer_stairs = Load_Texture("graphics\\Tiles\\sewer_stairs.png", Size)
    castle_ledge = Load_Texture("graphics\\Tiles\\castle_ledge.png", Size)
    castle_ledge_path = Load_Texture("graphics\\Tiles\\castle_ledge_path.png", Size)
    castle_table = Load_Texture("graphics\\Tiles\\castle_path_table.png", Size)
    castle_ledge_l = Load_Texture("graphics\\Tiles\\castle_ledge_blocked_l.png", Size)
    castle_ledge_r = Load_Texture("graphics\\Tiles\\castle_ledge_blocked_r.png", Size)
    castle_jail_door = Load_Texture("graphics\\Tiles\\castle_bar_door.png", Size)
    # Tent
    tent_top = Load_Texture("graphics\\Tiles\\tent\\top.png", Size)
    tent_corner = Load_Texture("graphics\\Tiles\\tent\\tent_topleft.png", Size)
    tent_middle = Load_Texture("graphics\\Tiles\\tent\\tent_midleft.png", Size)
    tent_bottom = Load_Texture("graphics\\Tiles\\tent\\tent_botleft.png", Size)
    tent_cornerr = Load_Texture("graphics\\Tiles\\tent\\tent_topright.png", Size)
    tent_middler = Load_Texture("graphics\\Tiles\\tent\\tent_midright.png", Size)
    tent_bottomr = Load_Texture("graphics\\Tiles\\tent\\tent_botright.png", Size)
    tent_entrance = Load_Texture("graphics\\Tiles\\tent\\entrance.png", Size)
    tent_mid = Load_Texture("graphics\\Tiles\\tent\\middle.png", Size)
    tent_grass = Load_Texture("graphics\\Tiles\\tent\\grass.png", Size)
    grass_bush = Load_Texture("graphics\\Tiles\\plants\\grass_bush.png", Size)
    tent_floor = Load_Texture("graphics\\Tiles\\tent\\floor.png", Size)
    closed_entrance = Load_Texture("graphics\\Tiles\\tent\\closed.png", Size)
    # Plants, Trees & other enviromental tiles
    tree001 = Load_Texture("graphics\\Tiles\\plants\\bottom_tree1.png", Size)
    tree002 = Load_Texture("graphics\\Tiles\\plants\\top_tree1.png", Size)
    flowers = Load_Texture("graphics\\Tiles\\plants\\flowers.png", Size)
    tree003 = Load_Texture("graphics\\Tiles\\plants\\tree001.png", Size)
    tree004 = Load_Texture("graphics\\Tiles\\plants\\tree002.png", Size)
    tree005 = Load_Texture("graphics\\Tiles\\plants\\tree003.png", Size)
    tree006 = Load_Texture("graphics\\Tiles\\plants\\tree004.png", Size)
    stacked_logs = Load_Texture("graphics\\Tiles\\plants\\stacked_logs.png", Size)

    

    


    Texture_Tags = {"1" : Grass, "2" : Stone,
                    "3" : Water, "4" : SkyB, "5" : FenceG,
                    "6" : NorthEntry, "7" : SouthEntry,
                    "8" : EastEntry, "9" : WestEntry,
                    "9" : Table2, "10" : stone_cliff,
                    "11" : stone_path, "12" : grass_fence_straight,
                    '13' : Southwater, '14' : Northwater,
                    '15' : Eastwater, '16' : Westwater,
                    '17' : Stone_path, '18' : HouseStairs,
                    '19' : Housefloor, '20' : HouseTable,
                    '21' : Houseplant, '22' : housetablen,
                    '23' : housetablee, '24' : housetables,
                    '25' : housetablew, '26' : house_stone_wall,
                    '27' : stone_roof, "28" : wood_roof,
                    '29' : wood_roof2, '30' : blank_stone_wall_side,
                    '31' : grass_stone_wall_side, '32' : grassflip_stone_wall_side,
                    '33' : blankflip_stone_wall_side, '34' : Stone_cliff,
                    '35' : Rock_stairs, '36' : platform,
                    '37' : fenced_left, '38' : fenced_right,
                    '39' : stone_cliff_loop, '40' : left_wooden_door,
                    '41' : right_wooden_door, '42' : bars,
                    '43' : sewer_stairs, '44' : castle_ledge,
                    '45' : castle_ledge_path, '46' : castle_table,
                    '47' : castle_ledge_l, '48' : castle_ledge_r,
                    '49' : castle_jail_door, '50' : tent_top,
                    '51' : tent_corner, '52' : tent_cornerr,
                    '53' : tent_middle, '54' : tent_middler,
                    '55' : tent_bottom, '56' : tent_bottomr,
                    '57' : tent_entrance, '58' : tent_mid, 
                    '59' : tent_grass, '60' : grass_bush,
                    '61' : tree001, '62' : tree002,
                    '63' : flowers, '64' : tree003,
                    '65' : tree004, '66' : tree005,
                    '67' : tree006, '68' : stacked_logs,
                    '69' : tent_floor, '70': closed_entrance,
                    
                    }



class chests():

    Allchests = []
    
    def __init__(self, pos, tag, number, rewards=[30, 'gold']):
        self.x = pos[0] * 32
        self.y = pos[1] * 32
        self.tag = tag
        self.number = number
        self.rewards = rewards

        chests.Allchests.append(self)

    def chest_open(chest):
        if Globals.playerdata['chests'][chest.number]:
            Globals.active_dialog = Dialog([("You have already opened this!", "There is nothing else in here!")])
            Globals.dialog_open = True
            Globals.chest_offcut = True
        else:
            if chest.rewards[1] == 'gold':
                Globals.playerdata['gold'] += chest.rewards[0]
                Globals.active_dialog = Dialog([("You found:", str(chest.rewards[0]) + " gold!")])
            elif chest.rewards[1] in Globals.items:
                Globals.playerdata[chest.rewards[1]] += chest.rewards[0]
                Globals.active_dialog = Dialog([("You found:", str(chest.rewards[0]) + " " + str(chest.rewards[1]))])
            elif chest.rewards[1] == 'weapon':
                Globals.playerdata['ownweapons'].append(chest.rewards[0])
                Globals.playerdata['curweap'] = chest.rewards[0]
                Globals.active_dialog = Dialog([("You found a ", str(chest.rewards[0])), (str(Globals.itemdescrip[chest.rewards[0]]), "")])
            elif chest.rewards[1] == 'shield':
                Globals.playerdata['ownshield'].append(chest.rewards[0])
                Globals.playerdata['curshield'] = chest.rewards[0]
                Globals.active_dialog = Dialog([("You found a ", str(chest.rewards[0])), (str(Globals.itemdescrip[chest.rewards[0]]), "")])
            elif chest.rewards[1] == 'key item':
                Globals.playerdata['key items'].append(chest.rewards[0])
                Globals.active_dialog = Dialog([("You found a ", str(chest.rewards[0])), (str(Globals.itemdescrip[chest.rewards[0]]), "")])
                if Globals.playerdata['poltowninnquest'] == 'part2' and chest.rewards[0] == "Bottle of Whiskey": Globals.playerdata['poltowninnquest'] = 'part3'
            Globals.active_dialog.page = 0
            Globals.dialog_open = True
            Globals.chest_offcut = True
            Globals.playerdata['chests'][chest.number] = True

class signs():

    Allsigns = []
    
    def __init__(self, pos, tag, info=[('Generic Information', '')]):
        self.x = pos[0] * 32
        self.y = pos[1] * 32
        self.tag = tag
        self.info = info

        signs.Allsigns.append(self)

    def sign_open(sign):
        Globals.active_dialog = Dialog(sign.info)
        Globals.dialog_open = True
        Globals.active_dialog.page = 0
        


class hangingsigns():

    Allsigns = []
    
    def __init__(self, pos, tag, image=hang_sign):
        self.x = pos[0] * 32
        self.y = pos[1] * 32
        self.tag = tag
        self.img = image

        hangingsigns.Allsigns.append(self)


class trees():

    Alltrees = []
    
    def __init__(self, pos, tag):
        self.x = (pos[0] * 32) #+ 20 
        self.y = (pos[1] * 32) #+ 96
        self.tag = tag

        trees.Alltrees.append(self)
from scripts.map_engine import Map_Engine
class doors():

    Alldoors = []
    
    def __init__(self, pos, tag, key, map_name):
        self.x = pos[0] * 32
        self.y = pos[1] * 32
        self.tag = tag
        self.key = key
        self.map = map_name
        doors.Alldoors.append(self)

    def door_open(door):
        if door.key in Globals.playerdata['key items']:
            door.x, door.y = -100, -100
            Globals.active_dialog = Dialog([("You opened the locked door with the", door.key)])
            
        else:
            Globals.active_dialog = Dialog([("The door is locked tight!", ""), ("You need to find a key", "")])
        Globals.active_dialog.page = 0
        Globals.dialog_open = True

class slabs():

    Allslabs = []
    
    def __init__(self, pos, tag, button_pos, btag, map_name):
        self.x = pos[0] * 32
        self.y = pos[1] * 32
        self.tag = tag
        self.butx = button_pos[0] * 32
        self.buty = button_pos[1] * 32
        self.previous_locale = pos
        self.but_tag = btag
        self.map = map_name
        self.locale = True
        slabs.Allslabs.append(self)

    def open_button(button):
        if button.locale:
            button.x = -100
            button.y = -100
            Globals.active_dialog = Dialog([("A door opened somewhere!", "")])
            Globals.active_dialog.page = 0
            Globals.dialog_open = True
        else:
            button.x = button.previous_locale[0] * 32
            button.y = button.previous_locale[1] * 32
            Globals.active_dialog = Dialog([("A door closed somewhere!", "")])
            Globals.active_dialog.page = 0
            Globals.dialog_open = True
        button.locale = not button.locale
