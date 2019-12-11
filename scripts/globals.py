import pygame

class Globals:
    play_music = True
    cooldown_counter_spec = 4
    cooldown_counter_ulti = 1
    ultimate_activated = False
    special_activated = False
    start_of_battle = False
    poisoned_player = False
    poisoned_enemy = False
    stunned = False
    repeat = False
    actions = {'action1' : pygame.K_z,
               'cancel' : pygame.K_x,
               'pause' : pygame.K_ESCAPE,
               'run' : pygame.K_LSHIFT}
    filename = 'nil'
    event = 'main'
    camera_x = 0
    camera_y = 0
    camera_ymove = 0
    camera_xmove = 0
    scene = "menu"
    fight_turn = 'player'
    fight_move = False
    fight_count = 0
    deltatime = 0
    npcname = ''
    data = "zip"
    data1 = 'zilch'
    data2 = 'love'
    chest_offcut = False
    win = False
    dialog_open = False
    active_dialog = None
    fight_currentmove = 'attack'
    storyline_fight = False
    enemy_switch = 0
    acceptsidequest = False
    sidequest = []
    idea_list = ['attack', 'magic', 'item', 'run']
    anime_turn = 1
    current_list = 0
    switch = True
    playerdata = {'name' : 'NEW', 'gold' : 50,
                  'realm' : 'normal',
                  'location' : 'pol town',
                  'health' : 120, 'maxhealth' : 120,
                  'cavequest1' : 'part 1',
                  'FPS' : False, 'Music_volume' : 0.5,
                  'chests' : [False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, 
                              False, False, False, False, False, False, False,
                              ],
                  'sidequest' : [],
    
                  
                  'curweap' : 'Rusty Sword',
                  'ownspells' : ["Heavy Sword Strike",
                                 'Fireball'
                                 ],
                  'magic' : 43,
                  'maxmagic' : 43,
                  'soothing apples' : 3, 'magic jam' : 3, 'fruit jam' : 0, 'mushed berries' : 0,
                  'items': ['magic jam', 'soothing apples'],
                  'experience' : 0,
                  "level" : 1,
                  'xpcap' : 7,
                  'ownweapons' : ['Rusty Sword'],
                  'curshield' : 'Half a shield',
                  'ownshield' : ['Half a shield'],
                  'storyline' : 1,
                  'energy' : 1,
                  'maxenergy' : 1,
                  'quests' : 0,
                  'sidequests' : 0,
                  'accessories' : ['None'],
                  'accessory' : 'None',
                  'lakemanquest' : 'part1',
                  'poltowninnquest' : 'part1',
                  'preloca' : [-258, 152],
                  'key items' : ['Wooden Ring', 'Logbook'],
                  'mapinpoltown' : 'start',
                  'discovered locations' : ['pol town'],
                  'test_query' : False,
                  'merc1_death' : False,
                  'michael_quests' : 0.0,
                  'michael_refusal' : False,
                  'gideon_quests' : 0.0,
                  'cutscenes' : {"guard greet somerberry" : 0.0},
                  'guards_somerquest' : "part1",
                  'guards_somer_killed' : False,
                  'little_lost_bear' : "part1",
                  'skills' : [[True, False, False, True, True], [False, False, False, False, False, False, False], 
                  [False, False, False, False, False, False, False]],
                  'skill points' : 0,
                  

                  
                  
                  }
    music = { "southern somerberry":"music\\somerberry_village.mp3", "northern passage":"music\\our_mountain.mp3", 
        "fields":"music\\our_mountain.mp3", "lake":"music\\Realm-of-Fantasy_Looping.mp3","lakehouse":"music\\Realm-of-Fantasy_Looping.mp3",
        "lakehouse":"music\\Realm-of-Fantasy_Looping.mp3", "cave":"music\\Evil_Guard.mp3", "southern frontier":"music\\bosstheme.mp3", 
        "pol town":"music\\mountain_peak.mp3", 'villagehouse1':"music\\mountain_peak.mp3", 'villagehouse2':"music\\mountain_peak.mp3", 'villagehouse3':"music\\mountain_peak.mp3", 'villagehouse4':"music\\mountain_peak.mp3", 'villageinn':"music\\mountain_peak.mp3", 'townstore':"music\\mountain_peak.mp3",
        'somerberry barracks':"music\\somerberry_village.mp3","somerberry barracks entry": "music\\storming_the_barracks.mp3", "east barrack wing": "music\\storming_the_barracks.mp3", "west barrack wing": "music\\storming_the_barracks.mp3",
        'somerberry barracks dungeon':"music\\storming_the_barracks.mp3", "somerberry barrack corridor":"music\\storming_the_barracks.mp3", "barrack chamber":"music\\storming_the_barracks.mp3", "barrack puzzle room": "music\\storming_the_barracks.mp3",
        "somerberry store":"music\\somerberry_village.mp3", "somerberry inn":"music\\somerberry_village.mp3",  "frontier market tent":"music\\bosstheme.mp3",
        "lower crushtown":"music\\bosstheme.mp3", "mercenary's tent":"music\\bosstheme.mp3"                  
                 
                 
                 
                  }
    Healing = 0
    Magic = 0
    storelist = {'townstore' : ['soothing apples', 'magic jam', "mushed berries"],
                 'somerberry store' : ['soothing apples', 'magic jam', 'fruit jam'],
                 'frontier market tent' : ['soothing apples', 'magic jam', "mushed berries"],

                 }
    items = ['soothing apples', 'magic jam', 'fruit jam']
    itemdescrip = {'magic jam' : "Recover a low amount of magic energy!",
                   'soothing apples' : 'Recover a low amount of health!',
                   "Khar's Ring" : 'Belonged to Khar. Gain +10 magic and +20 health!',
                   "Wooden Ring" : "This is your childhood ring from your  mother!",
                   "Sharp Sword" : "You can tell a mercenary sharpened its edge! 11-14 dmg",
                   "Rusty Sword" : "It's not very optimal since its covered with rust! 5-6 dmg",
                   "Wooden Spear" : "This is stock standard for any villager! 7-9 dmg",
                   "None" : "You don't have any!",
                   "Half a shield" : "We don't know where the other half is",
                   "Wooden Shield" : "Made from sturdy blackwood",
                   "Return to Menu" : "Simple. Return to Menu",
                   "Bottle of Whiskey" : "Too bad it's empty. Maybe someone is missing it!",
                   "Iron Dagger" : "It's embroidered with gems! 13-14 dmg",
                   "Southern Map" : "It's a highly detailed map of the south",
                   "Logbook" : "Keep up to date with your quests across the country!",
                   "Dungeon Key" : "This key opens the dungeon in Somerberry Barracks",
                   "Welded Sword" : "Made from scraps, its damage has high  variance",
                   "Welded Shield" : "Made from scraps, its defence has high  variance",
                   "Fluffy Bear" : "A Fluffy Bear. It has stains of blood",
                   "Treasure Room Key" : "This key opens the treasure room in the Barracks",
                   "Mercenary's Sword" : "This blade is rough, easy to cut. 12-15 dmg",
                   "Iron-Tipped Spear" : "The iron point can tear through flesh. 16-19 dmg",
                   "Barrack Chest Key" : "This key opens a door, which leads to treasure...",
                   "fruit jam" : "Recover a low amount of magic and health!",
                   "Woodcutter's Axe": "This axe is strong but unwieldy. 12-14 dmg",
                   'mushed berries' : "Recover a small amount of health"
                   
                   
                   }
    enemyLocation = {'lake' : 2400,
                     'cave' : 1200,
                     'fields' : 1500,
                     'southern frontier' : 1200,
                     'northern passage' : 1400}
    itemcost = {"magic jam" : 30,
                "soothing apples" : 20,
                "fruit jam" : 50,
                "mushed berries" : 10,
                }
    poltowninnquest_details = {"part1" : "No Show",
                               'part2' : ("You agreed to help a man find his lost bottle of whiskey", "He said he lost it in the fields"),
                               'part3' : ("You found the bottle in the fields! You should return it!", ""),
                               'finished' : ("A man in the pol town inn asked you to find his lost", "bottle of whiskey and you found it in the fields")
                               }
    lakemanquest_details = {"part2" : "You spoke to a mercenary of her problems - Find out more!"}
    guards_somerquest = {1 : "No Show",
                        2 : ("The guards of somerberry are corrupt", "You heard from one of their victims that Commander Knok", "is charge of them - You should investigate the Somerberry Barracks"),
                        3 : ("You managed to get past the guards at the front of the", "barracks", ""),
                        4 : ("You defeated multiple guards inside the barracks", "", ""),
                        7 : ("You used the Dungeon Key to open the dungeon doors", "", ""),
                        8 : ("You defeated the torturer - destroying his rein of", "killing", ""),
                        }


    little_lost_bear_details = {"part1" : "No Show",
                                "part2" : ("A guard in somerberry barracks is missing a child's bear", ""),
                                "part3" : ("You found the bear in the torture room of the dungeon", "Return it to the guard in the Barracks"),
                                "finished" : ("You found a bear in a torture room and returned it", "to the guard. He gave you the Treasure Room Key")}

    xpcap = [5, 7, 8, 10, 12, 14, 17, 19, 22, 24, 26, 29, 31, 33]
    chapter1 = {1.1: "You spoke to an old man",
                1.2: "He offered to pay you money",
                1.3: "He wants his ring back. He suggests going to Pol Town",
                1.4: "Someone knows something. Get them a soothing apple",
                1.5: "You found a soothing apple",
                1.6: "You finally found out they there is mercenaries in the cave",
                1.7: "The mercenary didn't have the ring but was blocking something",
                1.8: "You managed to defeat the leader. But you still don't have it",
                1.9: "You got the ring after dealing with the mercenary",
                2.0: "Seems like the old man didn't want it. He gave it straight back",
                }
    skill_info = {"swords and polearms" : "Can use swords and spears", "axes" : "Can use axes", "bows" : "Can use bow with 20 arrow quiver", "staves and magic" : "can use staves and magic", "shields" : "Can use shields", 
                    "knighthood" : "Deal 25% more damage with swords and spears", "double stance" : "25% Chance to attack again with swords and spears", "blood rage" : "Deal 100% more damage to enemies with low health", "standard quiver" : "Hold up to 50 arrows", "critical eye" : "20% Chance to critical hit when using a bow", "stamina" : "+5% Max Magic", "solid" : "+5% Max Health",
                    "health drain" : "Health recovery equal to 5% Of damage dealt", "magic drain" : "Magic recovery equal to 5% Of damage dealt", "savagery" : "Ignore enemy defence with axes", "large quiver" : "Hold up to 100 arrows", "weak-point" : "Gain +20 Critical damage with a bow", "even-weight" : "+50% more damage with staves", "parry" : "10% Chance to block enemy basic attack"}
    skill_class = [[0, 1, 1, 0, 0],
                   [2, 2, 2, 2, 2, 2, 2],
                   [1, 1, 2, 1, 2, 1, 1]]
    prev_choice = False
    weapons = {"rusty sword":[5, 6, "sword", ["None"]], "wooden spear":[7, 9, "spear", ["None"]], "sharp sword":[11,14,"sword",["Bleed=20"]],
               "iron dagger":[12,13,"sword", ["None"]], "welded sword":[9,15,"sword",["None"]], "iron-tipped spear":[16,19,"spear",["None"]],
               "mercenary's sword":[12,15,"sword",["None"]], "heavy sword strike":[8,12,10,"magic",["sword=10"]], "fireball":[25,30,40,"magic",["None"]],
               "balanced strike":[12,15,"magic",["healing=20"]],
               "woodcutter's axe":[12,14,"axe",["accuracy=75"]]
               }
    swordskills = [(1, 0), (1, 1), (2, 0), (2, 1)]
    axeskills = [(1, 2), (2, 2)]
    bowskills = [(1, 3), (1, 4), (2, 3), (2, 4)]
    magicskills = [(1, 5), (2, 5)]
    shieldskills = [(1, 6), (2, 6)]
    list_of_quests = 'poltowninnquest', 'lakemanquest', 'guards_somerquest', 'little_lost_bear'
    questart = False
    questfinish = False
    finishsidequest = False
    playerdata['health'] = playerdata['maxhealth']

    scaling = True
    blitext = False


    # Yes or No related:
    answer1 = False
    answer2 = False
    answer3 = False
    answer4 = False
    answers = 0
    answer_response = []
    queryid = ''

    def checkquery(queryid, answer):
        if queryid == 'test_response':
            if answer == 'accept':
                Globals.fight_turn = 'yes'
                Globals.playerdata['test_query'] = True
                Globals.active_dialog = Dialog([(""),("Thanks for participating", "Thank you for being a pleasant customer")])
                print('a')
            else:
                Globals.fight_turn = 'no'
                Globals.playerdata['test_query'] = False
                Globals.active_dialog = Dialog([(""),("Thanks for participating", "But why would you be so mean")])
                Globals.dialog_open = True
                print('n')
            Globals.dialog_open = True
            Globals.fight_turn = 'player'
        elif queryid == 'merc1_killing':
            if answer == 'kill':
                Globals.playerdata['merc1_death'] = True
                Globals.active_dialog = Dialog([(""), ("The mercenary's eyes freeze...", ""),
                                                ("You grab his sharp sword and brandish it", ""), ("You stab him through the chest", ""),
                                                ("His body falls limp and a small ring drops", "You take it...")])
            else:
                Globals.playerdata['merc1_death'] = False
                Globals.active_dialog = Dialog([(""), ("The mercenary smiles with gratitude and relief", ""), ("He grabs the small ring and hands it too you", ""),
                                                ("He also gives you his sharp sword", ""), ("It seems likes sparing him turned out better", "")])
                
            Globals.dialog_open = True
            Globals.fight_turn = 'player'
        elif queryid == 'help_michael?':
            if answer == 'help':
                Globals.fight_turn = 'yes'
                Globals.playerdata['michael_quests'] = 0.1
                Globals.active_dialog = Dialog([(""), ("Thank you so much!", "Suppose I should tell you what I need help with!")])
            else:
                Globals.fight_turn = 'yes'
                if Globals.playerdata['michael_refusal']:
                    Globals.playerdata['michael_quests'] = -1
                    Globals.playerdata['gideon_quests'] = 0.1
                    Globals.active_dialog = Dialog([(""), ("!!!", ""), ("Sure!!!", ""), ("I'll get out of your way", "")])
                else:
                    Globals.playerdata['michael_quests'] = 0.0
                    Globals.playerdata['michael_refusal'] = True
                    Globals.active_dialog = Dialog([(""), ("Oh...", ""), ("Maybe you can help me some other time?", ""), ("I promise it won't be a waste of time", "")])
            Globals.dialog_open = True
            Globals.fight_turn = 'player'
        elif queryid == "bribe_bar_somer_guards":
            if answer == "bribe":
                Globals.fight_turn = 'nil'
                if Globals.playerdata['gold'] >= 100:
                    Globals.playerdata['guards_somerquest'] = "part3"
                    Globals.playerdata['gold'] -= 100
                    Globals.active_dialog = Dialog([(""), ("Alright...", ""), ("Boys, let's scram", "")])
                    print("bribed em")
                else:
                    Globals.active_dialog = Dialog([(""), ("You're gonna need a lot more gold than that!", "")])
                    print("not enough gold")
                Globals.dialog_open = True
            elif answer == "fight":
                Globals.active_dialog = Dialog([(""), ("Let's fight, you filthly little vermin!", "")])
                print("let's fight")
                Globals.dialog_open = True
                Globals.fight_turn = 'player'
            else:
                Globals.active_dialog = Dialog([(""), ("See you around loser!", "")])
                Globals.dialog_open = True
                Globals.fight_turn = 'player'
                print("Run")
        elif queryid == "kill_torturer?":
            if answer == "kill":
                Globals.fight_turn = 'nil'
                Globals.active_dialog = Dialog([(""),("You stab him through the chest...", ""), ("He will kill no more...", "")])
                Globals.dialog_open = True
            else:
                Globals.active_dialog = Dialog([(""), ("You push the torturer against the wall so that", "you can pass...")])
                Globals.dialog_open = True
                Globals.fight_turn = 'player'
        elif queryid == "learn_defensive":
            if answer == "learn":
                Globals.fight_turn = 'nil'
                Globals.active_dialog = Dialog([(""),("You learnt the Defensive Strike!", "")])
                Globals.dialog_open = True
                if "Aggresive Strike" in Globals.playerdata['ownspells']: Globals.playerdata['ownspells'].remove("Aggresive Strike")
                if "Balanced Strike" in Globals.playerdata['ownspells']: Globals.playerdata['ownspells'].remove("Balanced Strike")
                Globals.playerdata['ownspells'].append("Defensive Strike")
            else:
                Globals.fight_turn = 'player'
                    
                
            
            

