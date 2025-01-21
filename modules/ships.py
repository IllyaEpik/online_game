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
        # Якщо корабель треба додати
        if add:
            # додаємо його до загального списку кораблів
            m_data.all_ships.append(self)
            # цикл для кількості
            for count in range(int(name[0])):
                # перевіряємо поворот корабля
                if rotate % 180 == 0:
                    # до клітинок поля додаємо кількість і це дорівнює назві
                    m_data.my_field[row][cell + count] = int(name[0])
                else:
                    #  до ряду поля додаємо кількість і це дорівнює назві
                    m_data.my_field[row + count][cell] = int(name[0])
        # задаємо параметри
        self.select = False  
        self.row = row
        self.cell = cell
        self.jump_cor = [10,20,False,False]
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.celled = None
    # Метод для перевірки, чи можна поставити корабель
    def check_enemy(self):
        '''
            >>> Перевіряє чи ми потрапили в ворожий корабель чи ні  
        '''
        # задємо значення 0 в змінну да_ні
        yes_no = 0
        # вороже поле
        field = m_data.enemy_field
        # список клітинок
        cells = []
        # цикл для кількості
        for count in range(int(self.name[0])):
            # Перевіряємо горизонтальне або вертикальне розміщення корабля
            if self.rotate % 180 == 0 and m_data.enemy_field[self.row][self.cell + count] != int(self.name[0]):
                # до клітинки додаємо ряд і кількість клітинок
                cells.append([self.row, self.cell + count])
                # до змінної да_ні додаємо 1
                yes_no += 1
            # превіряємо поворот корабля на ворожому полі
            elif self.rotate % 180 != 0 and m_data.enemy_field[self.row + count][self.cell] != int(self.name[0]):
                # до клітинки додаємо ряд і кількість клітинок
                cells.append([self.row + count, self.cell])
                # до змінної да_ні додаємо 1
                yes_no += 1
        # Якщо перевірка пройдена успішно, оновлюємо поле 
        if yes_no == int(self.name[0]):
            # перевіряємо всі кораблі
            if self in m_data.all_ships:
                pass
            else:
                try:
                    # цикл для клітинок
                    for cell in cells:
                        # до списку записуємо список вибухів
                        list = m_data.list_explosions
                        # список для реваншу
                        list.reverse()
                        # задаємо кількість
                        count = 0
                        # цикл для вібуху в списку
                        for explosion in list:
                            # перевірка вибуху в клітинках
                            if explosion[1] == cell[0] and explosion[2] == cell[1]:
                                # видалямо кількість з списку вибухів
                                del m_data.list_explosions[count]
                            # до кількості додаємо 1
                            count += 1
                # виводимо помилку
                except Exception as error:pass
                # відбувається вибух
                self.explosion = True
                # додаємо параметри к усім кораблям
                m_data.all_ships.append(self)
                # перевіряємо корабель, який вибухнув
                if str(self.name) == '4':
                    # додаємо досягнення
                    m_achievements.achievement('Titanic')
                # додаємо вибух до змінної необхідного для відправки
                m_attack.need_to_send.append(f"explosion:{self.row},{self.cell}")
                # цикл для клітинок
                for celll in cells:
                    # створюємо змінні для перевірки розташування кораблів
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
        # превірка виділення
        if self.rect.collidepoint(event.pos):
            # обираємо корабель
            self.select = True
            # рандомно розставляємо кораблі
            if random.randint(0,50) == 0 and self.name[0] == '4':
                # перехід координат
                self.jump_cor = [10,20,False,False]
                # перехід координат
                self.jump_cor[2] = True
                # розташування в клітинці

                m_data.cells['3'][0][0]=True
                # цикл для рядів на полі
                for row in m_data.my_field:
                    # цикл для клітинок в ряду
                    for cell in row:
                        # перевіряємо клітинки
                        if cell == 4:
                            # змінюємо клітинку на 0
                            cell = 0
            # обираємо назву
            self.name = self.name[0] + "_select"
        else:
            # розташовуємо по координатам на полі
            self.place(event.pos, multiplier_x, multiplier_y)
            # прибираємо виділення
            self.select = False
            # параметр з назвою
            self.name = self.name[0]
            #int(self.name[0]) => int(self.name[0])
        # оновлюємо картинку
        self.update_image()
    # Метод для обертання корабля
    def rotate_ship(self):
        '''
            >>> Обертає кораблі
        '''
        # Очищаємо місце для нового положення корабля на полі
        if self.row:
            # цикл для кількості кораблів 
            for count in range(int(self.name[0])):
                # перевіряємо поворот корабля
                if self.rotate % 180 == 0:
                    # до клітинок поля додаємо кількість
                    m_data.my_field[self.row][self.cell + count] = 0
                else:
                    # до рядів поля додаємо кількість
                    m_data.my_field[self.row + count][self.cell] = 0
        # Обираємо новий кут обертання
        self.rotate = self.rotate + 90
        # заповнюємо поле
        fill_field(m_data.my_field)
        # Перевірка на можливість обертання корабля без зіткнень
        no_yes = True
        try:
            # перевірка ряду
            if self.row:
                # цикл для кількості кораблів 
                for count in range(int(self.name[0])):
                    # перевіряємо поворот
                    if self.rotate % 180 == 0:
                        # превіряємо ряди і клітинки поля
                        if m_data.my_field[self.row][self.cell + count] != 0:
                            # не можемо обертати корабель
                            no_yes = False
                    else:
                        # превіряємо ряди і клітинки поля
                        if m_data.my_field[self.row + count][self.cell] != 0:
                            # не можемо обертати корабель
                            no_yes = False
        except:
            # не можемо обертати корабель
            no_yes = False
        # Якщо обертання можливе
        if no_yes:
            # оновлюємо корабель
            self.update_image()
            # перевіряємо поворот
            if self.rotate % 180 == 0:
                # перехід
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            else:
                # перехід
                self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        else:
            # змінюємо поворот
            self.rotate -= 90
        # Оновлюємо поле
        if self.row:
            # цикл для кількості кораблів 
            for count in range(int(self.name[0])):
                # перевіряємо поворот
                if self.rotate % 180 == 0:
                    # заповнення рядів і клітинок поля
                    m_data.my_field[self.row][self.cell + count] = int(self.name[0])
                else:
                    # заповнення рядів і клітинок поля
                    m_data.my_field[self.row + count][self.cell] = int(self.name[0])

    # Метод для зміщення корабля на нову позицію
    def place(self, pos, multiplier_x=1, multiplier_y=1):
        '''
            >>> Зміщує кораблі на нову позицію
        '''
        # якщо обрано
        if self.select:
            # цикл для кораблів в рядах
            for row in range(10):
                # цикл для кораблів в клітинках
                for cell in range(10):
                    # не дозволяємо 
                    yes_no = False
                    try:
                        # дозволяємо
                        yes_no_1 = True
                        # цикл для кількості кораблів
                        for count in range(int(self.name[0])):
                            # перевіряємо поворот
                            if self.rotate % 180 == 0:
                                # перевірка заповнення поля
                                if m_data.my_field[row][cell + count] != 0 and m_data.my_field[row][cell + count] != 5:
                                    # не дозволяємо поставити корабель
                                    yes_no_1 = False    
                            else: 
                                # перевірка заповнення поля                          
                                if m_data.my_field[row + count][cell] != 0 and m_data.my_field[row + count][cell] != 5:
                                    # не дозволяємо поставити корабель
                                    yes_no_1 = False   
                        # перевіряємо поставлен корабель чи ні
                        if yes_no_1:
                            # перевіряє встановлений корабель
                            if self.row:
                                # цикл для кількості кораблів
                                for count in range(int(self.name[0])):
                                    # перевіряємо поворот
                                    if self.rotate % 180 == 0:
                                        # заповнення поля кораблями в рядах і клітинках
                                        m_data.my_field[self.row][self.cell + count] = 0
                                    else:
                                        # заповнення поля кораблями в рядах і клітинках
                                        m_data.my_field[self.row + count][self.cell] = 0
                                # заповнюємо поле
                                fill_field(m_data.my_field)
                                # цикл для кількості кораблів
                                for count in range(int(self.name[0])):
                                    # перевіряємо поворот
                                    if self.rotate % 180 == 0:
                                        # заповнення поля кораблями в рядах і клітинках
                                        m_data.my_field[self.row][self.cell + count] = int(self.name[0])
                                    else:
                                        # заповнення поля кораблями в рядах і клітинках
                                        m_data.my_field[self.row + count][self.cell] = int(self.name[0])
                                #
                            yes_no_1 = True
                            # цикл для кількості кораблів
                            for count in range(int(self.name[0])):
                                # перевіряємо поворот
                                if self.rotate % 180 == 0:
                                    # перевірка заповнення поля 
                                    if m_data.my_field[row][cell + count] != 0:
                                        # не дозволяємо поставити корабель
                                        yes_no_1 = False    
                                else:            
                                    # перевірка заповнення поля                     
                                    if m_data.my_field[row + count][cell] != 0:
                                        # не дозволяємо поставити корабель
                                        yes_no_1 = False   
                            # перевіряємо встановлення корабля
                            if yes_no_1:
                                # дозволяємо поставити корабель
                                yes_no = True
                            # заповнюєо поле
                            fill_field(m_data.my_field)
                    except:
                        pass
                    # перевіряємо перехід
                    if yes_no:
                        # анімація переходу
                        rect = pygame.Rect(
                            (self.field_cor[0] + cell * 55.7)*multiplier_x,
                            (self.field_cor[1] + row * 55.7)*multiplier_y,
                            55.7*multiplier_x, 55.7*multiplier_y)
                        # перевіряємо обводку
                        if rect.collidepoint(pos):
                            # перевіряємо кораблі на полі
                            if self.row:
                                # цикл для кількості кораблів
                                for count in range(int(self.name[0])):
                                    # перевіряємо поворот
                                    if self.rotate % 180 == 0:
                                        # заповнення поля
                                        m_data.my_field[self.row][self.cell + count] = 0
                                    else:
                                        # заповнення поля
                                        m_data.my_field[self.row + count][self.cell] = 0
                            # перевірка назви
                            if self.celled != None:
                                # назва клітинок
                                m_data.cells[self.name[0]][self.celled][0] = False
                                # задаємо назву None
                                self.celled = None
                            # додаємо параметр ряду
                            self.row = row
                            # додаємо параметр клітинки
                            self.cell = cell
                            # додаємо параметр x
                            self.x = (cell * 55.7) + self.field_cor[0]
                            # додаємо параметр y
                            self.y = (row * 55.7) + self.field_cor[1]
                            # анімація переходу
                            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                            # цикл для кількості кораблів
                            for count in range(int(self.name[0])):
                                # перевірка повороту
                                if self.rotate % 180 == 0:
                                    # заповнення клітинок і рядів поля
                                    m_data.my_field[row][cell + count] = int(self.name[0])
                                else:
                                    # заповнення клітинок і рядів поля
                                    m_data.my_field[row + count][cell] = int(self.name[0])
                            # прибираємо виділення
                            self.select = False
                            # заповнюєо поле
                            fill_field(m_data.my_field)
                            # повертаємо True
                            return True
            # змінюємо кількість на 0
            count = 0
            # цикл для перевірки заповнення клітинок
            for cell1 in m_data.cells[self.name[0]]:
                # превіряємо заповнення клітинок
                if not cell1[0] or self.celled and m_data.cells[self.name[0]][self.celled] == cell1:
                    # якщо назва None
                    if self.celled != None:
                        print(self.celled)
                        # клітинка не заповнена
                        m_data.cells[self.name[0]][self.celled][0] = False
                        # значення назви корабля None
                        self.celled = None
                    # клітинка заповнена
                    cell1[0] = True
                    # розташування клітинки по x
                    self.x = cell1[1][0]
                    # розташування клітинки по y
                    self.y = cell1[1][1]
                    # перевірка кораблів на полі
                    if self.row:
                        # цикл для кількості кораблів
                        for count1 in range(int(self.name[0])):
                            # перевірка повороту корабля
                            if self.rotate % 180 == 0:
                                # заповнення клітинок і рядів поля
                                m_data.my_field[self.row][self.cell + count1] = 0
                            else:
                                # заповнення клітинок і рядів поля
                                m_data.my_field[self.row + count1][self.cell] = 0
                    # параметр ряду
                    self.row = None
                    # параметр клітинки
                    self.cell = None
                    # параметр для назви
                    self.celled = count
                    # параметр переходу
                    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    # зупинка
                    break
                # до кількості додаємо 1
                count += 1 
        # заповнюєо поле
        fill_field(m_data.my_field)
        for row in m_data.my_field:
            print(row)
