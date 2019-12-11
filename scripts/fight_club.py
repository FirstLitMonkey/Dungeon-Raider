import pygame, time, math
from scripts.globals import *
from scripts.enemystats import *
from scripts.meloonatic_gui import *
from scripts.playerstats import *
superfont = pygame.font.Font("C:\\Windows\\Fonts\\MTCORSVA.ttf", 100)
small_font = pygame.font.Font("C:\\Windows\\Fonts\\IMPACT.ttf", 11)
Pattack = 0
Eattack = 6
clock = pygame.time.Clock()
PlayerIG = player(200, 148)
class Fight():
    
    def display(win):
        enemy = Enemystats.enemies[Globals.enemy_switch]
        if Globals.fight_move == True:
            if Globals.fight_turn == 'enemy':
                message = ('You dealt ' + str(Pattack) + ' damage')
                if Pattack == 0:
                    message = ("The enemy is immune to this damage")
                elif Pattack < 0:
                    message = ("You missed the enemy!")
                win.blit(Font.Default.render(message, True, Color.White), (70, 170))
                win.blit(small_font.render(str(math.ceil(Globals.Healing)), True, Color.Red), (135, 10))
                win.blit(small_font.render(str(math.ceil(Globals.Magic)), True, Color.Blue), (144, 30))
                Globals.fight_count += Globals.deltatime
                if Globals.fight_count >= 0.8:
                    Globals.fight_move = False
                    Globals.fight_count = 0
                    enemy.Dead_()
                    if enemy.dead:
                        Globals.fight_move = False
                        Globals.fight_turn = 'zilch'
                        PlayerIG.attack1 = False
                        Globals.fight_count = 0
                        Globals.win = True
                        Globals.storyline_fight = False
                        Globals.playerdata['energy'] = 1
                        Globals.playerdata['maxenergy'] = 1
                        Globals.current_list = 0
                        PlayerIG.x = 50
                        
                    
                    
                    else:
                        
                        Globals.current_list = 0
                        Fight.EnemyAttack(enemy.weapon)
                        x = 50
            else:
                message = ('The enemy dealt ' + str(Eattack) + ' damage')
                if Globals.stunned == True:
                    if Eattack == 0:
                        message = ("The enemy stunned you!")
                    else:
                        message = ("The enemy dealt " + str(Eattack) + 'stunning you')
                win.blit(Font.Default.render(message, True, Color.Red), (400, 170))
                x = 50 + Globals.deltatime * 10
                if Globals.special_activated == True:
                    message = enemy.special[0]
                    win.blit(Font.Default.render(message, True, Color.Gold), (400, 20))
                    Globals.cooldown_counter_spec = 0
                    if enemy.special[0] == "Man of Power":
                        win.blit(golden_wave, (x, -140))
                    elif enemy.special[0] == "Walk of the Undead":
                        win.blit(pygame.transform.rotate(golden_wave, 270), (x + 300, 0))
                    elif enemy.special[0] == "Stare":
                        win.blit(stare, (340, -40))
                    elif enemy.special[0] == "Morale":
                        win.blit(golden_wave, (600, -140))
                elif Globals.ultimate_activated == True:
                    message = enemy.ultimate[0]
                    win.blit(Font.Default.render(message, True, Color.Blue), (400, 20))
                    Globals.cooldown_counter_ulti = 0
                    if enemy.ultimate[0] == "Crushing and Gnawing":
                        win.blit(golden_wave, (x + 200, -140))
                    elif enemy.ultimate[0] == "Death Be Upon You":
                        win.blit(spear_barrage, (75, 0))

                    
                
                Globals.fight_count += Globals.deltatime

                if Globals.fight_count >= 0.5:
                    Globals.fight_move = False
                    Globals.fight_count = 0
                    
                    playerdead_()
                    if PlayerIG.dead:
                        Globals.fight_move = False
                        Globals.fight_turn ='enemy win'
                        Globals.win = True
                        Globals.playerdata['energy'] = 1
                        Globals.playerdata['maxenergy'] = 1
                        Globals.storyline_fight = False
                        
                        
                    else:
                        if not Globals.stunned == True:
                            Globals.fight_turn = 'player'
                            if Globals.playerdata['energy'] == 1:
                                Globals.playerdata['maxenergy'] += 1
                            Globals.playerdata['energy'] = 1
                            if Globals.playerdata['maxenergy'] > 4:
                                Globals.playerdata['maxenergy'] = 4
                            Globals.playerdata['energy'] = 1
                            Globals.special_activated = False
                            Globals.ultimate_activated = False
                            x = 50
                            if Globals.poisoned_player:
                                Globals.playerdata['health'] -= Globals.playerdata['maxhealth'] * 0.05
                                Globals.poisoned_player = False
                                playerdead_()
                                if PlayerIG.dead:
                                    Globals.fight_move = False
                                    Globals.fight_turn ='enemy win'
                                    Globals.win = True
                                    Globals.playerdata['energy'] = 1
                                    Globals.playerdata['maxenergy'] = 1
                                    Globals.storyline_fight = False
                        else:
                            Globals.fight_turn = 'enemy'
                            Globals.special_activated = False
                            x = 50
                            Globals.ultimate_activated = False
                            Globals.cooldown_counter_spec += 1
                            Globals.cooldown_counter_ulti += 1
                            Fight.EnemyAttack(enemy.weapon)
                            Globals.stunned = False
                            Globals.current_list = 0




    def PlayerAttack(weapon):
        global Pattack, Eattack, enemy
        weapon = weapon.lower()
        enemy = Enemystats.enemies[Globals.enemy_switch]
        Globals.Healing, Globals.Magic = 0, 0
        try:
            Pattack = random.randint(Globals.weapons[weapon][0], Globals.weapons[weapon][1])
            for fx in Globals.weapons[weapon][3]:
                if "sword" in fx: Pattack += int(fx.split("=")[1])
                if "bleed" in fx: 
                    if random.randint(0, 99) <= int(fx.split("=")[1]): Pattack += Pattack/10
                if "accuracy" in fx:
                    if random.randint(1, 100) <= int(fx.split("=")[1]): 
                        Pattack = -1
                        break
                if "healing" in fx: Healing += int(fx.split("=")[1]) * Globals.playerdata['energy']
            if Globals.weapons[weapon][2] != 'magic': 
                Pattack *= Globals.playerdata['energy']
                Globals.anime_turn = Globals.playerdata['energy']
            else: 
                Pattack = round(Globals.playerdata['energy'] * Pattack / 3)
            if Globals.weapons[weapon][2] == "sword":
                for skill in Globals.swordskills:
                    print("true")
                    if Globals.playerdata['skills'][skill[0]][skill[1]] == True: Pattack = Fight.skill_check(skill, Pattack, Globals.playerdata['magic'], Globals.playerdata['health'], enemy.health)          
            elif Globals.weapons[weapon][2] == "axe":
                for skill in Globals.axeskills:
                    print("true")
                    if Globals.playerdata['skills'][skill[0]][skill[1]] == True: Pattack = Fight.skill_check(skill, Pattack, Globals.playerdata['magic'], Globals.playerdata['health'], enemy.health)
            if not "ignore defence" in Globals.weapons[weapon][3]:
                print(Pattack)
                Pattack -= enemy.defence
        except KeyError:
            Pattack = 5 * Globals.playerdata['energy']
        Globals.playerdata['maxenergy'] -= Globals.playerdata['energy']
        Globals.playerdata['maxenergy'] += 1
        if Globals.playerdata['maxenergy'] == 0:
            Globals.playerdata['maxenergy'] = 1
        Globals.fight_move = True
        if weapon in enemy.immunity:
            Pattack = 0
        if not Pattack <= 0:
            enemy.health -= Pattack
        Globals.playerdata['health'] += math.ceil(Globals.Healing)
        Globals.playerdata['magic'] += math.ceil(Globals.Magic) 
        if Globals.playerdata['health'] >= Globals.playerdata['maxhealth']: Globals.playerdata['health'] = Globals.playerdata['maxhealth']
        if Globals.playerdata['magic'] >= Globals.playerdata['maxmagic']: Globals.playerdata['magic'] = Globals.playerdata['maxmagic']
        Globals.fight_currentmove = 'run'

        
    def EnemyAttack(weapon):
        global Pattack, Eattack
        weapon = weapon.lower()
        enemy = Enemystats.enemies[Globals.enemy_switch]
        Globals.cooldown_counter_spec += 1
        Globals.cooldown_counter_ulti += 1
        Eattack = enemy.damage
        if Globals.playerdata['curshield'] == 'half a shield':
            PDefence = 1
        elif Globals.playerdata['curshield'] == 'wooden shield':
            PDefence = 5
        elif Globals.playerdata['curshield'] == 'welded shield':
            PDefence = random.randint(3, 8)
        else:
            PDefence = 0
        Eattack = round(Eattack - PDefence / (random.randint(5, 10)))
        Eattack = Eattack + random.randint(-3, 3)
        try:
            special_ability = enemy.special
            if enemy.special[2] <= Globals.cooldown_counter_spec:
                Eattack = round((enemy.special[1] * enemy.damage) - PDefence)
                if "ignore defence" in enemy.special[3]:
                    Eattack = round((enemy.special[1] * enemy.damage))
                if "health steal" in enemy.special[3]:
                    enemy.health += Eattack
                    if enemy.health > enemy.maxhealth:
                        enemy.health = enemy.maxhealth
                if "inflict stun" in enemy.special[3]:
                    
                    Globals.stunned = True
                if "increase attack" in enemy.special[3]:
                    enemy.damage = enemy.damage * 1.2
                if "inflict poison" in enemy.special[3]:
                    Globals.poisoned_player = True
                if "recover 10" in enemy.special[3]:
                    enemy.health += round(enemy.maxhealth / 10)
                    if enemy.health > enemy.maxhealth:
                        enemy.health = enemy.maxhealth

                Globals.special_activated = True
        except AttributeError:
            pass
        except NameError:
            pass
        try:
            
            ultimate = enemy.ultimate
            if enemy.ultimate[2] <= Globals.cooldown_counter_ulti:
                Eattack = round((enemy.ultimate[1] * enemy.damage) - PDefence)
                if "ignore defence" in enemy.ultimate[3]:
                    Eattack = round(enemy.ultimate[1] * enemy.damage)
                if "health steal" in enemy.ultimate[3]:
                    enemy.health += Eattack
                    if enemy.health > enemy.maxhealth:
                        enemy.health = enemy.maxhealth + (Globals.playerdata['level'] * 5)
                if "inflict stun" in enemy.ultimate[3]:
                    Globals.stunned = True
                if "remove 100 mag" in enemy.ultimate[3]:
                    Globals.playerdata['magic'] = 0
                if "remove 50 mag" in enemy.ultimate[3]:
                    Globals.playerdata['magic'] -= round(Globals.playerdata['maxmagic'] / 2)
                    if Globals.playerdata['magic'] < 0:
                        Globals.playerdata['magic'] = 0
                if "increase attack" in enemy.ultimate[3]:
                    enemy.damage = enemy.damage * 1.2

                Globals.ultimate_activated = True
        except AttributeError:
            pass
        except NameError:
            pass
        except KeyError:
            pass
            
        
        Globals.fight_move = True
        Globals.playerdata['health'] -= Eattack
        Globals.fight_turn = 'abcd'
        Globals.fight_currentmove = 'run'


    def prefight():
        # 0 - skeleton, 1 - Mercenary
        # 2 - Mercenary Leader, 3 - Bandit
        # 4 - Cyclops, 5 - Viper
        # 6 - Baby Rock Golem, 7 - Bat,
        # 8 - Zombie, 9 - Michael,
        # 10 - Gideon, 11 - Magical Cannon,
        # 12 - Corrupt S Guard, 13 - Torturer S
        # 14 - Commander Knok, 15 - Orc Assaulter
        if Globals.playerdata['location'] == 'cave':
            choice = random.randint(0, 100)
            if choice <= 16:
                choice = 6
            elif choice <= 58:
                choice = 0
            else:
                choice = 7
            # 16% - rock golem, 42% - bat, skeleton
        elif Globals.playerdata['location'] == 'lake':
            choice = random.randint(0, 100)
            if choice <= 50:
                choice = 5
            elif choice <= 75:
                choice = 7
            else:
                choice = 3
            # 50% - viper, 25% - bat, bandit
        elif Globals.playerdata['location'] == 'fields':
            choice = random.randint(0, 100)
            if choice <= 10:
                choice = 11
            elif choice <= 30:
                choice = 6
            elif choice <= 55:
                choice = 8
            else:
                choice = 5
            # 45% - viper, 25% - zombie, 20% - rock golem, 10% - Magic cannon
        elif Globals.playerdata['location'] == 'southern frontier':
            choice = random.randint(0, 100)
            if choice <= 11:
                choice = 0
            elif choice <= 22:
                choice = 3
            elif choice <=33:
                choice = 5
            elif choice <= 44:
                choice = 7
            elif choice <=60:
                choice = 8
            else:
                choice = 6
            # 11% - Skeleton, Bandit, Viper, Bat, 40 % - Golem, 16% Zombie
        elif Globals.playerdata['location'] == 'northern passage':
            choice = random.randint(0, 100)
            if choice <= 40:
                choice = 6
            else:
                choice = 8
            # 40% - Rock Golem; 60% - Zombie
        
        Globals.current_list = 0
        Globals.idea_list = ['attack']
        Globals.enemy_switch = choice   
        Globals.start_of_battle = True
        pygame.mixer.music.load("music\\fighttheme.mp3")
        pygame.mixer.music.play(-1)
    


    def skill_check(locale, Pattack, plmag, plheal, eheal):
        # Skill Location, Player Attack, Player magic, Player health, Enemy health
        if locale == (1,0): return round(Pattack * 1.25)
        if locale == (1,1):
            print("true")
            if random.randint(1,4) == 1: 
                Globals.anime_turn += 1
                return round(Pattack / Globals.playerdata['energy']) * (Globals.playerdata['energy'] + 1)
        if locale == (2, 0): Globals.Healing = Pattack / 20
        if locale == (2, 1): Globals.Magic = Pattack / 20
        if locale == (1, 2):
            if eheal >= eheal / 2: return Pattack * 2
        if locale == (2, 2):
            return Pattack + enemy.defence
        # If there are no sfx, then simply return the Player's attack
        return Pattack
        

        
def playerdead_():
     if Globals.playerdata['health'] <= 0:
        PlayerIG.dead = True
        

        
        
        
