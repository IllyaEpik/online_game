# Online game - Sea Battle

* [Ілля Епік / Illya Epik]
* [Денис Бондар / Denys Bondar]
* [Субач Максим / Subach Maksim]
* [Лебідь Ілля / Ilya Lebid]
* [Бобошко Ксюша/ Ksyusha Boboshko]

## Назва проекту: Онлайн гра морський бій/ name project: Online game sea battles

### опис:
* Ця гра дозволяє грати у морський бій удвох на різних комп'ютерах.
#### description:
* This game allows two players to play the sea battles on different computers

#### модулі/modules:
+ pygame; модуль який дозволяе реалізувати саму гру / a module that enables game development.
+ pillow; модуль для роботи pygame / a module for working pygame
+ random; вбудований модуль, який потрібен для генерації випадкових чисел / a built-in which used for generating random numbers.
+ os; вбудований модуль для пошуку абсолютного шляху / a built-in module for finding absolute paths
+ threading; вбудований модуль, який обробляє потоки для одночасних завдань / handles threads for concurrent tasks.
+ socket; вбудований модуль, який дозволяе реалізувати онлайн підключення / a built-in module for enabling online connections.

## інструкція для запуску:
1. Для початку потрібно встановити:
* Python останньої версії
- https://www.python.org/downloads/
* Застосунок для підключення по сеті
- https://www.radmin-vpn.com/

2. Зайти на Git Hub
3. У репозиторії проекту натиснути зелену кнопку "Code"
    ![alt text](images/readme/github_image.png)
4. Обрати "Завантажити ZIP"

* Для Windows
5. Перейти до завантаженого архіву та розархівувати його(Права кнопка миші -> "Витягнути до поточної папки".)
6. Зайти до розархівованої папки і скопіювати шлях:
    ![alt text](images/readme/path_to_folder.png)
7. Натиснути комбінацію **Wind + R**
8. Вписати у віконці:
- cmd
9. У терміналі прописати команду для переходу до файлу:
- cd <шлях>
10. Вести команду для завантаження необхідного модуля:
- pip install pygame
11. Активувати гру за допомогою команди:
- python main.py

* Для macOS
5. Перейти до завантаженого архіву та розархівувати його(двічі клацніть по архіву, щоб розпакувати його автоматично.)
6. Зайти до розпакованої папки і скопіювати її шлях:
7. Правою кнопкою миші на папку -> Оберіть "Get Info" -> Скопіюйте шлях у полі "Where".
8. Натисніть Command + Пробіл, введіть "Terminal" і натисніть Enter.
9. У терміналі прописати команду для переходу до файлу:
- cd <шлях>
10. Вести команду для завантаження необхідного модуля:
- pip3 install pygame
11. Активувати гру за допомогою команди:
- python3 main.py
* Для того щоб підєднатися по сеті:
12. Заходимо в гру

* Перший способ:
13. У грі сервер(один з гравців) повідомляє іншому свій IP та обирає роль сервера
14. Запускає другий етап(обов'язково перший!)
15. Другий гравець вводить IP сервера
16. Вдалої гри!

* Другий способ:
13. Запускаємо застосунок Radmin VPN:
14. Натискаємо на кнопку:
    ![alt text](images/readme/activate_radmin.png)
15. 1) Після цього один з гравців натискає:
    ![alt text](images/readme/server_radmin.png)
15. 1) Він має задати нобхідні данні і надати їх другому гравцю:
    ![alt text](images/readme/create_server_radmin.png)
15. 2) Другий має натиснути:
    ![alt text](images/readme/connect_radmin.png)
15. 2) Та ввести данні які були передані першим гравцем
16. Сервер(один з гравців) повідомляє іншому свій IP з Radmin VPN та обирає роль сервера
17. Другий гравець вводить IP
18. Вдалої гри!

### instructions for launch
1. First, you need to install:  
* The latest version of Python  
- https://www.python.org/downloads/
* Application for connecting over the network
- https://www.radmin-vpn.com/


2. Go to GitHub.  
3. In the project repository, click the green "Code" button.  
   ![alt text](image.png)  
4. Select "Download ZIP." 

* For Windows  
5. Navigate to the downloaded archive and extract it (Right-click -> "Extract to the current folder").  
6. Open the extracted folder and copy the path:  
   ![alt text](images/readme/path_to_folder.png) 
7. Press the **Win + R** key combination.  
8. In the dialog box, enter:  
- cmd  
9. In the terminal, type the command:  
- cd <path> 
10. Run a command to download the required module:
- pip install pygame
11. Launch the game using the command:  
- python main.py 

## структура проекту / project structure:
* Перше вікно: введення IP-адреси/First window: IP address input
* Друге вікно: етап розташування кораблів/Second window: ship placement stage
* Третє вікно: етап битви/Third window: battle stage
* Четверте вікно: результат гри (програш чи перемога)/Fourth window: game result (lose or victory)
* П'яте вікно: екран магазину / Fifth window: shop window
* Шосте вікно: екран з досягненнями / Sixth window: achievement window

### повний опис файлів / a full description of files:

#### Online_game/modules/main_window.py: створення головну екрану гри / create a main screen of game

```python
'''
    >>> Створює головне вікно - класс Screen
'''
# імпортуємо модуль pygame
import pygame, threading, os
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.data as m_data
import modules.buttons as m_buttons
import modules.images as m_images
import modules.clients_server as m_client
import modules.ships as m_ships
import modules.attack as m_attack
import modules.transform as m_transform
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.animations as m_animations
threading.Thread(target=m_animations.play_animation,daemon=True).start()
# клас для налаштування головного вікна
class Screen():
    '''
        >>> Налаштовує головне вікно
    '''
    # ініціалізуємо screen
    def __init__(self):
        size = pygame.display.Info()
        # створюємо таймер
        self.clock = pygame.time.Clock()
        # вказуємо ширину
        self.WIDTH= size.current_w * 0.75
        # вказуємо висоту
        self.HEIGHT = size.current_h * 0.75
        # створюємо екран
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
        self.counter = 0

        # задаємо назву нашому екрану
        pygame.display.set_caption('online game')
        
        icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
        pygame.display.set_icon(icon)
    # функція запуску
    def run(self):
        '''
            >>> Запускає гру
        '''
        # m_data.progression = 'lose'
        # запускаємо гру
        game = True
        self.counter += 1
        
        # налаштування розміра дісплея
        size = pygame.display.Info()
        # поки гра триває
        while game:
            size1 = self.screen.get_size()
            WIDTH = size1[0]
            HEIGHT= size1[1]
            multiplier_x = (WIDTH / 100) / (1280 / 100)
            multiplier_y = (HEIGHT / 100) / (832 / 100)
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
                    if m_transform.type_transform == None:
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
                            m_buttons.achievements.button_start(event)
                            # перехід в пре-гру етап
                            m_buttons.button_start.button_start(event)
                        # якщо прогресс дорівнює пре-грі то
                        elif m_data.progression == 'achievements':
                            m_buttons.achievements_.button_start(event)
                            for achievement in m_data.list_achievements_view:
                                m_data.list_achievements_view[achievement].button_start(event)
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
                            m_attack.attack(event.pos,multiplier_x,multiplier_y)
                            m_buttons.shop.button_start(event)
                            
                        elif m_data.progression == 'shop':
                            m_buttons.shop_.button_start(event)
                            m_buttons.buy.button_start(event)
                            
                            for weapon in m_buttons.list_weapons:
                                weapon.button_start(event=event)
                    # якщо будь-яка клавіша натиснута то
                    else:
                        m_transform.type_transform = None
                        m_transform.size = 0
                if event.type == pygame.KEYDOWN and m_data.progression == "menu":
                    # додає символи в event
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
            m_buttons.coins.TEXT = f"{m_data.coins}"
            # цикл відображення всього що є в списку
            for sprite in m_data.list_blits[m_data.progression]:
                # відображення елементу
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
            if m_data.list_achievements != []:
                achievement = m_data.list_achievements[0]
                achievement.move()
                achievement.blit(self.screen,multiplier_x,multiplier_y)
            if m_data.progression in "pre-game":
                # цикл для відображення всіх кораблів
                for ship in m_data.all_ships:
                    if ship.jump_cor[2]:
                        ship.x += ship.jump_cor[0]
                        ship.y -= ship.jump_cor[1]
                        if not ship.jump_cor[3]:
                            ship.jump_cor[0] /= 1.1
                            ship.jump_cor[1] -= 2.5
                        elif ship.y == 120:
                            ship.jump_cor[3] = False
                            ship.jump_cor[-2] = False
                            
                            m_achievements.achievement('the bug')
                    if ship.y > self.screen.get_size()[1]+1000:
                        ship.y = -100
                        ship.jump_cor[0] =0
                        ship.jump_cor[1] = -20
                        ship.jump_cor[3] = True
                        ship.x = 805
                    # саме відображення кораблів
                    ship.blit(self.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
            if m_data.progression == "game":
                for rocket in m_data.list_rockets:
                    try:
                        if rocket[0].name != 'weapons/line_rocket':
                            x = (725+55.7*rocket[2]) * multiplier_x
                            sprite = rocket[0]
                            sprite.blit(self.screen,
                                        sprite.x*multiplier_x,
                                        sprite.y*multiplier_y,
                                        sprite.width*multiplier_x,
                                        sprite.height*multiplier_y,
                                        multiplier_x,multiplier_y)
                            if rocket[0].x*multiplier_x + rocket[0].width*multiplier_x > x:
                                rocket[3]()
                                m_data.list_rockets.remove(rocket)
                        else:
                            
                            sprite = rocket[0]
                            sprite.blit(self.screen,
                                        sprite.x*multiplier_x,
                                        sprite.y*multiplier_y,
                                        sprite.width*multiplier_x,
                                        sprite.height*multiplier_y,
                                        multiplier_x,multiplier_y)
                            for count in range(10):
                                x = (725+55.7*count) * multiplier_x
                                if rocket[0].x*multiplier_x + rocket[0].width*multiplier_x > x:
                                    last = 0
                                    if str(m_data.enemy_field[rocket[1]][count]) in '1234' or count == 9:
                                        last = 1
                                    rocket[2](rocket[1],count,last)
                                    if last:
                                        m_data.list_rockets.remove(rocket)
                                        m_data.attack = None
                                        break
                    except Exception as error:
                        pass

                count = 0
                list_to_delete = []
                for buff in m_data.my_buffs:
                    if buff[0] == 'Air_Defence':
                        if str(m_data.my_field[buff[1]][buff[2]]) in '05':
                            m_images.air_defence.blit(self.screen,
                                                    (59+buff[2]*55.7)*multiplier_x,
                                                    (115+buff[1]*55.7)*multiplier_y,m_images.air_defence.width*multiplier_x,m_images.air_defence.height*multiplier_y,multiplier_x,multiplier_y
                                                    )
                        else:
                            list_to_delete.append(count)
                    count +=1
                for delete in list_to_delete:
                    del m_data.my_buffs[delete]

                for sprite in m_data.list_explosions:
                    sprite = sprite[0]
                    sprite.blit(self.screen,
                                sprite.x*multiplier_x,
                                sprite.y*multiplier_y,
                                sprite.width*multiplier_x,
                                sprite.height*multiplier_y,
                                multiplier_x,multiplier_y)
                if m_data.time_for_radar:
                    for sprite in m_data.list_for_radar:
                        pygame.draw.circle(self.screen,(50,255,50),((sprite.x+sprite.width/2)*multiplier_x,(sprite.y+sprite.height/2)*multiplier_y),10,25)
            
                if m_data.connected:
                    if m_data.turn:
                        m_buttons.opponent_turn.COLOR = (140, 140, 140)
                        m_buttons.your_turn.COLOR = (0, 0, 255)
                    else:
                        m_buttons.opponent_turn.COLOR = (255, 0, 0)
                        m_buttons.your_turn.COLOR = (140, 140, 140)
                        
                    sprite = m_buttons.shop
                    m_buttons.shop.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.your_turn
                    m_buttons.your_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.opponent_turn
                    m_buttons.opponent_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                else:
                    wait = m_buttons.wait
                    wait.blit(self.screen,wait.x*multiplier_x,wait.y*multiplier_y,wait.width*multiplier_x,wait.height*multiplier_y,multiplier_x,multiplier_y)

            elif m_data.progression == 'achievements':
                square = pygame.Surface((m_buttons.description_.rect.width,m_buttons.description_.rect.height))
                square.fill((255, 255, 255))
                square.set_alpha(200)
                self.screen.blit(square,m_buttons.description_.rect)
                m_buttons.stroke(self.screen,m_buttons.description_.rect,(0,0,0),5)
                sprite = m_buttons.description_
                m_buttons.description_.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
                x,y =50,50
                for achievement_code in m_data.achievements_data:
                    achievement = m_data.achievements_data[achievement_code]
                    
                    if achievement['has'] == 'True':
                        m_data.list_achievements_view[achievement_code].blit(self.screen,
                                 x*multiplier_x,
                                 y*multiplier_y,
                                 150*multiplier_x,
                                 150*multiplier_y,
                                 multiplier_x,multiplier_y)
                        x += 200
                        if x == 850:
                            x = 50
                            y += 200
            # оновлення екрану 
            m_transform.transform(self,multiplier_x,multiplier_y)
            # фпс
            self.clock.tick(60)
# створення екземпляру классу
screen = Screen()
```

