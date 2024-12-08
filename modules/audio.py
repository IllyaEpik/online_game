# імпортуємо модулі pyagame і os
import pygame, os 
# ініцілізуємо звук
pygame.mixer.init()
# встановлємо гучність для відтворення музики
pygame.mixer.music.set_volume(0.5)
# створення класу для роботи з аудіо
class Audio():
    # ініцілізуємо клас аудіо 
    def __init__(self, name: str, loops: int = -1): 
        # создаємо 3 змінні: self.audio, self.name, self.loops
        self.audio = None 
        self.name = name 
        self.loops = loops
    # метод для відтворення аудіо
    def play(self):
        try:
            # завантаження музику по вказаному шляху
            pygame.mixer.music.load(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
            # відтворюємо музику
            self.audio = pygame.mixer.music.play(loops= self.loops)
            print(self.audio)
        except:
            # якщо буде помилка при завантаженні, виводимо повідомлення про помилку
            print("Error: audio")
track = Audio('Soundtrack')
track.play()
# explosion = Audio('blas',0)
