




class Globals:

    camera_x = 0
    camera_y = 0
    camera_ymove = 0
    camera_xmove = 0
    scene = "menu"
    fight_turn = 'player'
    fight_move = False
    fight_count = 0
    deltatime = 0
    chest_offcut = False
    win = False
    dialog_open = False
    active_dialog = None

    playerdata = {'gold' : 20, 'location' : 'town',
                  'health' : 100, 'maxhealth' : 120,
                  'cavequest1' : 'part 1',
                  'FPS' : False, 'Music_volume' : 0.5,
                  'chest1' : False,
                  'chest2' : False,
                  'curweap' : 'Rusty Sword',
                  }

    cavechest_locations = [20, 30,
                          10, 7
                          ]

    print(playerdata['health'])
    playerdata['health'] = playerdata['maxhealth']
    print(playerdata['health'])


class Dialog:

    def __init__(self, text):
        self.page = 0
        self.text = text  # [("Hi"), ("How are you?")]



    
