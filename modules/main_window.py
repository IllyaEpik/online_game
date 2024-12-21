# імпортуємо модуль pygame
import pygame, threading, os
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.buttons as m_buttons
import modules.data as m_data
import modules.images as m_images
import modules.client as m_client
import modules.ships as m_ships
import modules.attack as m_attack
import modules.server as m_server
import modules.audio as m_audio


# 
class Screen():
    # ініціалізуємо screen
    def __init__(self):
        # создаємо таймер
        self.clock = pygame.time.Clock()
        # вказуємо ширину
        self.WIDTH= 1280
        # вказуємо висоту
        self.HEIGHT = 832
        # создаємо екран
        self.screen = pygame.display.set_mode(size= (self.WIDTH, self.HEIGHT))
        # задаємо назву нашому екрану
        pygame.display.set_caption('online game')
        icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
        pygame.display.set_icon(icon)
    # функція запуску
    def run(self):
        # m_data.progression = 'lose'
        # задаємо правдиве значення грі
        game = True
        # цикл поки гра активна
        while game:
            # цикл всіх подій
            for event in pygame.event.get():
                # якщо вікно зачинено то 
                if event.type == pygame.QUIT:
                    # значення гри неправда
                    game = False
                    m_data.end=True
                    try:
                        # відключаємо клієнта
                        m_client.client.close()
                    except:
                        pass 
                # коли кнопка миші натиснута
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if m_data.progression in "winlose":
                        m_buttons.revenge.button_start(event)
                        if m_buttons.out.button_start(event):
                            game = False
                            m_data.end=True
                            try:
                                # відключаємо клієнта
                                m_client.client.close()
                            except:
                                pass 
                    # якщо прогресс дорівнює меню то
                    if m_data.progression == "menu":
                        # вибір місця написання
                        m_buttons.input.activate(event) 
                        m_buttons.music.button_start(event)
                        m_buttons.client.button_start(event)
                        m_buttons.server.button_start(event)
                        # перехід в пре-гру етап
                        m_buttons.button_start.button_start(event)
                    # якщо прогресс дорівнює пре-грі то
                    if m_data.progression == "pre-game":
                        # преходить в гру
                        m_buttons.play.button_start(event)
                        # автоматична розтановка кораблів
                        m_buttons.auto.randomship(event.pos)
                        # поворот кораблів
                        m_buttons.rotate.button_start(event)
                        # цикл всіх кораблів
                        for ship in m_data.all_ships:
                            # виділення кораблів
                            ship.activate(event)
                    # якщо прогресс дорівнює грі то
                    if m_data.progression == "game":
                        # вибір місця атаки
                        m_attack.attack(event.pos)
                # якщо будь-яка клавіша натиснута то
                if event.type == pygame.KEYDOWN:
                    # додає символи до input
                    m_buttons.input.edit(event)
                    
                    
                    
            # цикл відображення всього що є в списку
            for sprite in m_data.list_blits[m_data.progression]:
                # print(sprite.name)
                # відображення елементу
                sprite.blit(self.screen)
            if m_data.progression == "menu" and m_audio.track.stoped:
                pygame.draw.line(self.screen,(255,50,50),(42,115,),(120,43),10)
            # якщо знаходимось не в меню то
            if m_data.progression in "pre-game":
                # цикл для відображення всіх кораблів
                for ship in m_data.all_ships:
                    # саме відображення кораблів
                    ship.blit(self.screen)
            if m_data.progression == "game":
                if m_data.turn:
                    m_images.your_turn.blit(self.screen)
                    m_images.opponent_turn_gray.blit(self.screen)
                else:
                    m_images.opponent_turn.blit(self.screen)
                    m_images.your_turn_gray.blit(self.screen)
                # for sprite in m_data.list_blits["game"]:
                #     if sprite.name in "miss, explosion":
                #         sprite.blit(self.screen)
            # оновлення екрану 
            pygame.display.flip()
            # фпс
            self.clock.tick(60)
# створення екземпляру классу
screen = Screen()