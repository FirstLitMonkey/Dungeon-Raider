import pygame


# Load Attack 1 animation
attProR7 = pygame.image.load("graphics\\character\\Attack1\\attack_7.png")
attProR8 = pygame.image.load("graphics\\character\\Attack1\\attack_8.png")
attProR9 = pygame.image.load("graphics\\character\\Attack1\\attack_9.png")
attProR10 = pygame.image.load("graphics\\character\\Attack1\\attack_10.png")
attProR11 = pygame.image.load("graphics\\character\\Attack1\\attack_11.png")
attProR12 = pygame.image.load("graphics\\character\\Attack1\\attack_12.png")
# Load Attack 2 animation 
attSpear1 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_1.png"), (200, 148))
attSpear2 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_2.png"), (200, 148))
attSpear3 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_3.png"), (200, 148))
attSpear4 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_4.png"), (200, 148))
attSpear5 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_5.png"), (200, 148))
attSpear6 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack2\\attack_6.png"), (200, 148))
# Load Attack 3 animations
attAxe1 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_7.png"), (200, 148))
attAxe2 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_8.png"), (200, 148))
attAxe3 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_9.png"), (200, 148))
attAxe4 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_10.png"), (200, 148))
attAxe5 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_11.png"), (200, 148))
attAxe6 = pygame.transform.scale(pygame.image.load("graphics\\character\\Attack3\\attack_12.png"), (200, 148))
# Scale Images
AttProR7 = pygame.transform.scale(attProR7, (200, 148))
AttProR8 = pygame.transform.scale(attProR8, (200, 148))
AttProR9 = pygame.transform.scale(attProR9, (200, 148))
AttProR10 = pygame.transform.scale(attProR10, (200, 148))
AttProR11 = pygame.transform.scale(attProR11, (200, 148))
AttProR12 = pygame.transform.scale(attProR12, (200, 148))
# Sword and Dagger Attack
att1ProR = [AttProR7, AttProR8, AttProR9, AttProR10, AttProR11, AttProR12]
# Spear Attack
att1Spear = [attSpear1, attSpear2, attSpear3, attSpear4, attSpear5, attSpear6]
# Axe Attack
att1Axe = [attAxe1, attAxe2, attAxe3, attAxe4, attAxe5, attAxe6]

# Load Heavy Attack Animation
attProR13 = pygame.image.load("graphics\\character\\Heavy\\attack_13.png")
attProR14 = pygame.image.load("graphics\\character\\Heavy\\attack_14.png")
attProR15 = pygame.image.load("graphics\\character\\Heavy\\attack_15.png")
attProR16 = pygame.image.load("graphics\\character\\Heavy\\attack_16.png")
attProR17 = pygame.image.load("graphics\\character\\Heavy\\attack_17.png")
attProR18 = pygame.image.load("graphics\\character\\Heavy\\attack_18.png")
attProR19 = pygame.image.load("graphics\\character\\Heavy\\attack_19.png")

AttProR13 = pygame.transform.scale(attProR13, (200, 148))
AttProR14 = pygame.transform.scale(attProR14, (200, 148))
AttProR15 = pygame.transform.scale(attProR15, (200, 148))
AttProR16 = pygame.transform.scale(attProR16, (200, 148))
AttProR17 = pygame.transform.scale(attProR17, (200, 148))
AttProR18 = pygame.transform.scale(attProR18, (200, 148))
AttProR19 = pygame.transform.scale(attProR19, (200, 148))

attHProR = [AttProR7, AttProR8, AttProR9, AttProR10, AttProR11, AttProR12, AttProR13, AttProR14, AttProR15, AttProR16, AttProR17, AttProR18, AttProR19]

# Import Fireball!

fireball1 = pygame.image.load("graphics\\effects\\fireball.png")
fireball2 = pygame.image.load("graphics\\effects\\fireball_1.png")
fireball3 = pygame.image.load("graphics\\effects\\fireball_2.png")

Fireball1 = pygame.transform.scale(fireball1, (380, 180))
Fireball2 = pygame.transform.scale(fireball2, (380, 180))
Fireball3 = pygame.transform.scale(fireball3, (380, 180))

attFire = [Fireball1, Fireball2, Fireball3]
merc1 = pygame.image.load("graphics\\enemies\\merc1.png")
merc2 = pygame.image.load("graphics\\enemies\\merc2.png")
Merc1 = pygame.transform.scale(merc1, (250, 185))
# Import fight stances with different weapons
idle = pygame.transform.scale(pygame.image.load("graphics\\character\\Idle.png"), (200, 148))
idle2 = pygame.transform.scale(pygame.image.load("graphics\\character\\idle_.png"), (200, 148))
idle3 = pygame.transform.scale(pygame.image.load("graphics\\character\\idle_sp.png"), (200, 148))
idle4 = pygame.transform.scale(pygame.image.load("graphics\\character\\idle_axe.png"), (200, 148))
Idle = [idle, idle2, idle3, idle4]