# Функція перевірки на полі для кожної клітинки
def check(field, row, cell, values=[0, 5]):
    '''
        >>> Перевіряє клітинки на полі
    '''
    # перевірка ряду і клітинки
    if row != -1 and -1 != cell:
        # перевірка ряду і клітинки
        if row != 10 and 10 != cell:
            # Перевірка значення в клітинці
            if field[row][cell] == values[0]:
                # заповнення рядів і клітинок значенням 1
                field[row][cell] = values[1]
                # перевіряємо значення
                if values[1] == 7:
                    # наслідуємо клас Image і додаємо параметри для картинки
                    image = m_images.Image(
                        progression="Noke",
                        name="miss",
                        x=725 + 55.7 * cell,
                        y=115 + 55.7 * row,
                        width=55.7,
                        height=55.7
                    )
                    # оновлюємо картинку
                    image.update_image()
                    # перевіряємо картинку
                    if image:
                        # до списку вибуху додаємо картинку, ряд і клітинку
                        m_data.list_explosions.append((image,row,cell))
# Заповнюємо поле
def fill_field(field: list):
    '''
        >>> Заповнює поле
    '''
    # очищуємо поле
    clear_field(field)
    # цикл для кораблів на полі 
    for row in range(10):
        # цикл для кораблів на полі
        for cell in range(10):
            # змінна для клітинок на полі
            cell_on_field = field[row][cell]
            # перевірка значення клітинки
            if cell_on_field != 5 and cell_on_field != 0:
                # перевірка заповнення поля, ряда і клітинки
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
    # цикл для кораблів в рядах
    for row in range(10):
        # цикл для кораблів в клітинках
        for cell in range(10):
            # перевіряємо заповнення поля
            if field[row][cell] == 5:
                # змінюємо значення на 0
                field[row][cell] = 0
# змінюємо розмір корабля на 1
size_ship = "1"
# цикл для кількості кораблів і їх розміщення
for count in range(10):
    # наслідуємо клас Ship і задаємо параметри для корабля
    ship = Ship(x=59, y=115, name=size_ship)
    # обираємо корабель
    ship.select = True
    # розташовуємо корабель за координатами
    ship.place((684, 220))
    # прибираємо виділення корабля
    ship.select = False
    # перевіряємо кількість кораблів
    if count == 3:
        # розмір дво-палубний
        size_ship = "2"
    # перевіряємо кількість кораблів
    if count == 6:
        # розмір три-палубний
        size_ship = "3"
    # перевіряємо кількість кораблів
    if count == 8:
        # розмір чотири-палубний
        size_ship = "4"
# заповнюємо поле
fill_field(m_data.my_field)
# Додаємо корабель на нову позицію
ship.place((1, 1))
# Створення списку, у якому зберігаеться усе поле гравця
m_data.my_field = []
for count in range(10):
    m_data.my_field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])