#### Online_game/modules/attack.py: створення механіки атаки кораблів / creation of ship attack mechanics
```python
'''
    >>> Відповідає за атаку кораблей
    >>> Перевіряє чи відбулась атака
    >>> Відповідає за роботу зброї
'''
# імпортуємо необхідні модулі
import pygame,random, time, threading,os
import modules.data as m_data
import modules.images as m_images
import modules.clients_server as m_client
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.transform as m_transform
import modules.animations as m_animations
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
attack_list = '012345'
# функція для атаки кораблів в клітинках
def attack_for_cell(row,cell):
    '''
        >>> Відповідає за вибух кораблів
    '''
    # змінна з назвою
    name = None
    # наслідування класа Image для картинки і задання параметрів для неї
    image = m_images.Image(
            progression = "Noke",
            name = "",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            height=55.7,
    )
    # для вибуху кораблів на ворожому полі
    if str(m_data.enemy_field[row][cell]) in list_explosion:
        # вибухи кораблів на ворожому полі
        m_data.enemy_field[row][cell] = 6
        # наслідування класа Animation для анімації і задання параметрів для неї
        image = m_animations.Animation(progression = "Noke",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            name = 'explosion',
            height=55.7)
        # назва змінюється на виьух
        name = "explosion"
        # для атаки з використанням вогненної ракети
        if m_data.attack == 'fire_rocket':
            # назва змінюється на вогонь
            name = 'fire'
            # назва картинки змінюється на вогонь
            image.name = 'fire'
            # вибух корабля на ворожому полі
            m_data.enemy_field[row][cell] = 8
            # атака
            m_data.attack = None
        # додає монети за атаку
        m_data.coins += 10
        # оновлює картинки
        image.update_image()
        # додає параметри до списку з вибухами
        m_data.list_explosions.append([image, row, cell])
        # додає досягнення гравцю
        m_achievements.achievement('It’s a Hit!')
        # список для вибухів
        explosions = []
        # цикл для ворожих кораблів
        for ship in m_data.enemy_ships:
            # перевіряє ворожий корабль
            ship.check_enemy()
            # список з клітинками кораблів
            cells = []
            # цикл для додавання всіх клітинок корабля до cells
            for count in range(int(ship.name)):
                # якщо корабель стоїть горизонтально то
                if ship.rotate %180 == 0 and m_data.enemy_field[ship.row][ship.cell+count] != int(ship.name[0]):
                    # додається клітика
                    cells.append([ship.row, ship.cell+count])
                # інакше якщо корабель стоїть вертикалюно то
                elif ship.rotate %180 != 0 and m_data.enemy_field[ship.row+count][ship.cell] != int(ship.name[0]):
                    # додається клітинка
                    cells.append([ship.row+count, ship.cell])
            # назва корабля повинна дорівнювати довжині клітинок
            if int(ship.name) == len(cells):
                # для вибухів в списку вибухів
                for explosion in m_data.list_explosions:
                    # цикл для клітинок
                    for celll in cells:
                        # якщо вибухи дорівнюють клітинкам то
                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                            # до вибухів додається 0
                            explosions.append(explosion[0])
        # цикл минулих для вибухів
        for ex in explosions:
            try:
                # до списку додається значення 'game' і прибирається минулиц вибух
                m_data.list_blits['game'].remove(ex)
            except:
                pass
    # інакше промах на воожому полі
    elif str(m_data.enemy_field[row][cell]) in list_miss:
        # нове досягнення
        m_achievements.achievement('Missed Shot')
        # для атаки вогненної ракети
        if m_data.attack == 'fire_rocket':
            # атака
            m_data.attack = None
        # промах на ворожому полі
        m_data.enemy_field[row][cell] = 7
        # зміна назви на промах
        name = "miss"
        # зміна назви картинки на промах
        image.name = 'miss'
        # оновлення картинки
        image.update_image()
        # зміна ходу
        m_data.turn = False
        # додає параметри до списку з вибухами
        m_data.list_explosions.append([image, row, cell])
    # повертає назву
    return name
# функція для часу радара
def timer_for_radar():
    '''
        >>> Відповідає за час роботи(таймер) радару
    '''
    # поки радар працює
    while m_data.time_for_radar:
        # від часу віднімається 1 секунда
        m_data.time_for_radar -= 1
        # пауза на 1 секунду
        time.sleep(1)
    # якщо не має ходу
    if not m_data.turn:
        # відправляє пропуск в m_client
        m_client.send("pass:")
# список для відправки всього необхідного
need_to_send = []
# метод з атакою
def attack(pos: tuple,multiplier_x,multiplier_y):
    '''
        >>> Відповідає за атаку кораблів зі зброєю
    '''
    # створення глобальних змінних
    global list_miss, list_explosion
    # blits = True
    # текст для відправки
    text_for_send = ''
    # зміна ходу і підключення
    if m_data.turn and m_data.connected and not m_data.list_rockets:
        # цикл для атаки самонаводящою ракетою
        if m_data.attack == 'homing_rocket':
            # функція з вогнем
            fire()
            # список кораблів
            list_ships = []
            # для кораблів на ворожому полі
            for ship in m_data.enemy_ships:
                # якщо не кораблі в всіх кораблях то
                if not ship in m_data.all_ships:
                    # до списку кораблів додається корабель
                    list_ships.append(ship)
            # головний корабель, його поворот і довжина списку кораблів
            main_ship = list_ships[random.randint(0,len(list_ships)-1)]
            # головна клітинка і віднімання 1 значення від корабля
            main_cell = random.randint(0,int(main_ship.name)-1)
            # головний ряд
            main_row = main_ship.row
            # поворот кораблів
            rotate_ship = main_ship.rotate
            # перевірка розвороту корабля
            if rotate_ship % 180 == 0:
                # головна клітинка додається до головного корабля
                main_cell += main_ship.cell
                # name = attack_for_cell(main_ship.row,main_cell + main_ship.cell)
                # m_client.send(f"attack:{ main_ship.row},{main_cell + main_ship.cell},{name}".encode())
            else:
                # головна клітинка додається до головного корабля
                main_row += main_cell
                # нове досягнення
                # головна клітинка дорівнює головному кораблю
                main_cell = main_ship.cell
            # наявнісь ефектів
            for buff in m_data.buffs:
                # якщо ефект протиповітряної оборони
                if buff[0] == 'Air_Defence':
                    # список клітинок
                    list_cells = []
                    # ефект в ряду
                    buff_row = int(buff[1])
                    # ефект в клітинці
                    buff_cell = int(buff[2])
                    # для ракети в ряд
                    for row_air in range(5):
                        # для ракети по клітинкам
                        for cell_air in range(5):
                            # до ефекту в ряд додається ракета в ряд
                            row = buff_row + row_air-2
                            # до ефекту по клітинкам додається ракета по клітинкам
                            cell = buff_cell + cell_air-2
                            # перевірка значення в ряду і клітинці
                            if -1 < row < 10 and -1 < cell < 10:
                                # до списку клітинок додаються параметри: ряд і клітинка
                                list_cells.append([row,cell])
                    # для клітинок в повітрі в списку клітинок 
                    for cell_for_air in list_cells:
                        # якщо клітинки мають однакові значення
                        if main_row == cell_for_air[0] and main_cell == cell_for_air[1]:
                            # в ряду ефект в ряд
                            main_row = buff_row
                            # в клітинці ефект в клітинку
                            m_achievements.achievement('Closed Skies')
                            main_cell = buff_cell
                            # видалення ефекту
                            m_data.buffs.remove(buff)
            # if can_attack:
            def atta(main_row,main_cell):
                '''
                    >>> Відповідає за хід після атаки
                '''
                # функція атаки для клітинок
                name = attack_for_cell(main_row,main_cell)
                # текст для відправки: атака
                text_for_send = f"attack:{main_row},{main_cell},{name};"
                # if name: 
                # атака
                m_data.attack = None
                # зміна ходу
                m_data.turn = False
                # для ефекту в ефектах
                for buff in m_data.buffs:
                    # якщо ефект енергетик
                    if buff[0] == 'Energetic':
                        # зміна ходу
                        m_data.turn = True
                # якщо не має ходу
                if not m_data.turn:
                    # текст для відправки: пропуск
                    text_for_send+= 'pass:'
                win_lose(text_for_send) 
                m_audio.explosion.play()
            
            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*main_row,f'weapons/homing_rocket','Noke',0),main_row,main_cell,lambda:atta(main_row,main_cell),0))
            try:
                #
                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
            except:
                pass
            ## 59, 115
            # звук вибуху
        # атака протиповітряної оборони
        elif m_data.attack == 'Air_Defence':
            # функція вогню
            fire()
            # цикл для ряду
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    # створюємо хіт-бокс
                    rect = pygame.Rect((59+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію
                    if rect.collidepoint(pos) and str(m_data.my_field[row][cell]) in '05':
                        # до моїх ефектів додається протиповітряна оборона
                        m_data.my_buffs.append(['Air_Defence',row,cell])
                        # текст для відправки: ефект протиповітряної оборони
                        text_for_send+=f'buff:Air_Defence,{row},{cell};'
                        # атака
                        m_data.attack = None
                        # зміна ходу
                        m_data.turn = False
                        # цикл для ефекту в ефектах
                        for buff in m_data.buffs:
                            # якщо ефект енергетик
                            if buff[0] == 'Energetic':
                                # зміна ходу
                                m_data.turn = True
                        # якщо не має ходу
                        if not m_data.turn:
                            # текст для відправки: пропуск
                            text_for_send+='pass:;'
        else:
            #
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    
                    # створюємо хіт-бокс
                    rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію

                    if rect.collidepoint(pos) and str(m_data.enemy_field[row][cell]) in attack_list:
                        # якщо атака ракетою 3x3
                        if m_data.attack == 'rocket_3x3':
                            # текст: атака
                            def atta(row,cell):
                                '''
                                    >>> Відповідає за атаку ракетою 3x3
                                '''
                                text = 'attack:'
                                # цикл для ракети 3х3
                                for row_3x3 in range(3):
                                    # цикл для ракети 3х3
                                    for cell_3x3 in range(3):
                                        # перевірка ракети в клітинках 3х3
                                        if -1 < row+row_3x3-1 < 10 and -1 < cell+cell_3x3-1 < 10:
                                            # атака для клітинок
                                            name = attack_for_cell(row+row_3x3-1,cell+cell_3x3-1)
                                            # текст для ракети 3х3 в ряду і клітинці
                                            text += f'{row+row_3x3-1},{cell+cell_3x3-1},{name},1 '
                                # до тексту додаємо символ ";"
                                # атака
                                m_data.attack = None
                                # функція вогню
                                fire()
                                m_audio.explosion.play(1)
                                win_lose(text + ';')
                            # змінна для тимчасового збереження рядка   
                            ok,ok1 = row,cell 
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/rocket_3x3','Noke',0),ok,ok1,lambda:atta(ok,ok1),0))
                            try:
                                #
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass
                        # атака дінійною ракетою  
                        elif m_data.attack == 'line_rocket':
                            fire()
                            # функція для атаки
                            def atta(row,cell,last = 0):
                                '''
                                    >>> Відповідає за атаку в клітинках
                                '''
                                # функція вогню
                                # даємо назву - атака для клітинок
                                name = attack_for_cell(row,cell)
                                # змінна текст
                                text = ''
                                # якщо назва - атака для клітинок
                                if name: 
                                    # виграш або програш 
                                    # win_lose(f"attack:{row},{cell},{name}")
                                    if last:
                                        win_lose(m_data.list_rockets[-1][-1]+f"{row},{cell},{name}")
                                        # звук вибуху
                                        m_audio.explosion.play() 
                                    else:
                                        # m_data.list_rockets[-1][-1]+=f"{row},{cell},{name} "
                                        win_lose(f"attack:{row},{cell},{name},0")
                                
                            # змінна для тимчасового збереження рядка   
                            ok = row
                            
                            # до списку ракет додаємо параметри
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/line_rocket','Noke',0),ok,atta,'pass;attack:'))
                            try:
                                # запуск списку ракет, їх анімація
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass
                                # elif str(m_data.enemy_field[row][cell]) in '05':
                        # атака радаром
                        elif m_data.attack == 'radar':
                            # функція вогню
                            fire()
                            # нове досягнення
                            m_achievements.achievement('used radar')
                            # змінюємо ширину
                            width = 55.7 * multiplier_x
                            # змінюємо висоту
                            height = 55.7 * multiplier_y
                            # змінюємо розташування по x
                            x = (725+55.7*cell) * multiplier_x
                            # змінюємо розташування по y
                            y = (115+55.7*row) * multiplier_y
                            # задаємо початок клітинок
                            start_cell = cell
                            # задаємо початок рядів
                            start_row = row
                            # задаємо кінець клітинок
                            end_cell = cell
                            # задаємо кінець рядів
                            end_row = row
                            # перевіряємо розташування рядів
                            if row > 1:
                                # змінюємо параметри ширини, x і початку ряду
                                width += 55.7 * multiplier_x *2
                                x -= 55.7 * multiplier_x *2
                                start_row -= 2
                            # перевіряємо розташування рядів
                            elif row == 1:
                                # змінюємо параметри ширини, x і початку ряду
                                width += 55.7 * multiplier_x
                                x -= 55.7 * multiplier_x
                                start_row -= 1
                            # перевіряємо розташування рядів
                            if row < 8:
                                # змінюємо параметри ширини і кінця ряду
                                width += 55.7 * multiplier_x*2
                                end_row += 2
                            # перевіряємо розташування рядів
                            elif row == 8:
                                # змінюємо параметри ширини і кінця ряду
                                width += 55.7 * multiplier_x
                                end_row += 1
                            # перевіряємо розташування клітинок
                            if cell < 8:
                                # змінюємо параметри висоти і кінця клітинок
                                height += 55.7 * multiplier_y*2
                                end_cell += 2
                            # перевіряємо розташування клітинок
                            elif cell == 8:
                                # змінюємо параметри висоти і кінця клітинок
                                height += 55.7 * multiplier_y
                                end_cell += 1
                            # перевіряємо розташування клітинок
                            if cell > 1:
                                # змінюємо параметри висоти, y і початку клітинок
                                start_cell -=2
                                height += 55.7 * multiplier_y*2
                                y -= 55.7 * multiplier_y * 2 
                            # перевіряємо розташування клітинок
                            elif cell == 1:
                                # змінюємо параметри висоти, y і початку клітинок
                                start_cell -=1
                                height += 55.7 * multiplier_y
                                y -= 55.7 * multiplier_y
                            # поле для радару
                            m_data.rect_for_radar = pygame.Rect(x,y,width,height)
                            # список для радару
                            m_data.list_for_radar = []
                            # звук радару
                            m_audio.radar.play()
                            # цикл для ряду
                            for row2 in range(10):
                                # цикл для клітинки
                                for cell2 in range(10):
                                    # перевірка першого і останнього ряда
                                    if row2 >= start_row and row2 <= end_row:
                                        # перевірка першої клітинки і останньої
                                        if cell2 >= start_cell and cell2 <= end_cell:
                                            # перевірка розташування кораблів на ворожому полі
                                            if str(m_data.enemy_field[row2][cell2]) in '1234':
                                                # додаємо до списку з радаром:
                                                m_data.list_for_radar.append(
                                                    # наслідуємо клас Image і задаємо параметри
                                                    m_images.Image(55.7,
                                                                55.7,
                                                                725+55.7*cell2,
                                                                115+55.7*row2,
                                                                'explosion',
                                                                progression='Noke')
                                                                )
                            # ставимо час для роботи радару 5 секунд
                            m_data.time_for_radar = 5
                            # запускаємо час дії радару
                            threading.Thread(target= timer_for_radar,daemon = True).start()
                            # атакуємо
                            m_data.attack = None
                            # змінюємо ход
                            m_data.turn = False
                            # для ефекту в ефектах
                            for buff in m_data.buffs:
                                # якщо ефект - енергетик
                                if buff[0] == 'Energetic':
                                    # дозволяємо ходити
                                    m_data.turn = True
                        
                        else:
                            # функція для атаки
                            def atta(row,cell):
                                '''
                                    >>> Відповідає за атаку по клітинкам
                                '''
                                # функція вогню
                                fire()
                                # даємо назву - атака для клітинок
                                name = attack_for_cell(row,cell)
                                # змінна текст
                                text = ''
                                # якщо назва - атака для клітинок
                                if name: 
                                    # виграш або програш                                  
                                    win_lose(f"attack:{row},{cell},{name}")
                                    # звук вибуху
                                    m_audio.explosion.play()
                            # змінна для тимчасового збереження рядка   
                            ok,ok1 = row,cell
                            # створення назви для звичайної ракети
                            name_for_rocket = 'standart_rocket'
                            # якщо атака вогняною ракетою, то
                            if m_data.attack == 'fire_rocket':
                                # назва ракети змінюється на вогняну ракету
                                name_for_rocket = 'fire_rocket'
                            # до списку ракет додаємо параметри
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/{name_for_rocket}','Noke',0),ok,ok1,lambda:atta(ok,ok1),0))
                            try:
                                # запуск списку ракет, їх анімація
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass

        # if text != 'fire:':
        #     text_for_send+= ';'+text
        
        # функція для перемоги і програшу
        win_lose(text_for_send)
# функція для вогню
def fire():
    '''
        >>> Відповідає за горіння кораблів
    '''
    # робимо змінну необхідної для відправки глобальною
    global need_to_send
    # текст для вогню
    text = 'fire:'
    # цикл для перевірки рядів
    for row in range(10):
            # перевіряємо ряди на полі
            if 8 in m_data.my_field[row]:
                # цикл для перевірки клітинок
                for cell in range(10):
                    #  перевіряємо кількість ряди на полі
                    if m_data.my_field[row][cell] == 8:
                        # цикл для вогню в ряд
                        for row_fire in range(3):
                            # цикл для вогню в клітинках
                            for cell_fire in range(3):
                                # перевіряємо ряди і вогонь в рядах
                                if -1 < (row_fire + row-1) < 10:
                                    # перевіряємо клітинки і вогонь в клітинках 
                                    if -1 < (cell_fire + cell-1) < 10:
                                        # перевіряємо вибухи на полі в списку вибухів
                                        if str(m_data.my_field[row+row_fire-1][cell+cell_fire-1]) in list_explosion:
                                            # 9 рядів і клітинок на полі
                                            m_data.my_field[row+row_fire-1][cell+cell_fire-1] = 9
    # цикл для рядів
    for row in range(10):
        # якщо на полі є 9 рядів
        if 9 in m_data.my_field[row]:
            # цикл для клітинок
            for cell in range(10):
                # якщо на полі 9 рядів і клітинок
                if m_data.my_field[row][cell] == 9:
                    # до тексту записується ряд і клітинка
                    text += f'{row},{cell} '
                    # 8 рядів і клітинок на полі
                    m_data.my_field[row][cell] = 8
                    # наслідування класу Animation для картинки анімацій і задаємо параметри
                    image = m_animations.Animation(
                            progression = "Noke",
                            name = 'fire',
                            x = 59+55.7*cell,
                            y = 115+55.7*row,
                            # 5 9 4
                            width= 55.7,
                            height=55.7
                        )
                    # до списку вибухів додаємо картинку, ряд і клітинку
                    m_data.list_explosions.append([image,row,cell])
    # якщо текст не дорвнює вогню
    if text != 'fire:':
        # додаємо символ ';' до змінної необхідного для відправки
        need_to_send.append(';' + text)
    # return text
# функція для виграшу та поразки
def win_lose(text_for_send):
    '''
        >>> Відповідає за виграш та програш
    '''
    # робимо змінну необхідної для відправки глобальною
    global need_to_send
    # змінна да_ні
    yes_no = True
    # цикл для корабля в ворожих кораблях
    for ship in m_data.enemy_ships:
        # якщо немає вибуху корабля
        if not ship.explosion:
        # elif :
            # змінна да_ні змінюється на False
            yes_no = False
    # перевірка да_ні і ворожих кораблів
    if yes_no and m_data.enemy_ships:
        # зміна кольору
        m_transform.color = (25,255,25)
        # зміна типу переходу
        m_transform.type_transform = 0
        # перехід на вікно перемоги
        m_data.progression = "win"
        # нове досягнення
        m_achievements.achievement('Like a Clap of Hands')
        # змінна може
        can= True
        # цикл для рядів на полі
        for row in m_data.my_field:
            # цикл для клітинок в ряду
            for cell in row:
                # перевірка клітинок
                if cell == 6 or cell == 8:
                    # не може
                    can = False
                    # зупинка
                    break 
        # умова для досягнення
        if can:
            # нове досягнення
            m_achievements.achievement('Total Domination')
        # додається перемога
        m_data.read_data['wins']+= 1
        # записується в дату
        m_data.reading_data(m_data.read_data,'date.txt')
        # якщо ьільше ніж 2 перемоги, то
        if m_data.read_data['wins'] > 2:
            # нове досягнення
            m_achievements.achievement('Smells Like Victory')
            #
            if m_data.read_data['wins'] > 49:
                # нове досягнення
                m_achievements.achievement('True Cossack')
        # перевірка наявних монет 
        if m_data.coins == 200:
            # нове досягнення
            m_achievements.achievement('Need More Gold!')
        #
        elif m_data.coins == 190:
            # нове досягнення
            m_achievements.achievement("Big Spender")
        # до тексту для відправки додається програш
        text_for_send += ";lose:?????"
    # перевірка тексту для відправки
    if text_for_send:
        # змінна додати
        add = ''
        # якщо хід не змінюється
        if not m_data.turn:
            # пропуск ходу
            add = ';pass:'
        # перевірка необхідного для відправки
        if need_to_send:
            # до тексту додаємо символ ';'
            text_for_send +=';' + ";".join(need_to_send)
            # список для необхідного для відправки
            need_to_send = []
        # відправляємо все в клієнта
        m_client.send(text_for_send + add)
```

