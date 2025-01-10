# імпортуємо модулі pyagame і os
import pygame, os 
import modules.data as m_data
# ініцілізуємо звук
pygame.mixer.init()
# встановлємо гучність для відтворення музики
# pygame.mixer.music.set_volume(0.5)
# створення класу для роботи з аудіо
class Audio():
    # ініцілізуємо клас аудіо 
    def __init__(self, name: str, loops: int = -1,volume = 0.5,max_time = "any"): 
        # создаємо 3 змінні: self.audio, self.name, self.loops
        self.audio = None 
        self.name = name 
        self.loops = loops
        self.stoped = True
        self.audio = pygame.mixer.Sound(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
        self.audio.set_volume(volume)
        if max_time == 'any':
            max_time = self.audio.get_length()
    # метод для відтворення аудіо
    def play(self):
        try:
            # завантаження музику по вказаному шляху
            
            self.stoped = False
            
            # відтворюємо музику
            self.audio.play(loops= self.loops)
        except:
            # якщо буде помилка при завантаженні, виводимо повідомлення про помилку
            print("Error: audio")
    def stop(self):
        self.audio.stop()
        # pygame.mixer.music.stop()
        self.stoped = True
    # def pause(self):
    #     self.audio
# pygame.mixer_music.load()
achievement = Audio('achievement',max_time=2, loops=0)
radar = Audio('radar', loops=0)
track = Audio('Soundtrack')
if m_data.read_data["sound"] != "False":
    track.play()
explosion = Audio('blas',0)