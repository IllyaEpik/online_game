import pygame, os 
pygame.mixer.init()
pygame.mixer.music.set_volume(1)

class Audio():
    def __init__(self, name: str, loops: int = -1): 
        self.name = name 
        self.audio = None 
        self.loops = loops
    def play(self):
        try:
            pygame.mixer.music.load(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
            self.audio = pygame.mixer.music.play(loops= self.loops)
        except:
            print("Error: audio")
