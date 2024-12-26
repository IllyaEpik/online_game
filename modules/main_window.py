# імпортуємо модуль pygame
import pygame, threading, os
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.buttons as m_buttons
import modules.data as m_data
import modules.images as m_images
import modules.clients_server as m_client
import modules.ships as m_ships
import modules.attack as m_attack
# import modules.server as m_server
import modules.audio as m_audio


# 
class Screen():
    # ініціалізуємо screen
    def __init__(self):
        size = pygame.display.Info()
        # создаємо таймер
        self.clock = pygame.time.Clock()
        # вказуємо ширину
        self.WIDTH= size.current_w * 0.75
        # вказуємо висоту
        self.HEIGHT = size.current_h * 0.75
        # создаємо екран
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
        

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
        size = pygame.display.Info()
        while game:
            size1 = self.screen.get_size()
            WIDTH = size1[0]
            HEIGHT= size1[1]
            multiplier_x = (WIDTH / 100) / (1280 / 100)
            multiplier_y = (HEIGHT / 100) / (832 / 100)
            # print(width2)
            # print(size,size1)
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
                        m_buttons.nickname.activate(event)
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
                            ship.activate(event, multiplier_x, multiplier_y)
                    # якщо прогресс дорівнює грі то
                    if m_data.progression == "game":
                        # вибір місця атаки
                        m_attack.attack(event.pos)
                # якщо будь-яка клавіша натиснута то
                if event.type == pygame.KEYDOWN and m_data.progression == "menu":
                    # додає символи до input
                    m_buttons.input.edit(event)
                    m_buttons.nickname.edit(event)
                    for object in [m_buttons.nickname]:
                        size = object.FONT.size(object.TEXT)
                        # if object.width < size[0] - 10:
                        width = -(object.start_width - size[0] - 10)
                        object.width = width + object.start_width
                        if object.width < object.start_width:
                            object.width = object.start_width
                        object.update_image()
                        
                        m_buttons.music.rect = pygame.Rect(m_buttons.music.x, m_buttons.music.y,m_buttons.music.width,m_buttons.music.height)
                        m_buttons.music.x = m_buttons.nickname.width + 50
                        # else:
                            # object.width = object.start_width
                            # object.update_image()
                    
            # цикл відображення всього що є в списку
            for sprite in m_data.list_blits[m_data.progression]:
                # print(sprite.name)
                # відображення елементу
                # print(sprite)
                sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            if m_data.progression == "menu" and m_audio.track.stoped:
                pygame.draw.line(self.screen,(255,50,50),
                                 (m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y,),
                                 (m_buttons.music.x*multiplier_x + m_buttons.music.width*multiplier_x,m_buttons.music.y*multiplier_y + m_buttons.music.height*multiplier_y),10)
            # якщо знаходимось не в меню то
            
            if m_data.progression in "pre-game":
                # цикл для відображення всіх кораблів
                for ship in m_data.all_ships:
                    # саме відображення кораблів
                    # print(sprite.x,sprite.y,sprite.width,sprite.height,multiplier_x,multiplier_y,ship.name)
                    # print(sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y,ship.name)
                    ship.blit(self.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
            if m_data.progression == "game":
                if m_data.connected:
                    if m_data.turn:
                        m_images.your_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                        m_images.opponent_turn_gray.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    else:
                        m_images.opponent_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                        m_images.your_turn_gray.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                else:
                    m_buttons.wait.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                # for sprite in m_data.list_blits["game"]:
                #     if sprite.name in "miss, explosion":
                #         sprite.blit(self.screen)
            # оновлення екрану 
            pygame.display.flip()
            # фпс
            self.clock.tick(60)
# створення екземпляру классу
screen = Screen()