class Startup:
    playerdata = {'name' : 'NEW', 'gold' : 50,
                  'realm' : 'normal',
                  'location' : 'pol town',
                  'health' : 120, 'maxhealth' : 120,
                  'cavequest1' : 'part 1',
                  'FPS' : False, 'Music_volume' : 0.5,
                  'chests' : [False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, 
                              False, False, False, False, False, False, False,
                              ],
                  'sidequest' : [],
    
                  
                  'curweap' : 'Rusty Sword',
                  'ownspells' : ["Heavy Sword Strike",
                                 'Fireball'
                                 ],
                  'magic' : 43,
                  'maxmagic' : 43,
                  'soothing apples' : 3, 'magic jam' : 3, 'fruit jam' : 0, 'mushed berries' : 0,
                  'items': ['magic jam', 'soothing apples'],
                  'experience' : 0,
                  "level" : 1,
                  'xpcap' : 7,
                  'ownweapons' : ['Rusty Sword'],
                  'curshield' : 'Half a shield',
                  'ownshield' : ['Half a shield'],
                  'storyline' : 1,
                  'energy' : 1,
                  'maxenergy' : 1,
                  'quests' : 0,
                  'sidequests' : 0,
                  'accessories' : ['None'],
                  'accessory' : 'None',
                  'lakemanquest' : 'part1',
                  'poltowninnquest' : 'part1',
                  'preloca' : [-258, 152],
                  'key items' : ['Wooden Ring', 'Logbook'],
                  'mapinpoltown' : 'start',
                  'discovered locations' : ['pol town'],
                  'test_query' : False,
                  'merc1_death' : True,
                  'michael_quests' : 0.0,
                  'michael_refusal' : False,
                  'gideon_quests' : 0.0,
                  'cutscenes' : {"guard greet somerberry" : 0.0},
                  'guards_somerquest' : "part1",
                  'guards_somer_killed' : False,
                  'little_lost_bear' : "part1",
                  'skills' : [[True, False, False, True, True], [False, False, False, False, False, False, False], 
                  [False, False, False, False, False, False, False]],
                  'skill points' : 0,
                  

                  
                  
                  }

                #  LEVEL   STAT
    healthchart = { 1 :  110,
                    2 : 118,
                    3 : 124,
                    4 : 131,
                    5 : 138,
                    6 : 146,
                    7 : 153,
                    8 : 160,
                    9 : 167,
                    10 : 175,
                    11 : 183,
                    12 : 192,
                    13 : 200,
                    14 : 209,
                    15 : 219,
                    16 : 230,
                    17 : 241,
                    18 : 253,
                    19 : 266,
                    20 : 277,
                    21 : 290,
                    }
    manachart = { 1 : 40,
                  2 : 43,
                  3 : 46,
                  4 : 49,
                  5 : 52,
                  6 : 55,
                  7 : 57,
                  8 : 59,
                  9 : 62,
                  10 : 65,
                  11 : 68,
                  12 : 72,
                  13 : 75,
                  14 : 78,
                  15 : 81,
                  16 : 85,
                  17 : 88,
                  18 : 91,
                  19 : 94,
                  20 : 98,
                  21 : 107,
                  
                  
                  }

class Dialog:

    def __init__(self, text):
        self.page = 0
        self.text = text  # [("Hi"), ("How are you?")]

  

