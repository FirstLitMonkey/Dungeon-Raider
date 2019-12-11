from scripts.meloonatic_gui import *
from scripts.globals import *
from scripts.textures import *
import pickle, pygame, os


window_width, window_height = 800, 600


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Dungeon Raider Animated"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)



def play():
    Globals.scene = "game"
def exit():
    is_running = False
def options():
    Globals.scene = 'options'
def backto_menu():
    Globals.scene = 'menu'

def FPSon_off():
    if Globals.playerdata['FPS']:
        btnFPS = Menu.Button(text='Off', rect=(360, 80, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
        btnFPS.Command = FPSon_off
        Globals.playerdata['FPS'] = False
        print(Globals.playerdata)
    else:
        btnFPS = Menu.Button(text='On', rect=(360, 80, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
        btnFPS.Command = FPSon_off
        Globals.playerdata['FPS'] = True
        print(Globals.playerdata)
def Scale_on_off():
    if Globals.scaling:
        btnScale = Menu.Button(text='Off', rect=(360, 320, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
        btnScale.Command = Scale_on_off
        Globals.scaling = False
    else:
        btnScale = Menu.Button(text='On', rect=(360, 320, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
        btnScale.Command = Scale_on_off
        Globals.scaling = True
def change_volumeL():
    pygame.mixer.music.set_volume(0.1)
    Globals.playerdata['Music_volume'] = 0.1
    btnLowVolume = Menu.Button(text='Low', rect=(280, 200, 80, 60),
                      bg=Color.CornflowerBlue, fg=Color.White,
                      bgr=Color.CornflowerBlue, tag=('options', None))
    btnHighVolume = Menu.Button(text='High', rect=(440, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
    btnMedVolume = Menu.Button(text='Med', rect=(360, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
def change_volumeM():
    pygame.mixer.music.set_volume(0.5)
    Globals.playerdata['Music_volume'] = 0.5
    btnMedVolume = Menu.Button(text='Med', rect=(360, 200, 80, 60),
                      bg=Color.CornflowerBlue, fg=Color.White,
                      bgr=Color.CornflowerBlue, tag=('options', None))
    btnLowVolume = Menu.Button(text='Low', rect=(280, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
    btnHighVolume = Menu.Button(text='High', rect=(440, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
def change_volumeH():
    pygame.mixer.music.set_volume(0.9)
    Globals.playerdata['Music_volume'] = 0.9
    btnHighVolume = Menu.Button(text='High', rect=(440, 200, 80, 60),
                      bg=Color.CornflowerBlue, fg=Color.White,
                      bgr=Color.CornflowerBlue, tag=('options', None))
    btnLowVolume = Menu.Button(text='Low', rect=(280, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
    btnMedVolume = Menu.Button(text='Med', rect=(360, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
def inventory_switch():
    Globals.scene = 'inventory'
    Globals.fight_turn = 'invent'

def help_switch():
    Globals.scene = 'help'
def save():
    Globals.playerdata['preloca'] = [Globals.camera_x, Globals.camera_y]
    with open(Globals.filename, 'wb') as f:
        pickle.dump(Globals.playerdata, f)
    create_window()

def load():
    if os.path.exists(Globals.filename) == True:
        os.system("cls")
        with open(Globals.filename, "rb") as f:
            Globals.playerdata = pickle.load(f)
        print("Loaded Save File")
        option = input("...")
    else:
        print("The savefile does not exist!")
        exit()


btnFPS = Menu.Button(text='Off', rect=(360, 80, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
btnFPS.Command = FPSon_off

btnLowVolume = Menu.Button(text='Low', rect=(280, 200, 80, 60),
                           bg=Color.Gray, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
btnMedVolume = Menu.Button(text='Med', rect=(360, 200, 80, 60),
                           bg=Color.CornflowerBlue, fg=Color.White,
                           bgr=Color.CornflowerBlue, tag=('options', None))
btnHighVolume = Menu.Button(text='High', rect=(440, 200, 80, 60),
                            bg=Color.Gray, fg=Color.White,
                            bgr=Color.CornflowerBlue, tag=('options', None))
btnLowVolume.Command, btnHighVolume.Command, btnMedVolume.Command = change_volumeL, change_volumeH, change_volumeM


menuFPS = Menu.Text(text="FPS:", color=Color.White, font=Font.Default)

menuFPS.Left, menuFPS.Top = 300, 100

menuVol = Menu.Text(text='Volume:', color=Color.White, font=Font.Default)

menuVol.Left, menuVol.Top = 170, 215


menuScale = Menu.Text(text="Scaling:", color=Color.White, font=Font.Default)

menuScale.Left, menuScale.Top = 250, 330
btnScale = Menu.Button(text='On', rect=(360, 320, 80, 60),
                     bg=Color.Gray, fg=Color.White,
                     bgr=Color.CornflowerBlue, tag=('options', None))
btnScale.Command = Scale_on_off