#### Online_game/modules/buttons.py: створення необхідних кнопок для застосунку / сreation of necessary buttons for the application
```python
'''
    >>> Відповідяє за створення всіх кнопок - клас Button
    >>> Відповідає за функції при натисканні кнопок - метод button_start 
'''
# імпорт чужих модулів для роботи
import pygame , socket, os
import threading, random
import getpass
# імпорт наших модулів
import modules.audio as m_audio
from modules.images import Image
import modules.transform as m_transform
import modules.data as m_data
import modules.clients_server as m_client 
import modules.achievements as m_achievements
import modules.attack as m_attack
# import modules.server as m_server
from modules.ships import Ship,fill_field
def stroke(screen,rect:pygame.Rect,color = (0,0,0),width = 5,multiplier_x = 1,multiplier_y = 1):
    '''
        >>> Малює обведення
    '''
    pygame.draw.line(screen,color,
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y+rect.height)*multiplier_y),
                     (int(rect.x*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))

# класс з кнопками
class Button(Image):
    '''
        >>> Додає параметри до класу зображень
    '''
    # метод з створенням параметрів
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text: str ="Button", size = 65, color = (0, 0, 0),rotate = 0):
        # задаємо параметри в класс зображень
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression,rotate=rotate)
        # переносимо параметри в змінні
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.TEXT = text  
        self.render = None
        self.last_text = None
        self.activate = 0
        # створюємо параметри
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", size)
        self.rect = pygame.Rect(x,y,width,height)
        self.size = size 
        self.start_size = size
        self.current_size = self.size
    # метод з кнопкою старт
    def button_start(self, event):
        '''
            >>> Створює кнопку старт
            >>> Перевіряє чи кнопка натиснута
        '''
        if type(event) == pygame.event.Event:

            pos = event.pos
        else:
            pos = event
        # якщо кнопка натиснута
        if self.rect.collidepoint(pos):
            if type(self.function) == type("123") and self.function.split(":")[0] == "c_s":
                m_data.client_server = self.function.split(":")[1]
                server.COLOR = (0,0,0)
                client.COLOR = (0,0,0)
                self.COLOR =(40,2,255)
            # якщо функція корабль то
            elif self.function == "ship":
                # цикл для всіх кораблів
                for ship in m_data.all_ships:
                    # якщо корабль виділен
                    if ship.select:
                        # поворот корабля   
                       ship.rotate_ship()
                        # виділення корабля
                       ship.select  = False
            elif self.function == "music":
                if m_audio.track.stoped:
                    m_audio.track.play()
                    # self.name = "music"
                else:
                    m_audio.track.stop()
                    # self.name = "music_off"
                # self.update_image()
            elif self.function == "win_lose":
                m_data.revenge = True
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                m_data.progression = "pre-game"
                
                size_ship = "1"
                m_data.enemy_ships = []
                m_data.all_ships = []
                # Створення списку, у якому зберігаеться усе наше поле
                m_data.my_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

                # Створення списку, у якому зберігаеться усе поле ворога
                m_data.enemy_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                m_data.turn = True
                # list_count = []
                m_data.list_blits["game"] = []
                m_data.list_explosions = []
                play_field = Image(width = 1280, height = 851, x = 0, y = 0, name = "play_field", progression = "game", edit = False)
                # for count in range(len(m_data.list_blits["game"])):
                #     if m_data.list_blits["game"][count].name in "miss, explosion":
                #         list_count += [count]
                # for count in range(len(list_count)):
                #     del m_data.list_blits["game"][list_count[-(count + 1)]]
                for count in range(10):
                    ship = Ship(x=59, y=115, name=size_ship)
                    ship.select = True
                    ship.place((684, 220))
                    ship.select = False
                    if count == 3:
                        size_ship = "2"
                    if count == 6:
                        size_ship = "3"
                    if count == 8:
                        size_ship = "4"
            elif self.function == "check":
                return True
            elif self.function == "buy":
                try:
                    if not m_data.attack:
                        if m_data.cost_data[m_data.select_weapon] <= m_data.coins:
                            m_data.coins -= m_data.cost_data[m_data.select_weapon]
                            m_achievements.achievement('Hooked')
                            m_audio.buying.play()
                            if 'Energetic' == m_data.select_weapon:
                                m_data.buffs.append(['Energetic'])
                                # m_client.send('buff:Energetic')
                            elif "Anti_fire"== m_data.select_weapon:
                                add = ';pass'
                                for buff in m_data.buffs:
                                    if buff[0] == 'Energetic':
                                        add = ''
                                m_client.send('Anti_fire:'+add)
                                if add:
                                    m_data.turn = False
                                for row in range(10):
                                    if 8 in m_data.my_field[row]:
                                        for cell in range(10):
                                            if m_data.my_field[row][cell] == 8:
                                                m_data.my_field[row][cell] = 6
                                for explosion in m_data.list_explosions:
                                    if explosion[0].name == 'fire' and explosion[0].x < 725:
                                        explosion[0].name = 'explosion'
                                        explosion[0].update_image()
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                m_data.progression = "game"
                                                        # m_attack.need_to_send.append('Anti_fire:')
                                                        
                            else:
                                m_data.attack = m_data.select_weapon
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                m_data.progression = "game"
                except:
                    pass
            elif self.function == 'shop':
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                if m_data.progression == 'shop':
                    m_data.progression = "game"
                    m_data.select_weapon = None
                else:
                    m_data.progression = 'shop'
                    m_achievements.achievement("New Opportunities")
            elif self.function == 'achievements':
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                if m_data.progression == 'achievements':
                    m_data.progression = "menu"
                else:
                    m_data.progression = 'achievements'
            # інакше функція гра
            elif self.function == "play":

                # змінна да_ні дорівнює правді
                yes_no = True
                # цикл для стандартних клітинок
                for row in m_data.cells:
                    # цикл для клітинок в ряду
                    for cell in m_data.cells[row]:
                        # якщо кораблі не розставлені
                        if cell[0]:
                            # змінна да_ні змінюється на неправду 
                            yes_no =  False
                # якщо всі кораблі розставлені
                if yes_no:
                    # переходимо в гру
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    m_data.progression = "game"
                    icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
                    pygame.display.set_icon(icon)
                    if not m_data.revenge:
                        # if m_data.client_server == "client" or not m_data.client_server:
                            # активує клієнта одночасно з роботою кода
                        threading.Thread(target = m_client.activate,daemon=True).start()
                        # if m_data.client_server == "server" or not m_data.client_server:
                            # активує сервер
                            # threading.Thread(target = m_server.activate,daemon=True).start()
                        # 
                    else:
                        ships = "field:"
                        for ship in m_data.all_ships:
                            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
                        # визиваємо функцію для відправки даних на сервер
                        m_client.send(ships.encode()) 

            elif self.function and 'set_achievement' in self.function:
                description_.TEXT = (self.name.split('/')[1]+': '+m_data.achievements_data[self.function.split('/')[1]]['description']).split(' ') +['                ', '           ']
                m_data.select_weapon = self.name.split('/')[1]
                size = description_.FONT.size(" ".join(description_.TEXT))
                if size[0] < description_.rect.width:
                    description_.TEXT = [" ".join(description_.TEXT)]
                elif len(description_.TEXT)-2:
                    list_text = []
                    text = ''
                    
                    for text_for in description_.TEXT:
                        size = description_.FONT.size(text+text_for)
                        if size[0] < description_.rect.width:
                            text += text_for + ' '
                        elif size[0] > description_.rect.width:
                            list_text.append(text)
                            text = text_for + ' '
                        elif description_.TEXT[-1] == text_for + ' ':
                            list_text.append(text)
                    if text_for in list_text[-1]:
                        pass
                    else:
                        size = description_.FONT.size(text+text_for)
                        if size[0] < description_.rect.width:
                            text += text_for
                        elif size[0] > description_.rect.width:
                            list_text.append(text)
                            list_text.append(text_for)
                        elif description_.TEXT[-1] == text_for:
                            list_text.append(text)
                    description_.TEXT =  list_text
            elif self.function and 'weapons' in self.function:
                # buff
                
                description.TEXT = m_data.weapon_data[self.function.split('/')[1]][self.function.split('/')[2]].split(' ') +['                ', '           ']
                m_data.select_weapon = self.function.split('/')[2]
                multiplers = [
                    self.rect.width/self.width,
                    self.rect.height/self.height
                ]
                if multiplers[0] > multiplers[1]:
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[1])))
                else:
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[0])))
                size = description.FONT.size(" ".join(description.TEXT))
                if size[0] < description.width*multiplers[0]:
                    description.TEXT = [" ".join(description.TEXT)]
                elif len(description.TEXT)-2:
                    list_text = []
                    text = ''
                    
                    for text_for in description.TEXT:
                        size = description.FONT.size(text+text_for)
                        if size[0] < description.width*multiplers[0]:
                            text += text_for + ' '
                        elif size[0] > description.width*multiplers[0]:
                            list_text.append(text)
                            text = text_for + ' '
                        elif description.TEXT[-1] == text_for + ' ':
                            list_text.append(text)
                    if text_for in list_text[-1]:
                        pass
                    else:
                        size = description.FONT.size(text+text_for)
                        if size[0] < description.width*multiplers[0]:
                            text += text_for
                        elif size[0] > description.width*multiplers[0]:
                            list_text.append(text)
                            list_text.append(text_for)
                        elif description.TEXT[-1] == text_for:
                            list_text.append(text)
                    description.TEXT = [self.function.split('/')[2]+': '] +  list_text
            else:
                if m_data.client_server and nickname.TEXT:
                    # записання ip
                    ip = input.TEXT.split(": ")
                    del ip[0]
                    ip = ": ".join(ip)
                    m_data.ip = ip
                    if m_data.ip == "":
                        m_data.ip = m_client.ip
                    with open(m_data.path+m_data.type+'data.txt', "w") as file:
                        file.write(f"{nickname.TEXT}\n{m_data.ip}\n{not m_audio.track.stoped}\n{m_data.client_server}")
                    # перехід в пре-гру"
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    m_data.progression = "pre-game"
    # метод відображення поверхні на головному окні
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        # якщо картинка задана 
        self.rect = pygame.Rect(x,y,width,height)
        if self.name != "":
            # відображення картинки 
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            self.current_size= int((self.size*(multiplier_y/2)))
            # self.size = int((self.size*multiplier_y))
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            self.FONT = pygame.font.SysFont("algerian", int((self.size*(multiplier_x))))
            self.current_size = int((self.size*multiplier_x))
            
        if type(self.TEXT) == type(""):
            size = self.FONT.size(self.TEXT) 
            # задаємо y для тексту
            y = y + height/2-size[1]/2
            # задаємо x для тексту
            x = x + width/2-size[0]/2
            # if self.TEXT != self.last_text:
                # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
            render = self.FONT.render(self.TEXT,True,self.COLOR)
            render.set_alpha(self.opasity)
            screen.blit(render, (x, y))
            self.last_text = self.TEXT
            # else:
            #     screen.blit(self.render, (x, y))
            # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
        elif type(self.TEXT) == type([]):
                
            count = 0
            # while True:
            for text in self.TEXT:
                if multiplier_x > multiplier_y:
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
                else:
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
                height = self.FONT.size(text)[1]
                size = self.FONT.size(text) 
                y = (self.rect.y+10+height*count) * multiplier_y
                # задаємо x для тексту 
                x = (self.rect.x)*multiplier_x
                # відображення тексту на екрані
                render = self.FONT.render(text,True,(0,0,0))
                render.set_alpha(self.opasity)
                screen.blit(render, (self.rect.x, y))
                count += 1
        # y = y + height/2-size[1]/2
        # # задаємо x для тексту 
        # x = x + width/2-size[0]/2
        # # відображення тексту на екрані
        # size = self.FONT.size(self.TEXT)

        # size[0] = multiplier_x * size[0]
        # size[1] = multiplier_y * size[1]
        # задаємо y для тексту

# button = Button()
class Input(Image):
    '''
        >>> Додає параметри до картинки
    '''
    def __init__(self, width: int, height: int,x = 0,y = 0, name = "", progression = "menu", color = (0,0,0), text = "ip: ", list = "0123456789."):
        self.start_width = width 
        self.start_height = height 
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", 65)
        self.TEXT = text 
        self.RENDER_TEXT = None
        self.enter = False
        self.edit("ok")
        self.rect = pygame.Rect(x,y,width,height)
        self.list = list
        self.size = 65 
        self.current_size = self.size
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        if self.name != "":
            # відображення картинки
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        # s = pygame.time.get_ticks()
        # задання розміру для тексту
        self.rect = pygame.Rect(x,y,width,height)
        if self.list == 'any':
            self.x = 42
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            self.current_size= int((self.size*multiplier_y))
            # self.size = int((self.size*multiplier_y))
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_x)))
            self.current_size = int((self.size*multiplier_x))
        size = self.FONT.size(self.TEXT)
        # задаємо y для тексту
        y = y + height/2-size[1]/2
        # задаємо x для тексту
        x = x + width/2-size[0]/2
        render = self.FONT.render(self.TEXT,True,self.COLOR)
        render.set_alpha(self.opasity)
        screen.blit(render, (x, y))
        self.rect = pygame.Rect(x,y,width,height)
        # відображення тексту на екрані
    def activate(self, event):
        '''
            >>> Відповідає за виділення поля ввода
        '''
        if self.rect.collidepoint(event.pos):
            self.enter = True
        else:
            self.enter = False
    def edit(self,event):
        '''
            >>> Редагує текст
        '''
        if self.enter:
            key = pygame.key.name(event.key)
            if event.key == pygame.K_BACKSPACE and self.TEXT != "ip: ":
                # прибирає останній символ текста 
                self.TEXT = self.TEXT[:-1]
            elif key in self.list or self.list != "0123456789." and len(key) == 1:
                # 
                self.TEXT += key

        self.RENDER_TEXT = self.FONT.render(self.TEXT, True, self.COLOR)
class Auto(Image):
    '''
        >>> Випадково розставляє кораблі
    '''
    def __init__(self, width: int, height: int, x: int, y: int, name='', progression: str = "pre-game"):
        super().__init__(width, height, x, y, name, progression)
        self.rect = pygame.Rect(x,y,width,height)
        m_data.list_blits["pre-game"].append(self)
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає кнопку на екрані
        '''
        self.rect = pygame.Rect(x,y,width,height)
        # pygame.draw.rect(screen,(255,25,25),self.rect)
    def randomship(self, cor):
        '''
            >>> Випадково розставляє кораблі
        '''
        if self.rect.collidepoint(cor):
            count = 0
            count_ships = 0  
            m_data.my_field = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            m_data.all_ships = []
            for row in m_data.cells:
                for cell in m_data.cells[row]:
                    cell[0] =  False
            # for ship in m_data.all_ships:
                
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                if m_data.my_field[row][cell] ==  0:
                    ship = Ship(x = 59, y = 115, cell = cell, row = row, rotate = rotate * 90)
                    count_ships += 1
                    m_data.my_field[row][cell] = 1
                    fill_field(m_data.my_field)
                if count_ships == 4 or count > 1000:
                    break
                
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try: 

                    if m_data.my_field[row][cell] == 0: 
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1: 
                            ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "2", rotate = rotate * 90)
                            count_ships += 1
                            fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 3 or count > 1000:
                    break

            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] == 0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "3", rotate= rotate * 90)
                                count_ships += 1
                                fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 2 or count > 1000:
                    break
            
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] ==  0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                if m_data.my_field[row][cell+3] == 0 and rotate % 2 == 0 or m_data.my_field[row+3][cell] == 0 and rotate % 2 == 1:
                                    ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "4", rotate= rotate * 90)
                                    count_ships += 1
                                    fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 1 or count > 1000:
                    break
            if count > 1000:
                self.randomship(cor)


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ip1 = ""
nick = getpass.getuser()
if m_data.read_data["nickname"] != "":
    nick = m_data.read_data["nickname"]
if "." in m_data.read_data["ip"]:
    ip1 = m_data.read_data["ip"]
button_start = Button(width = 402 , height = 120, x = 435, y = 370, name = "", text= "start")
m_data.list_blits["menu"].append(button_start)

input = Input(width = 496, height = 148, x = 387 , y = 568, name = "button_start", text = f"ip: {ip1}")
nickname = Input(x= 42, y= 43, width= 281, height= 84, name = "button_start", text = nick, list = "any")
ip = Button(x = 981, y = 59, width = 281, height = 84, name = "button_start", text = m_client.ip, size = 50)
for object in [nickname, ip]:
    size = object.FONT.size(object.TEXT)
    if object.width - size[0] - 10 < 0:
        width = -(object.width - size[0] - 10)
        object.x -= width
        object.width += width
        object.update_image()
text_ip = Button(x = ip.x, y = 10, width = ip.width, height = 45, text = "user ip", size = 50)
m_data.list_blits["menu"].append(text_ip)
auto = Auto(width= 179, height= 79, x= 794, y= 587)
rotate = Button(fun= 'ship',  width = 222, height = 68, x= 1000, y= 600, name = "", progression= "pre-game", text= "")
play = Button(x = 900, y = 720, name = "", fun= 'play', width = 200, height = 65, text = "")
revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "win", fun= "win_lose")
out = Button(height = 80, width = 518, x = 0, y = 712, progression = "win", text = "", fun = "check")
m_data.list_blits["pre-game"].extend([rotate,play])
# revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "lose", fun= "win_lose")
# out = Button(height = 80, width = 518, x = 0, y = 712, progression = "lose", text = "", fun = "check")
music =Button(width = 76,height = 72,x = nickname.width + 50, y = 45, text = "", fun = "music", name =  "music")
client = Button(width= 281, height= 100, name= "button_start", text= "client", x= 42, y= 600, fun= "c_s:client")  
shop = Button(width= 281, height= 90, name= "button_start", text= "shop", x= 387+60, y= 725, fun= "shop",progression="NONE")
shop_ = Button(width= 321, height= 145, name= "", text= "", x= 0, y= 0, fun= "shop",progression='shop', size = 40)
achievements = Button(width= 500, height= 90, name= "button_start", text= "achievements", x= 387, y= 725, fun= "achievements",progression="menu")
achievements_ = Button(width= 281, height= 90, name= "button_start", text= "back to menu", x= 960, y= 15, fun= "achievements",progression='achievements', size = 40)
server = Button(width= 281, height= 100, name= "button_start", text= "server", x= 981, y= 600, fun= "c_s:server")
wait = Button(width= 1280, x = 0, y = 712, height= 59, text = "wait", progression= "game")
enemy_nickname = Button(y = 10, x = 1000, width= 200, height= 40, size = 40)
your_nickname = Button(y = 10, x = 20, width= 200, height= 40, size = 40)
coins = Button(y = 30, x = 950, width= 300, height= 90, size = 40, progression= "shop", text = "0", name = "")
# coin = Button(y = 50, x = 970, width= 50, height= 50, size = 0, progression= "shop", text = "", name = "duplone")
description = Button(y = 175, x = 950, width= 300, height= 533, size = 20, progression= "shop", text = "select item")
description_ = Button(y = 150, x = 950, width= 300, height= 533, size = 20, progression= "achievements", text = "select achievement")
buy = Button(y = 696, x = 957, width= 321, height= 145, size = 40, progression= "shop", text = "", name = "",fun='buy')
# m_data.list_blits["shop"].append(description)
homing_rocket = Button(y = 235, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/homing_rocket")
line_rocket= Button(y = 235, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/line_rocket")
fire_rocket = Button(y = 235, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/fire_rocket")
rocket_3x3 = Button(y = 235, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/rocket_3x3")

Anti_fire = Button(y = 514, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Anti_fire")
radar = Button(y = 514, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/radar")
Energetic = Button(y = 514, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Energetic")
Air_Defence = Button(y = 514, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Air_Defence")
list_weapons = [homing_rocket,rocket_3x3,line_rocket,fire_rocket,Energetic,radar,Air_Defence,Anti_fire]

m_data.list_blits['shop'] += list_weapons+[coins,buy,description]
if m_data.client_server == "server":
    server.COLOR =(40,2,255)
if m_data.client_server == "client":
    client.COLOR =(40,2,255)
your_turn = Button(width= 272, height= 66, x= 133, y= 712, text= "your step", progression= "", color=(0, 0, 255),size=50)
opponent_turn = Button(width= 350, height= 66, x= 800, y= 712, text= "enemy step", progression= "", color = (255, 0, 0),size=50)

m_data.list_blits["game"].append(your_nickname)
m_data.list_blits["game"].append(enemy_nickname)

m_data.list_blits["lose"].extend([revenge, out])
for achievement_code in m_data.achievements_data:
    m_data.list_achievements_view[achievement_code] = Button(fun=f"set_achievements/{achievement_code}",width=50,height=50,x=0,y=0,name=f"achievements/{achievement_code}",progression='NONE',text='')
# for achievement in m_data.list_achievements_view:
#     pass
 
# achievements
```

