'''
    >>> Програє звуки і музику
    >>> Зупиняє звук і музику
'''
# імпортуємо модулі 
import pygame, os, time 
import modules.data as m_data
# ініцілізуємо звук
pygame.mixer.init()
# встановлємо гучність для відтворення музики
# pygame.mixer.music.set_volume(0.5)
# створення класу для роботи з аудіо
main_volume = 0.5
soundtrack = 0.5
try:
    with open(m_data.path+m_data.type+'volume.txt', "r") as file:
        text = file.read()
        if 0 <= float(text) <= 1:
            main_volume = float(text)
            # print(main_volume)
except Exception as error:
    print(error)
    with open(m_data.path+m_data.type+'volume.txt', "w") as file:
        file.write(str(main_volume))
        # print("FFFFFFFFFFFFFFFFFFF")
class Audio():
    '''
        >>> Додає фонову музику
        >>> Встановлює гучність для звуку
    '''
    # ініцілізуємо клас аудіо 
    def __init__(self, name: str, loops: int = -1,volume = 0.5,max_time = "any",user = True): 
        global list_audio
        # створюємо змінні
        self.audio = None 
        self.name = name 
        self.loops = loops
        self.stoped = True
        # додаємо музику
        if user:
            self.audio = pygame.mixer.Sound(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
        else:
            self.audio = pygame.mixer.Sound(self.name)
        # встановлюємо гучність звуку
        self.audio.set_volume(volume)
        # перевіряємо чи дорівнює максимальний час будь-якому
        if max_time == 'any':
            # додаємо довжину звуку
            max_time = self.audio.get_length()
        # list_audio.append(self)
    def volume(self, volume):
        self.audio.set_volume(volume)
        if 'Soundtracks' in self.name:
            self.audio.set_volume(soundtrack*main_volume)
    # метод для відтворення аудіо
    def play(self, volume = None):
        global main_volume,soundtrack
        '''
            >>> Починає музику
        '''
        print(self.audio.get_length(),'times')
        try:
            # зупиняємо музику
            self.stoped = False
            # відтворюємо музику
            if volume:
                self.audio.set_volume(volume)
            elif 'Soundtracks' in self.name:
                # print(soundtrack)
                self.audio.set_volume(soundtrack*main_volume)
            else:
                self.audio.set_volume(main_volume)
            self.audio.play(loops= self.loops)
        except:
            # якщо буде помилка при завантаженні, виводимо повідомлення про помилку
            pass
    # метод для зупинки звуку

    def stop(self):
        '''
            >>> Зупиняє звук
            >>> Задає зупинки між звуками
            >>> Додає звук до досягнень
            >>> Додає звук для вибуху
            >>> Зупиняє музику
        '''
        # зупинка звуку
        self.audio.stop()
        # задаємо для зуптнки звуку значення True 
        self.stoped = True
# додаємо звук для досягнення
achievement = Audio('achievement',max_time=2, loops=0)
# додаємо звук для радару
radar = Audio('radar', loops=0)
name = '1'
try:
    with open(m_data.path+m_data.type+'music.txt', "r") as file:
        text = file.read()
        if 0 < int(text) < 5:
            name = int(text)
except Exception as error:
    print(error)
    with open(m_data.path+m_data.type+'music.txt', "w") as file:
        file.write('1')
list_audio = []
# задаємо саундтрек для доріжки звуку
track = Audio(f'Soundtracks/{name}')
# додаємо звук покупки
buying = Audio('buying',0)
# перевіряємо чи не дорівнює звук значенню False
if m_data.read_data["sound"] != "False":
    # граємо звукову доріжку
    track.play()
# додаємо звук для вибуху
explosion = Audio('blas',0)
def edit_soundtrack():
    global track 
    while True:
        if not track.stoped:
            if int(track.audio.get_length()) <= m_data.count_of_music:
                if m_data.is_change:
                    track.stop()
                    number = track.name.split("/")[1]
                    track.name = f"Soundtracks/{int(number)+1}"
                    if number == "5":
                        track.name = f"Soundtracks/1"
                    track.audio = track.audio = pygame.mixer.Sound(os.path.abspath(f"{__file__}/../../audio/{track.name}.mp3"))
                    track.play()
                    m_data.count_of_music = 0
                    track.volume(main_volume * soundtrack)
                else:
                    m_data.count_of_music = 0
            else:
                print('hhhhhhhhhhhhhhhhhhhh',m_data.is_change,int(track.audio.get_length()), m_data.count_of_music)
            m_data.count_of_music += 1
        time.sleep(1)

