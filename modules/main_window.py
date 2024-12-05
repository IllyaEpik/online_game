# імпортуємо модуль pygame
import pygame,threading
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.buttons as m_buttons
import modules.data as m_data
import modules.images
import modules.client as m_client
import modules.ships as m_ships
import modules.attack as m_attack
import modules.server as m_server
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
    # функція запуску
    def run(self):
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
                    try:
                        # відключаємо клієнта
                        m_client.client.close()
                    except:
                        pass 
                # коли кнопка миші натиснута
                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    # якщо прогресс дорівнює меню то
                    if m_data.progression == "menu":
                        # вибір місця написання
                        m_buttons.input.activate(event) 
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
                    # активує клієнта одночасно з роботою кода
                    print(event.key)
                    if event.key == pygame.K_c:
                        print('good')
                        threading.Thread(target = m_client.activate).start()
                    if event.key == pygame.K_s:
                        print('asd')
                        # активує сервер
                        threading.Thread(target = m_server.activate,daemon=True).start()
            # цикл відображення всього що є в списку
            for sprite in m_data.list_blits[m_data.progression]:
                # відображення елементу
                sprite.blit(self.screen)
            # якщо знаходимось не в меню то
            if m_data.progression != "menu":
                # цикл для відображення всіх кораблів
                for ship in m_data.all_ships:
                    # саме відображення кораблів
                    ship.blit(self.screen)
            # оновлення екрану 
            pygame.display.flip()
            # фпс
            self.clock.tick(60)
# створення екземпляру классу
screen = Screen()