#### Online_game/modules/ships.py: створення механік кораблів, грального поля / development of mechanics for ships and the game field
```python
'''
    >>> Відображає кораблі на полі - клас Ship
    >>> Розміщує кораблі за координатами - параметри x, y
    >>> Перевіряє чи можна поставити корабель - метод check_enemy
    >>> Обертає кораблі - метод rotate_ship
    >>> Переміщує кораблі на нову позицію - метод place
    >>> Робить перевірку кожної клітинки - функція check
    >>> Очищує поле - функція clear_field
'''
# імпортуємо файли
import modules.images as m_images
import modules.data as m_data
import modules.clients_server as m_client
import modules.attack as m_attack
import modules.achievements as m_achievements
# імпортуємо модуль pygame
import pygame,random

# створює кораблі
class Ship(m_images.Image):
    '''
        >>> Створює кораблі
    '''
    # Ініціалізація корабля, параметри координат, розміри та орієнтація
    def __init__(self, x: int, y: int, name='1', row=0, cell=0, field_cor=[59, 115], rotate=0, add=True):
        # Розміри корабля залежать від його імені (перший символ - це кількість клітин корабля)
        self.width = int(name[0]) * 50
        self.height = 50
        self.explosion = False
        # Викликаємо конструктор батьківського класу (Image) для ініціалізації зображення
        super().__init__(self.width, self.height, x, y, name, "F", rotate)
        # Встановлюємо нові координати для корабля на полі
        self.x += (cell * 55.7)
        self.y += (row * 55.7)
        # Якщо корабель треба додати, додаємо його до загального списку кораблів
        if add:
            m_data.all_ships.append(self)
            for count in range(int(name[0])):
                if rotate % 180 == 0:
                    m_data.my_field[row][cell + count] = int(name[0])
                else:
                    m_data.my_field[row + count][cell] = int(name[0])
        # Ініціалізація деяких змінних
        self.select = False  # Перевірка, чи вибрано корабель
        self.row = row
        self.cell = cell
        self.jump_cor = [10,20,False,False]
        # Оновлюємо ігрове поле (записуємо розміри корабля)
        # Встановлюємо кордони корабля на полі
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.celled = None
    # Метод для перевірки, чи можна поставити корабель
    def check_enemy(self):
        '''
            >>> Перевіряє чи ми потрапили в ворожий корабель чи ні  
        '''
        yes_no = 0
        field = m_data.enemy_field
        cells = []
        for count in range(int(self.name[0])):
            # Перевіряємо горизонтальне або вертикальне розміщення корабля
            if self.rotate % 180 == 0 and m_data.enemy_field[self.row][self.cell + count] != int(self.name[0]):
                cells.append([self.row, self.cell + count])
                yes_no += 1
            elif self.rotate % 180 != 0 and m_data.enemy_field[self.row + count][self.cell] != int(self.name[0]):
                cells.append([self.row + count, self.cell])
                yes_no += 1

        # Якщо перевірка пройдена успішно, оновлюємо поле 
        if yes_no == int(self.name[0]):
            if self in m_data.all_ships:
                pass
            else:
                try:
                    for cell in cells:
                        list = m_data.list_explosions
                        list.reverse()
                        count = 0

                        for explosion in list:
                            if explosion[1] == cell[0] and explosion[2] == cell[1]:
                                del m_data.list_explosions[count]
                            count += 1
                except Exception as error:pass
                self.explosion = True

                m_data.all_ships.append(self)
                if str(self.name) == '4':
                    m_achievements.achievement('Titanic')
                m_attack.need_to_send.append(f"explosion:{self.row},{self.cell}")
                for celll in cells:
                    row = celll[0]
                    cell = celll[1]
                    fill_field(field)
                    check(field=field, row=row + 1, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell - 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row + 1, cell=cell - 1, values=[5, 7])
                    check(field=field, row=row + 1, cell=cell, values=[5, 7])
                    check(field=field, row=row, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell, values=[5, 7])
                    check(field=field, row=row, cell=cell - 1, values=[5, 7])

    # Метод активації корабля при натисканні
    def activate(self, event, multiplier_x=1, multiplier_y=1):
        '''
            >>> Виділяє корабель при натисканні на нього
        '''
        if self.rect.collidepoint(event.pos):
            self.select = True
            if random.randint(0,50) == 0 and ship.name[0] == '4':
                self.jump_cor = [10,20,False,False]
                self.jump_cor[2] = True
                m_data.cells[0]=True
                
                for row in m_data.my_field:
                    for cell in row:
                        if cell == 4:
                            cell = 0
            self.name = self.name[0] + "_select"
        else:
            self.place(event.pos, multiplier_x, multiplier_y)
            self.select = False
            self.name = self.name[0]
            #int(self.name[0]) => int(self.name[0])
        self.update_image()
    # Метод для обертання корабля
    def rotate_ship(self):
        '''
            >>> Обертає кораблі
        '''
        # Очищаємо місце для нового положення корабля на полі
        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell + count] = 0
            else:
                m_data.my_field[self.row + count][self.cell] = 0
        # Обираємо новий кут обертання
        self.rotate = self.rotate + 90
        fill_field(m_data.my_field)
        # Перевірка на можливість обертання корабля без зіткнень
        no_yes = True
        try:
            for count in range(int(self.name[0])):
                if self.rotate % 180 == 0:
                    if m_data.my_field[self.row][self.cell + count] != 0:
                        no_yes = False
                else:
                    if m_data.my_field[self.row + count][self.cell] != 0:
                        no_yes = False
        except:
            no_yes = False
        # Якщо обертання можливе, оновлюємо корабель
        if no_yes:
            self.update_image()
            if self.rotate % 180 == 0:
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            else:
                self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        else:
            self.rotate -= 90
        # Оновлюємо поле
        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell + count] = int(self.name[0])
            else:
                m_data.my_field[self.row + count][self.cell] = int(self.name[0])

    # Метод для зміщення корабля на нову позицію
    def place(self, pos, multiplier_x=1, multiplier_y=1):
        '''
            >>> Зміщує кораблі на нову позицію
        '''
        if self.select:
            for row in range(10):
                for cell in range(10):
                    yes_no = False
                    try:
                        yes_no_1 = True
                        for count in range(int(self.name[0])):
                            if self.rotate % 180 == 0:
                                if m_data.my_field[row][cell + count] != 0 and m_data.my_field[row][cell + count] != 5:
                                    yes_no_1 = False    
                            else:                                 
                                if m_data.my_field[row + count][cell] != 0 and m_data.my_field[row + count][cell] != 5:
                                    yes_no_1 = False   
                        if yes_no_1:
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell + count] = 0
                                else:
                                    m_data.my_field[self.row + count][self.cell] = 0
                            fill_field(m_data.my_field)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell + count] = int(self.name[0])
                                else:
                                    m_data.my_field[self.row + count][self.cell] = int(self.name[0])
                            yes_no_1 = True
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    if m_data.my_field[row][cell + count] != 0:
                                        yes_no_1 = False    
                                else:                                 
                                    if m_data.my_field[row + count][cell] != 0:
                                        yes_no_1 = False   
                            if yes_no_1:
                                yes_no = True
                            fill_field(m_data.my_field)
                    except:
                        pass
                    if yes_no:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7*multiplier_x,
                            self.field_cor[1] + row * 55.7*multiplier_y,
                            55.7, 55.7)
                        if rect.collidepoint(pos):
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell + count] = 0
                                else:
                                    m_data.my_field[self.row + count][self.cell] = 0
                            if self.celled != None:
                                m_data.cells[self.name[0]][self.celled][0] = False
                                self.celled = None
                            self.row = row
                            self.cell = cell
                            self.x = (cell * 55.7) + self.field_cor[0]
                            self.y = (row * 55.7) + self.field_cor[1]
                            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[row][cell + count] = int(self.name[0])
                                else:
                                    m_data.my_field[row + count][cell] = int(self.name[0])
                            self.select = False
                            fill_field(m_data.my_field)
                            return True
            count = 0
            for cell1 in m_data.cells[self.name[0]]:
                if not cell1[0]:
                    cell1[0] = True
                    self.x = cell1[1][0]
                    self.y = cell1[1][1]
                    for count1 in range(int(self.name[0])):
                        if self.rotate % 180 == 0:
                            m_data.my_field[self.row][self.cell + count1] = 0
                        else:
                            m_data.my_field[self.row + count1][self.cell] = 0
                    self.celled = count
                    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    break
                count += 1 
        fill_field(m_data.my_field)
# Функція перевірки на полі для кожної клітинки
def check(field, row, cell, values=[0, 5]):
    '''
        >>> Перевіряє клітинки на полі
    '''
    if row != -1 and -1 != cell:
        if row != 10 and 10 != cell:
            # Перевірка значення в клітинці
            if field[row][cell] == values[0]:
                field[row][cell] = values[1]
                if values[1] == 7:
                    image = m_images.Image(
                        progression="Noke",
                        name="miss",
                        x=725 + 55.7 * cell,
                        y=115 + 55.7 * row,
                        width=55.7,
                        height=55.7
                    )
                    image.update_image()
                    if image:
                        m_data.list_explosions.append((image,row,cell))
# Заповнюємо поле
def fill_field(field: list):
    '''
        >>> Заповнює поле
    '''
    clear_field(field)
    for row in range(10):
        for cell in range(10):
            cell_on_field = field[row][cell]
            if cell_on_field != 5 and cell_on_field != 0:
                check(field=field, row=row + 1, cell=cell + 1)
                check(field=field, row=row - 1, cell=cell - 1)
                check(field=field, row=row - 1, cell=cell + 1)
                check(field=field, row=row + 1, cell=cell - 1)
                
                check(field=field, row=row + 1, cell=cell)
                check(field=field, row=row, cell=cell + 1)
                check(field=field, row=row - 1, cell=cell)
                check(field=field, row=row, cell=cell - 1)
# Очищаємо поле від певних значень
def clear_field(field):
    '''
        >>> Очищує поле
    '''
    for row in range(10):
        for cell in range(10):
            if field[row][cell] == 5:
                field[row][cell] = 0
# Створення кораблів та їх розміщення
size_ship = "1"
for count in range(10):
    ship = Ship(x=59, y=115, name=size_ship)
    ship.select = True
    ship.place((684, 220))
    ship.select = False
    if count == 3:
        size_ship = "2"
    if count == 6:
        size_ship = "3"
    if count == 8:
        size_ship = "4"

fill_field(m_data.my_field)
# Додаємо корабель на нову позицію
ship.place((1, 1))

```

