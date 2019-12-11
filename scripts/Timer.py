from scripts.globals import *

class Timer:

    def __init__(self, interval = 1):
        self.interval = interval
        self.Value = 0
        self.LastInt = 0
        self.active = False
        self.OnNext = None


    def Update(self):
        if self.active:
            self.Value += Globals.deltatime / self.interval
            if int(self.Value) != int(self.LastInt):
                self.LastInt = int(self.Value)
                if self.OnNext != None:
                    self.OnNext()


    def Start(self):
        self.active = True

    def Pause(self):
        self.active = False

    def Stop(self):
        self.Reset()
        self.active = False


    def Reset(self):
        self.Value = 0
        self.LastInt = 0
        self.active = True
