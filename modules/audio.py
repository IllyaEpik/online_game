# імпортуємо модулі 
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
        # створюємо змінні
        self.audio = None 
        self.name = name 
        self.loops = loops
        self.stoped = True
        # додаємо фонову музику
        self.audio = pygame.mixer.Sound(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
        # встановлюємо гучність звуку
        self.audio.set_volume(volume)
        # перевіряємо чи дорівнює максимальний час будь-якому
        if max_time == 'any':
            # додаємо довжину звуку
            max_time = self.audio.get_length()
    # метод для відтворення аудіо
    def play(self):
        try:
            # зупиняємо музику
            self.stoped = False
            # відтворюємо музику
            self.audio.play(loops= self.loops)
        except:
            # якщо буде помилка при завантаженні, виводимо повідомлення про помилку
            print("Error: audio")
    # метод для зупинки звуку
    def stop(self):
        # зупинка звуку
        self.audio.stop()
        # задаємо для зуптнки звуку значення True 
        self.stoped = True
# додаємо звук для досягнення
achievement = Audio('achievement',max_time=2, loops=0)
# додаємо звук для радару
radar = Audio('radar', loops=0)
# задаємо саундтрек для доріжки звуку
track = Audio('Soundtrack')
# перевіряємо чи не дорівнює звук значенню False
if m_data.read_data["sound"] != "False":
    # граємо звукову доріжку
    track.play()
# додаємо звук для вибуху
explosion = Audio('blas',0)