#### Online_game/modules/images.py: файл для роботи з зображеннями / file for working with images
```python
'''
    >>> Працює з зображеннями - клас Image
    >>> Оновлюємо зображення - метод update_image
    >>> Відображує картинки на екрані - метод blit
'''
# імпортуємо модуль pygame , os
import pygame, os
#імпртуємо модуль modules.data як m_data
import modules.data as m_data
import modules.main_window as main_window
# клас для роботи з зображенням
class Image():
    '''
        >>> Задаємо параметри до зображення
    '''
    # ініціалізуємо зображення
    def __init__(self, width: int, height: int, x: int, y: int, name = '', progression: str = "menu", rotate = 0, edit = True): 
        # переносимо параметри в змінні
        self.opasity = 255
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.name = name
        self.progression = progression
        self.rotate = rotate
        self.row = None
        self.cell = None
        # создаємо змінну self.image
        self.image = None
        # self.select_image = None
        # self.main_image = None
        # self.current_select = 0
        self.last_name = None
        # вказуємо чи можемо ми редагувати зображення
        self.edit_image = True
        # оновлюємо наше зображення
        self.update_image()
    # создаємо метод який оновлює наше зображення
    def update_image(self):
        '''
            >>> Завантажує зображення за вказаним шляхом
            >>> Змінює розмір зображення
        '''
        try:
            # завантажуємо зображення з вказаного нам шляху
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
            self.image = pygame.transform.rotate(self.image, self.rotate)
            
            if self.edit_image:
                # змінюємо розмір зображення 
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image = pygame.transform.rotate(self.image, self.rotate)
            # пепевіряємо чи є наше зораження в  списку в якому все відображаться на екрані
            if self in m_data.list_blits[self.progression]:
                pass
            else:
                # ми додаємо в цей список наше зображення
                m_data.list_blits[self.progression].append(self)
        except :
            # якщо сталась помилка при завантаженні зображення - ми пишемемо її
            pass
    # создаємо метод який відображє наше зображення
    # def blit(self, screen):

    #     # відображаємо наше зображення
    #     screen.blit(self.image, (self.x, self.y))
    # метод для відображення на екрані
    def blit(self,screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображуємо картинку на екрані
        '''
        # перевіряємо отриману ширину і висоту
        # s = pygame.time.get_ticks()
        # self.image = self.main_image
        # if self.current_select:
        #     self.image = self.
        try:
            if self.name != self.last_name or self.image.get_width() != int(width) or self.image.get_height() != int(height) :
                if self.rotate == 0 or self.image.get_width() != int(self.height*multiplier_x) or self.image.get_height() != int(self.width*multiplier_y) or self.name != self.last_name:
                    
                    # завантажуємо картинку
                    self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
                    # перевертаємо картинку
                    self.image = pygame.transform.rotate(self.image, self.rotate)
                    # перевіряємо оберт екрану
                    if self.rotate % 180 == 0:
                        # змінює масштаб
                        self.image = pygame.transform.scale(self.image, (width, height))
                        # задаємо розмір квадрату 
                        self.rect = pygame.Rect(x,y,width,height)
                        # малює прозорість зображення
                        # self.image.set_alpha(self.opasity)
                    else:
                        # задаємо інший масштаб картинки
                        self.image = pygame.transform.scale(self.image, (self.height*multiplier_x, self.width*multiplier_y))
                        # задаємо інший розмір квадрату
                        self.rect = pygame.Rect(x,y,height, width)
                        # малює прозорість зображення
                        # self.image.set_alpha(self.opasity)
                    self.last_name = self.name
            # відображення зображення на екрані
            screen.blit(self.image, (x, y))
        except:
            pass
        # e = pygame.time.get_ticks()
        # if e-s:
# задаємо параметри для фону 
background = Image(width = 1280, height = 851, x = 0, y = 0, name = "background")
# задаємо параметри для фону магазину
background_shop = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_shop",progression='shop')
background_achievements = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_shop",progression='achievements')
# задаємо параметри для грального поля
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")
# задаємо параметри для поля гри
play_field = Image(width = 1280, height = 835, x = 0, y = 0, name = "play_field", progression = "game")
# задаємо параметри для екрану програшу
lose = Image(width = 1280, height = 852, x = 0, y = 0, name = "lose", progression = "lose", edit = False)
# задаємо параметри для екрану перемоги
win = Image(width = 1280, height = 852, x = 0, y = 0, name = "win", progression = "win", edit = False)
# задаємо параметри для екрану досягнень
background_achievements = Image(width = 1280, height = 851, x = 0, y = 0, name = "achievements", progression = "achievements")
# задаємо параметри для протиповітряної охорони
air_defence = Image(55.7,55.7,-999,-99,'weapons/Air_Defence',progression='None')
```