# Import Skeleton
skeleton_idle = pygame.image.load("graphics\\Skeleton\\Idle.png")
skeleton_Idle = pygame.transform.scale(skeleton_idle, (160, 160))
# Import Bandit
bandit = pygame.image.load("graphics\\enemies\\merc2.png")
Bandit = pygame.transform.scale(bandit, (150, 111))

# Import Grass Viper
viper1 = pygame.image.load("graphics\\enemies\\forest_viper.png")
Viper1 = pygame.transform.scale(viper1, (156, 152))
viper1h = pygame.image.load("graphics\\enemies\\forest_viper_hurt.png")
Viper1h = pygame.transform.scale(viper1h, (156, 152))


# Import Rock Golem
golem1 = pygame.image.load("graphics\\enemies\\rock_golem.png")
RockGolem1 = pygame.transform.scale(golem1, (124, 166))
golem2 = pygame.image.load("graphics\\enemies\\rock_golem_hurt.png")
RockGolem2 = pygame.transform.scale(golem2, (124, 166))

# Import Cyclops
cyclops = pygame.image.load("graphics\\enemies\\green_cyclops.png")
Cyclops = pygame.transform.scale(cyclops, (196, 196 ))


# Import Bat
bat_img = pygame.image.load("graphics\\enemies\\bat.png")
bat_img = pygame.transform.scale(bat_img, (153, 132))

# Import Zombie
zombie_img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("graphics\\enemies\\zombie.png"), (106, 170)), True, False)
zombie_hurt = pygame.transform.flip(pygame.transform.scale(pygame.image.load("graphics\\enemies\\zombie_hurt.png"), (106, 170)),True, False)

# Import Backgrounds

cave_bg = pygame.image.load("graphics\\gui\\cave_bg.jpg")
cave_bg = pygame.transform.scale(cave_bg, (800, 200))

# Import Arrow
arrow = pygame.image.load("graphics\\gui\\arrow.png")
# Import Magical Cannon # MADE BY CRIMSON_REAPER
mag_cannon = pygame.image.load("graphics\\enemies\\magic_cannon.png")
mag_cannon = pygame.transform.scale(pygame.transform.flip(mag_cannon, True, False), (350, 350))
mag_cannon_hurt = pygame.image.load("graphics\\enemies\\magic_cannon_hurt.png")
mag_cannon_hurt = pygame.transform.scale(pygame.transform.flip(mag_cannon_hurt, True, False), (350, 350))
# Not Removable
cool_bg = pygame.image.load("graphics\\gui\\cool_bg.png")
# Import Somerberry Guard
somer_guard = pygame.image.load("graphics\\enemies\\guard1.png")
somer_guard = pygame.transform.scale(somer_guard, (250, 180))
# Import Commander Knok
knok_battle = pygame.image.load("graphics\\enemies\\knok.png")
knok_battle = pygame.transform.scale(knok_battle, (250, 180))
# Import Axe
orc_image = pygame.image.load("graphics\\enemies\\orc.png")
orc_image = pygame.transform.scale(orc_image, (180, 180))
orc_hurt = pygame.image.load("graphics\\enemies\\orc_hurt.png")
orc_hurt = pygame.transform.scale(orc_hurt, (180, 180))

# Import Golden Wave
golden_wave = pygame.image.load("graphics\\effects\\glowing_wave.png")
golden_wave = pygame.transform.scale(golden_wave, (200, 400))
# Import stare
stare = pygame.image.load("graphics\\effects\\stare.png")
stare = pygame.transform.rotate(stare, 275)
# Import spear barrage
spear_barrage = pygame.image.load("graphics\\effects\\spears.png")
spear_barrage = pygame.transform.scale(pygame.transform.rotate(spear_barrage, 45), (260, 275))


del  attProR7, attProR8, attProR9, attProR10, attProR11, attProR12, attProR13, attProR14, attProR15,
del  attProR16, attProR17, attProR18, attProR19, idle, skeleton_idle,
del fireball1, fireball2, fireball3, viper1, viper1h, golem1, golem2, cyclops
del attSpear1, attSpear2, attSpear3, attSpear4, attSpear5, attSpear6, attAxe1, attAxe2, attAxe3, attAxe4, attAxe5, attAxe6

