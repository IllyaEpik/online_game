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
        # print(self.width)
        self.height = 50
        self.explosion = False
        # print(self.height)
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
        # print(self.y)
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
    # def jump(self, x = 5,y = 100):
    #     self.x 
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
                        print(cell,0)
                        print(m_data.list_explosions)
                        list = m_data.list_explosions
                        list.reverse()
                        print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhssssssssssssssssssssssssssssssssssssssssssssssssssssss')
                        print(list)
                        count = 0

                        for explosion in list:
                            print(explosion,count,'troll')
                            if explosion[1] == cell[0] and explosion[2] == cell[1]:
                                del m_data.list_explosions[count]
                            count += 1
                except Exception as error:
                    for c in range(222):
                        print(error)
                self.explosion = True

                m_data.all_ships.append(self)
                if str(self.name) == '4':
                    m_achievements.achievement('Titanic')
                m_attack.need_to_send.append(f"explosion:{self.row},{self.cell}")
                # m_client.send()
                

                # print(cells)
                for celll in cells:
                    row = celll[0]
                    cell = celll[1]
                    # print(row, cell)
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
            # print('eqw')
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
        # print(2132132312123123231213231)
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
            # print(self.field.collidepoint(pos))
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
                        # print("капибара")
                    if yes_no:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7*multiplier_x,
                            self.field_cor[1] + row * 55.7*multiplier_y,
                            55.7, 55.7)
                        if rect.collidepoint(pos):
                            # print(m_data.cells,self.celled)
                            # print()
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
                            # print(m_data.cells,self.celled)
                            return True
            count = 0
            for cell1 in m_data.cells[self.name[0]]:
                # print(cell1)
                if not cell1[0]:
                    cell1[0] = True
                    self.x = cell1[1][0]
                    self.y = cell1[1][1]
                    for count1 in range(int(self.name[0])):
                        if self.rotate % 180 == 0:
                            m_data.my_field[self.row][self.cell + count1] = 0
                        else:
                            m_data.my_field[self.row + count1][self.cell] = 0
                    # m_data.my_field[self.row][self.cell] = 0 
                    self.celled = count
                    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    # for row in m_data.my_field:
                    #     print(row)      
                    break
                count += 1 
        fill_field(m_data.my_field)
        for row in m_data.my_field:
            print(row)
        # print(m_data.cells)

        # for row in m_data.my_field:
        #     print(row)
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
                    # print(11)
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