#### Online_game/modules/audio.py: файл для роботи зі звуком / file for working with sound
```python
'''
    >>> Програє звуки і музику
    >>> Зупиняє звук і музику
'''
# імпортуємо модулі 
import pygame, os 
import modules.data as m_data
# ініцілізуємо звук
pygame.mixer.init()
# встановлємо гучність для відтворення музики
# pygame.mixer.music.set_volume(0.5)
# створення класу для роботи з аудіо
class Audio():
    '''
        >>> Додає фонову музику
        >>> Встановлює гучність для звуку
    '''
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
    def play(self, volume = 0.5):
        '''
            >>> Починає музику
            
        '''
        try:
            # зупиняємо музику
            self.stoped = False
            # відтворюємо музику
            self.audio.set_volume(volume)
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
# задаємо саундтрек для доріжки звуку
track = Audio('Soundtrack')
buying = Audio('buying',0)
# перевіряємо чи не дорівнює звук значенню False
if m_data.read_data["sound"] != "False":
    # граємо звукову доріжку
    track.play()
# додаємо звук для вибуху
explosion = Audio('blas',0)
```

#### Online_game/modules/data.py: файл у якому зберігається змінні / file for storing variables
```python
'''
    >>> Працює з словниками та списками
    >>> Зберігає данні та налаштування гри
'''
import os 
type = "/"
path = __file__.split("/")
if len(path) == 1:
    path = __file__.split("\\");type = "\\"
del path[-1]
del path[-1]
path.append("data")
# path.append("data.txt")
path = type.join(path)
try:
    os.mkdir(path+type+'achievements')
except:
    pass
read_data = {"nickname": "",
             "ip": "",
             "sound": True,
             "client_server": None,
             'wins':0,
             'loses':0
}
cost_data = {
    "homing_rocket":30,
    "line_rocket":30,
    "rocket_3x3":30,
    "fire_rocket":2,

    "Energetic":20,
    "radar":100,
    "Air_Defence":20,
    "Anti_fire":10,
}
weapon_data = {
    "rockets":{
        "homing_rocket":f"This rocket cost:{cost_data['homing_rocket']} and can hit one of the ships on the field, but it can be deflected.",
        "rocket_3x3":f"This rocket cost:{cost_data['rocket_3x3']} and can target any location within a 3x3 square of cells.",
        "line_rocket":f"This rocket cost:{cost_data['line_rocket']} and can move along a horizontal row of cells until it collides with a ship or the edge of the map.",
        "fire_rocket":f"This rocket cost:{cost_data['fire_rocket']} and can strike a single cell, leaving behind fire that will spread after the opponent's turn, destroying the ship."
    },
    "buff":{
        "radar":f"This buff cost:{cost_data['radar']} and grants the ability to see all enemy ships within a 5x5 cell radius.",
        "Air_Defence":f"This buff cost:{cost_data['Air_Defence']} and spreads in a 5x5 cell radius and can deflect a homing missile, but it only activates once.",
        "Energetic":f"This buff cost:{cost_data['Energetic']} and allows the player to perform two actions during their current turn (this item is not counted as an action).",
        "Anti_fire":f"This buff cost:{cost_data['Anti_fire']} and enables the player to extinguish a ship after it has been hit by a fire missile."
    }
}

select_weapon = None
attack = None
time_for_radar = 0
rect_for_radar = None
coins = 0
list_achievements = []
list_animations = []
list_for_radar = []
buffs = []

list_rockets = []
my_buffs = []
# achievements_data = [
#     {
#         'name':'',
#         'description':'',
#         'has':False,
#         'tier':0
#     }
# ]
list_achievements_view = {}
achievements_data = {
    "Total Domination":{
        'description':'win without a single hits',
        'has':False,
        'tier':1
    },
    "It’s a Hit!":{
        'description':'Hit a ship for the first time',
        'has':False,
        'tier':1
    },
    "Missed Shot":{
        'description':'First missed shot',
        'has':False,
        'tier':1
    },
    "Pants on Fire":{
        'description':'First defeat',
        'has':False,
        'tier':1
    },

    "Need More Gold!":{
        'description':'Accumulate 1000 tier',
        'has':False,
        'tier':1
    },
    "Like a Clap of Hands":{
        'description':'First victory',
        'has':False,
        'tier':1
    },
    "New Opportunities":{
        'description':'Enter the shop for the first time',
        'has':False,
        'tier':1
    },
    "Glory to Air Defense":{
        'description':'Destroy an "homing rocket" using Air defense',
        'has':False,
        'tier':1
    },
    "Hooked":{
        'description':'Buy your first weapon in the shop',
        'has':False,
        'tier':1
    },
    "Smells Like Victory":{
        'description':'Get a streak of three wins',
        'has':False,
        'tier':1
    },
    "Closed Skies":{
        'description':'Shoot down the first missile using air defense',
        'has':False,
        'tier':1
    },
    "Titanic":{
        'description':'Sink the first four-deck ship',
        'has':False,
        'tier':1
    },
    "used radar":{
        'description':'use an radar',
        'has':False,
        'tier':1
    },
    "Into the Sunset...":{
        'description':'Unlock all achievements',
        'has':False,
        'tier':1
    },
    "Losing Streak":{
        'description':'Lose three times in a row',
        'has':False,
        'tier':1
    },
    "Big Spender":{
        'description':'Spend 190 coins',
        'has':False,
        'tier':1
    },
    "Shopaholic":{
        'description':'Buy everything in the shop',
        'has':False,
        'tier':1
    },
    "the bug":{
        'description':'Secret',
        'has':False,
        'tier':1
    },
    "True Cossack":{
        'description':'Get 50 victories',
        'has':False,
        'tier':1
    }
}

def reading_data(dict,filename):
    try:
        with open(path+type+filename, "r") as file:
            data = file.read().split("\n")
            # if not "." in data[1] or data[1] == "" or data[0] == "":
            #     0 / 0
            count = 0
            for name in dict:
                if data[count] != '':
                    dict[name] = data[count]
                count+=1
    except Exception as error:
        text = ''
        count = 0
        for name in dict:
            if count:
                text+='\n'
            count +=1
        with open(path+type+filename, "w") as file:
            file.write(text)
    return dict 
read_data = reading_data(read_data,'data.txt')
for achievement in achievements_data:
    # name = achievement['name']
    name = achievement
    try:
        with open(path+type+'achievements'+type+name+'.txt', "r") as file:
            achievements_data[achievement]['has'] = file.read()
    except:
        with open(path+type+'achievements'+type+name+'.txt', "w") as file:
            file.write('False')


# створення словника у якому містяться всі картинки для кожної стадії гри
list_blits = {
    "menu": [],
    "pre-game": [],
    "game": [],
    "lose": [],
    "win": [],
    "shop": [],
    "achievements":[]
}
# http://127.0.0.1/
# Створення змінної, у якій ми будемо задавати потрібний єтап ігри
progression = "menu"
# Створення змінної, у якій буде записуватись ip ворога
ip = None
# Створення списку, у якому будуть зберігатися усі данні ворога
enemy_data = []
# Створення списку, у якому будуть зберігатися данні про всі наші кораблі
all_ships = []
# Створення списку, у якому будуть зберігатися данні про всі кораблі ворога
enemy_ships = []
# Створення списку, у якому знаходяться всі данні про клітинки у яких відбувся вибух
list_explosions = []
end = False
connected = False
enemy_nickname = ""
# Створення списку, у якому зберігаеться усе поле гравця
my_field = []
# Створення списку, у якому зберігаеться усе поле ворога
enemy_field = []
for count in range(10):
    enemy_field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    my_field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# Створеня змінної, у якій ми говоримо треба чи ні повернути корабель
turn = False
client_server = read_data["client_server"]
revenge = False
# Створеня словника, у якому міститься стандартне розташування всіх кораблів
cells = {
    "1":[
        [False, [728, 450]],
        [False, [840, 450]],
        [False, [950, 450]],
        [False, [1060, 450]]
    ],
    "2":[
        [False, [680, 340]],
        [False, [840, 340]],
        [False, [1010, 340]]
    ],
    "3":[
        [False, [730, 228]],
        [False, [950, 228]]
    ],
    "4":[
        [False, [805, 120]]
    ]
}


```

#### Online_game/modules/clients_server.py: файл який відповідає за роботу клієнту та серверу для гри по мережі / file responsible for the client and server functionality in a networked game
```python
'''
    >>> Працює з підключенням клієнта та сервера - змінна client_server
'''
# імпортуємо необхідні модулі
import modules.data as m_data 
import modules.ships as m_ships
import modules.images as m_images
import modules.buttons as m_buttons
import modules.transform as m_transform
import modules.achievements as m_achievements
import modules.audio as m_audio
import socket,random,os
import modules.animations as m_animations
# створюємо функцію для відправкм даних на сервер
def send(data:bytes):
    '''
        >>> Відправляє закодовані данні
    '''
    # відправляємо дані серверу
    try:
        # відпровляємо закодовані данні
        client.sendall([';'.encode()][0]+data+[';'.encode()][0])
    except:
        # відпровляємо закодовані данні
        client.sendall(f";{data};".encode())
# отримує ім'я хоста 
hostname = socket.gethostname()
# Повертає IP адрессу по імені хосту 
ip = socket.gethostbyname(hostname)

# створюємо сокет клієнту
client_server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
# функція для активації
count = 0
def activate():
        '''
            >>> Під'єднуємо клієнта і сервера
        '''
    # робимо змінну глобальною
        global client,count
    # try:
        # перевіряємо чи не відбувається хід супротивника
        if not m_data.revenge:
            # виводимо ім'я на поле
            ships = f"field_nickname:{m_buttons.nickname.TEXT}:"
            # перевіряємо всі кораблі
            for ship in m_data.all_ships:
                # додаємо функції для кораблів
                ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
            # перевіряємо чи клієнт на сервері
            if m_data.client_server == "server":
                # зв'язує клієнта з ip і портом
                client_server.bind(('0.0.0.0', 8800))
                # Функція listen активує очікування підключення користувача
                client_server.listen()
                m_data.turn = random.randint(0,1)
                if not m_data.turn:
                    ships+=';pass:'
                # Підтверджуємо з'єднання від клієнту
                client = client_server.accept()[0]
                # перевіряємо з'єднання
                m_data.connected = True
            # перевіряємо чи клієнт знаходиться в клієнті
            if m_data.client_server == "client":
                # підключаємо кліента до сервера
                client = client_server
                # під'єднуємо клієнта по ip і порту
                client.connect((m_data.ip, 8800))
                
            # надаємо підключенню значення True
            m_data.connected = True 
            # надаємо ходу супротивника значення True
            m_data.revenge = True
            # визиваємо функцію для відправки даних на сервер
            send(ships.encode())
            # перевіряємо чи не закінчена гра
            client_data = ''
            while not m_data.end:
                # Отримання данних кліенту та декодування їх
                client_data = client.recv(1024).decode()
                # розділяємо рядки сиволом ";"

                raw_data = client_data.split(";")
                # створюємо змінну текст зі значенням str
                text1 = ''
                list_to_del = []
                # перевіряємо ряди 
                for counter in range(len(raw_data)):
                    # перевіряємо клієнт дату
                    if raw_data[counter]:
                        # створюємо змінну текст зі значенням str
                        text1 = ''
                        # Перетворення данних на список розділяючи символом :
                        data = raw_data[counter].split(":")
                        # перевіряємо наявність ім'я на полі
                        if "field_nickname" in data[0]:
                            list_to_del.append(counter)
                            # текст нікнейму такий самий як твій нікнейм
                            m_buttons.your_nickname.TEXT = m_buttons.nickname.TEXT
                            # текст нікнейму супротивника дорівнює значенню в даті
                            m_buttons.enemy_nickname.TEXT = data[1]
                            
                            # друге значення зі списку буде розділен за пробілами
                            data = data[2].split(" ")
                            # Для кожного корабля у списку данних
                            for ship in data:
                                # Розділення кожного корабля по комі
                                splited_data = ship.split(",")
                                # Якщо розділенні данні кораблів не пусті
                                if splited_data != [""]:
                                    try:
                                        # створюеться екземпляр класу корабля з переданими параметрами
                                        ship = m_ships.Ship(x = 724,y = 115,
                                                    field_cor = (724,115),
                                                    name  = splited_data[0],
                                                    row = int(splited_data[1]),
                                                    cell = int(splited_data[2]),
                                                    rotate = int(splited_data[3]),
                                                    add = False)
                                        
                                        # Для кожного корабля первірка
                                        for count in range(int(ship.name[0])):
                                            # Якщо корабль було повернуто
                                            if ship.rotate % 180 == 0:
                                                # Додаємо його частини в поле противника по рядку
                                                m_data.enemy_field[ship.row][ship.cell+count] = int(ship.name[0])
                                            else:
                                                # Додаємо його частини в поле противника по стовпцю
                                                m_data.enemy_field[ship.row+count][ship.cell] = int(ship.name[0])
                                        
                                        # Додаємо корабель до списку кораблів противника
                                        m_data.enemy_ships.append(ship)
                                    except:
                                        pass
                        # Перевіряємо чи є "buff" в даті
                        elif "buff" in data[0]:
                            # додаємо "buff" в дату
                            m_data.buffs.append(data[1].split(','))
                            list_to_del.append(counter)
                        # Перевіряємо чи є "remove_buff" в даті
                        elif "remove_buff" in data[0]:
                            # видаляємо "buff" з дати
                            m_data.buffs.remove(data[1].split(','))
                            list_to_del+=[counter]
                        # Перевіряємо чи є "Anti_fire" в даті
                        elif 'Anti_fire' in data[0]:
                            list_to_del.append(counter)
                            # для повторів рядів
                            for row in range(10):
                                # якщо 8 в ряду поля супротивника
                                if 8 in m_data.enemy_field[row]:
                                    # для повторів клітинок 
                                    for cell in range(10):
                                        # перевіряємо кількість рядів і клітинок
                                        if m_data.enemy_field[row][cell] == 8:
                                            # змінюємо кількість рядів і клітинок
                                            m_data.enemy_field[row][cell] = 6
                            # вибух у списку вибуху                  
                            for explosion in m_data.list_explosions:
                                # перевіряє чи вибух перетворюється на вогонь
                                if explosion[0].name == 'fire' and explosion[0].x > 724:
                                    # записує 'explosion' в вибух
                                    explosion[0].name = 'explosion'
                                    # відновлює картинку вибуху
                                    explosion[0].update_image()
                        # записуємо атаку в дату
                        elif "attack" in data[0]:
                            # додає до пробіл до списку атак 
                            list_attacks = data[1].split(" ")
                            # для атак в списку атак
                            for attack in list_attacks:
                                try:
                                    # додаємо "," до атаки
                                    pos = attack.split(",")
                                    
                                    
                                    # записуємо функції до змінних
                                    volume = 0.5
                                    try:
                                        pos[3]
                                        if pos[3] == '1':
                                            volume = float(pos[3])
                                        else:
                                            for c in range(1000):
                                                print('YYYYYYYYYYYYYYYYYYYEEEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSSSSSS')
                                    except Exception as error:
                                        
                                        pass
                                    pos = [int(pos[0]), int(pos[1]),pos[2]]

                                    # Створюємо обект класа картинки, для відображення результату атаки, та передаємо параметри 
                                    clas = m_animations.Animation
                                    # Перевірка, чи атака була промахом
                                    if pos[2] == "miss":
                                        # Передаємо хід гравцю
                                        m_data.turn = True
                                        # Позначаємо промах на полі
                                        m_data.my_field[pos[0]][pos[1]] = 7
                                        clas = m_images.Image
                                        pass
                                    # перевіряємо чи корабель горить
                                    elif pos[2] == "fire":
                                        # Позначаємо промах на полі
                                        m_data.my_field[pos[0]][pos[1]] = 8
                                    else:
                                        # Позначаємо влучання на полі
                                        m_data.my_field[pos[0]][pos[1]] = 6
                                    image = clas(
                                        progression = "Noke",
                                        name = pos[2],
                                        x = 59+55.7*pos[1],
                                        y = 115+55.7*pos[0],
                                        width= 55.7,
                                        height=55.7,
                                    )
                                    m_audio.explosion.play(volume)
                                    # додаємо картинку до списку вибуху
                                    m_data.list_explosions.append([image,pos[0],pos[1]])
                                except Exception as error:
                                    pass
                            list_to_del.append(counter)
                        # записуємо "pass" в дату
                        elif "pass" in data[0]:
                            # передаємо хід 
                            m_data.turn = True
                            list_to_del.append(counter)
                        # перевіряємо наявність "fire" в даті
                        if 'fire' in data[0]:
                            try:
                                # додає пробіл до ряду в даті
                                raw_data1 = data[1].split(' ')
                                # для клітинок в ряду
                                for cells in raw_data1:
                                    # чи є в клітинках щось
                                    if cells:
                                        # додаємо "," до клітинки
                                        cells1 = cells.split(',')
                                        # позначаємо промах для ворожнечого поля
                                        m_data.enemy_field[int(cells1[0])][int(cells1[1])] = 8
                                        # Створюємо обект класа картинки, для відображення вогню, та передаємо параметри 
                                        image = m_images.Image(
                                                progression = "game",
                                                name = 'fire',
                                                x = 725+55.7*int(cells1[1]),
                                                y = 115+55.7*int(cells1[0]),
                                                width= 55.7,
                                                height=55.7
                                        )
                                        # додаємо картинку до списку вибуху
                                        m_data.list_explosions.append([image,int(cells1[0]),int(cells1[1])])
                                        # дя кораблів в ворожих кораблях
                                        for ship in m_data.enemy_ships:
                                            # перевіряємо кораблі ворога
                                            ship.check_enemy()
                            except Exception as error:
                                # безпечно відкриває output/txt
                                with open(os.path.abspath(__file__+'/../../data/output.txt')) as file:
                                    # до тексту додаємо файл для читання
                                    text1 += file.read()
                                # безпечно відкриває output/txt 
                                with open(os.path.abspath(__file__+'/../../data/output.txt'),'w') as file:
                                    # відкриває файл для написання
                                    file.write(text1+'\n'+str(error))
                            list_to_del.append(counter)
                                                
                        # Перевірка, чи відбувся вибух
                        if "explosion" in data[0]:
                            # в дату додає знак ","
                            pos = data[1].split(",")
                            # перевіряє довжин
                            if len(pos[0]) > 1:
                                # залишає значення позиції таким самим
                                pos[0] = pos[0][0]
                            # перевіряє довжину
                            if len(pos[1]) > 1:
                                # змінює значення позиції
                                pos[1] = pos[1][0]
                            # записуємо функції до змінних
                            pos = [int(pos[0]), int(pos[1])]
                            # except:
                            # Перебираемо всі кораблі
                            for ship in m_data.all_ships:
                                # Якщо це корабль противника пропускаємо
                                if ship in m_data.enemy_ships:
                                    pass
                                # якщо координати вибуху збігаються з позицією корабля
                                elif ship.row == pos[0] and ship.cell == pos[1]:
                                    # то відбуваеться вибух
                                    ship.explosion = True
                                    
                                    
                            list_to_del.append(counter)
                            # дата видаляється
                            
                        # якщо відбуваеться програш
                        elif "lose" in data[0]:
                            # змінюємо колір трансформації
                            m_transform.color = (255,25,25)
                            #задаємо кількість типів трансформації
                            m_transform.type_transform = 0
                            # стан гри змінюеться на програш
                            m_data.progression = "lose"
                            # додається нове досягнення
                            m_achievements.achievement('Pants on Fire')
                            list_to_del.append(counter)
                            # дата видаляється
                try:
                    for counts in list_to_del:
                        del raw_data[-(counts+1)]
                    client_data = ";".join(raw_data)
                    pass
                except Exception as error:
                    pass
```

#### Online_game/modules/transform.py: файл у якому реалізовані анімації переходів / file for transition animations
```python
'''
    >>> Відповідає за перехід між екранами - фунція transform
    >>> Відповідає за анімацію переходу між екранами - функція transform_rect
'''
# імпортуємо рандомайзер
import random
# робимо імпорт pygame
import pygame
# з файлу button імпортуємо кнопку
import modules.buttons as m_buttons
# з дати імпортуємо дату
import modules.data as m_data
# з файлу звука імортуємо аудіо
import modules.audio as m_audio 
# з файлу доягнень імпортуємо досягнення
import modules.achievements as m_achievements
# змінна трансформації зі значенням нічого
type_transform = None

# задаємо ширину
width = 1280
# задаємо висоту
height = 832
# задаємо колір переходу 
color = (0,0,0)
# задаємо розмір переходу
size = 0
# створюємо змінну переходу
progression = None
# задаємо число типів переходів
count_types = 0
# задаємо кінець
end = 0
# функція для трансформації екрану
def transform(screen,multiplier_x,multiplier_y):
    '''
        >>> Трансформує екран
    '''
    # робимо змінні глобальними
    global type_transform,color,progression
    # умова якщо екран нікуди не переходить
    if type_transform == None:
        # задаємо перехід
        progression = m_data.progression
        # задаємо випадковий колір
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # перевертаємо дісплей
        pygame.display.flip()
    # інакше змінна трансформації набуває значення 0
    elif type_transform == 0:
        # трансформуємо в прямокутну форму
        transform_rect(screen.screen,multiplier_x,multiplier_y)
# функція для трансформування екрану в прямокутну форму   
def transform_rect(screen,multiplier_x,multiplier_y):
    '''
        >>> Змінює розмір прямокутника під час анімації переходу
    '''
    # робить змінні глобальними
    global size,type_transform,color
    # додає до розміру 25
    size += 25
    # зміна розміру прямокутника при переході
    rect = pygame.Rect((640 - size/2*1.53846153846)*multiplier_x, (416 - size/2)*multiplier_y, size*multiplier_x*1.53846153846,size*multiplier_y)
    # надаємо параметри для ходу
    m_buttons.stroke(screen,rect,
                     color,10)
    # оновлюємо перехід екрану
    pygame.display.update(rect)
    # перевіряємо розмір
    if size > 832:
        # змінюємо значення трансформації на нічого
        type_transform = None
        # змінюємо розмір на 0
        size = 0

```

#### Online_game/modules/achievements.py: файл для реалізауції механіки досягнень / file for achievement mechanics
```python
'''
    >>> Додаємо список досягнень
    >>> Перевіряєм їх наявність в гравця
    >>> Виводимо доягнення на екран 
'''
# імпортуємо необхідні модулі
import pygame, os, time, threading
# з файлу дата імпортуємо дату
import modules.data as m_data
# з файлу аудіо імпортуємо аудіо
import modules.audio as m_audio
# задаємо ширину
width = 400
# задаємо висоту
height = 120
# задаємо y
y = 0
# задаємо x
x = 1280

# класс з досягненнями
class achievement():
    '''
        >>> Перевіряє наявність досягнень
        >>> Додає нові досягнення
    '''
    # метод класу
    def __init__(self,name):
        # робимо змінні глобальними
        global x,y,width,height
        # перевіряємо чи не має досягнення
        if m_data.achievements_data[name]['has'] == "False":
            # задаємо наявність досягнення
            if name != "Into the Sunset...":
                yes_no = True
                for achievement_code in m_data.achievements_data:
                    if (m_data.achievements_data[achievement_code]['has'] == 'False' or m_data.achievements_data[achievement_code]['has'] == False) and achievement_code!= "Into the Sunset...":
                        yes_no = False
                if yes_no:
                    achievement("Into the Sunset...")
            m_data.achievements_data[name]['has'] = "True"
            # задаємо шрифт
            self.FONT = pygame.font.SysFont("algerian", 40)
            # задаємо розмір квадрату
            self.rect = pygame.Rect(x,y,width,height)
            # додаємо срисок досягнень
            m_data.list_achievements.append(self)
            # розділяємо текст на частини
            self.text = name.split(' ')
            # об'єднує розмір шрифта тексту
            size = self.FONT.size(" ".join(self.text))
            # перевіряємо розмір
            if size[0] < 300:
                # об'єднуємо текст
                self.text = [" ".join(self.text)]
            # віднімаємо 2 від довжини тексту
            elif len(self.text)-2:
                # створюємо список для тексту
                list_text = []
                # створюємо змінну з текстом
                text = ''
                # цикл для тексту
                for text_for in self.text:
                    # розмір шрифту
                    size = self.FONT.size(text+text_for)
                    # перевіряємо розмір
                    if size[0] < 280:
                        # додаємо текст до змінної з текстом для
                        text += text_for+' '
                    # перевіряємо розмір
                    if size[0] > 280:
                        # додаємо текст до списку
                        list_text.append(text)
                        # текст дорівнює змінній текст для
                        text = text_for
                    # від тексту віднімаємо одне значення
                    elif self.text[-1] == text_for:
                        # додаємо текст до списку
                        list_text.append(text)
                # перевіряємо чи немає текту в списку
                if not text_for in list_text[-1]:
                    # додаємо розміри текту і тексту для
                    size = self.FONT.size(text+text_for)
                    # перевіряємо розмір
                    if size[0] < 280:
                        # додаємо текст до змінної з текстом для
                        text += text_for+' '
                    # перевіряємо розмір
                    if size[0] > 280:
                        # додаємо текст до списку
                        list_text.append(text)
                        # текст дорівнює змінній текст для
                        text = text_for
                    # від тексту віднімаємо одне значення
                    elif self.text[-1] == text_for:
                        # додаємо текст до списку
                        list_text.append(text)
                # текст дорівнює списку з текстом
                self.text = list_text
            # звук при отриманні досягнення   
            m_audio.achievement.play()
            # задаємо час
            self.time = 5
            # задаємо активацію таймеру
            self.activate_timer = False
            # задаємо деактивацію таймеру
            self.deactivate_timer = False
            # задаємо ім'я
            self.name = name
            # безпечно відкриваємо файл
            with open(m_data.path+m_data.type+'achievements'+m_data.type+name+'.txt', "w") as file:
                # записуємо значення True в файл
                file.write('True')
    # метод для руху
    def move(self):
        '''
            >>> Відповідає за анімацію вилізання досягнення
        '''
        # робимо змінні глобальними
        global x,y,width,height
        # перевіряємо чи не активований таймер
        if not self.activate_timer:
            # перевіряємо x квадрату і не деактивований таймер
            if self.rect.x < 1280-395 and not self.deactivate_timer:
                # активовуємо таймер
                self.activate_timer = True
                # створення потоків
                threading.Thread(target=self.timer,daemon=1).start()
            # перевіряємо x квадрату і деактивовацію таймеру
            elif self.rect.x > 1280 and self.deactivate_timer:
                # видаляємо зі списку
                m_data.list_achievements.remove(self)
            else:
                # перевіряємо чи не деактивований таймер
                if not self.deactivate_timer:
                    # від x квадрату віднімаємо 15
                    self.rect.x -= 15
                else:
                    # від x квадрату додаємо 15
                    self.rect.x += 15
    # промальовуємо основу поверхності
    def blit(self,screen:pygame.Surface,multiplier_x,multiplier_y):
        '''
            >>> Трансформує масштаб картинки
        '''
        # завантажуємо картинку
        self.img = pygame.image.load(os.path.abspath(f"{__file__}/../../images/achievements/{self.name}.png"))
        # трансформуємо масштаб
        self.img = pygame.transform.scale(self.img, (100, 100))
        # кольори пікселів, які збігаються стають прозорими
        self.img.set_colorkey((0, 0, 0))
        # змінюємо розмір квадрату
        rect = pygame.Rect(
            self.rect.x*multiplier_x,
            self.rect.y*multiplier_y,
            self.rect.width*multiplier_x,
            self.rect.height*multiplier_y
            )
        # промальовка квадрату
        square = pygame.Surface((rect.width,rect.height))
        # заповнення квадрату кольором
        square.fill((69, 69, 69))
        # заливаємо квадрат кольором зображення
        square.set_alpha(200)
        # відображення квадрату на екрані
        screen.blit(square,rect)
        # відображення картинки на екрані
        screen.blit(self.img, ((self.rect.x+10)*multiplier_x,(self.rect.y)*multiplier_y))
        # задаємо кількість
        count = 0
        # цикл для текту
        for text in self.text:
            # перевіряємо чи x більший за y
            if multiplier_x > multiplier_y:
                # задаємо шрифт для тексту y
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
            else:
                # задаємо шрифт для тексту x
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
            # задаємо шрифт для висоти
            height = self.FONT.size(text)[1]
            # задаємо y для тексту
            y = (self.rect.y+10+height*count) * multiplier_y
            # задаємо x для тексту
            x = (self.rect.x + 120)*multiplier_x
            # відображення тексту на екрані
            screen.blit(self.FONT.render(text,True,(0,0,0)), (x, y))
            # до кількості додаємо 1
            count += 1
    # метод для таймеру
    def timer(self):
        '''
            >>> Відповідає за запуск і зупинку часу
        '''
        # працює поки час не дорувнює 0
        while self.time != 0:
            # від часу віднімається 1
            self.time -= 1
            # пауза 1 секунда
            time.sleep(1)
        # задаємо значення True для деактивації таймеру
        self.deactivate_timer = True
        # задаємо значення False для активації таймеру
        self.activate_timer = False

```