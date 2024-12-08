# імпортуємо файли
import modules.images as m_images
import modules.data as m_data
import modules.client as m_client

# імпортуємо модуль pygame
import pygame 

# создаемо з Кораблями
class Ship(m_images.Image):
    # Ініціалізація корабля, параметри координат, розміри та орієнтація
    def __init__(self, x: int, y: int, name='1', row=0, cell=0, field_cor=[59, 115], rotate=0, add=True):
        # Розміри корабля залежать від його імені (перший символ - це кількість клітин корабля)
        self.width = int(name[0]) * 50
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
        # print(self.y)
        # Ініціалізація деяких змінних
        self.select = False  # Перевірка, чи вибрано корабель
        self.row = row
        self.cell = cell
        # Оновлюємо ігрове поле (записуємо розміри корабля)
        for count in range(int(name[0])):
            if rotate % 180 == 0:
                m_data.my_field[row][cell + count] = int(name[0])
            else:
                m_data.my_field[row + count][cell] = int(name[0])
        # Встановлюємо кордони корабля на полі
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.celled = None

    # Метод для перевірки, чи можна поставити корабель
    def check_enemy(self):
        yes_no = 0
        cells = []
        for count in range(int(self.name[0])):
            # Перевіряємо горизонтальне або вертикальне розміщення корабля
            if self.rotate % 180 == 0 and m_data.my_field[self.row][self.cell + count] != int(self.name[0]):
                cells.append([self.row, self.cell + count])
                yes_no += 1
            elif self.rotate % 180 != 0 and m_data.my_field[self.row + count][self.cell] != int(self.name[0]):
                cells.append([self.row + count, self.cell])
                yes_no += 1
                
        # Якщо перевірка пройдена успішно, оновлюємо поле
        if yes_no == int(self.name[0]):
            if self in m_data.all_ships:
                pass
            else:
                self.explosion = True
                m_data.all_ships.append(self)
                
                m_client.send(f"explosion:{self.row},{self.cell}".encode())

                field = m_data.enemy_field
                # print(cells)
                for celll in cells:
                    row = celll[0]
                    cell = celll[1]
                    # print(row, cell)
                    fill_field(m_data.enemy_field)
                    check(field=field, row=row + 1, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell - 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row + 1, cell=cell - 1, values=[5, 7])
                    check(field=field, row=row + 1, cell=cell, values=[5, 7])
                    check(field=field, row=row, cell=cell + 1, values=[5, 7])
                    check(field=field, row=row - 1, cell=cell, values=[5, 7])
                    check(field=field, row=row, cell=cell - 1, values=[5, 7])

    # Метод активації корабля при натисканні
    def activate(self, event):
        if self.rect.collidepoint(event.pos):
            self.select = True
            # print('eqw')
        else:
            self.place(event.pos)
            self.select = False
    # Метод для обертання корабля
    def rotate_ship(self):
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
    def place(self, pos):
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
                            yes_no = True
                    except:
                        pass
                        # print("капибара")
                    if yes_no:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7,
                            self.field_cor[1] + row * 55.7,
                            55.7, 55.7)
                        if rect.collidepoint(pos):
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell + count] = 0
                                else:
                                    m_data.my_field[self.row + count][self.cell] = 0
                            if self.celled:
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
                # print(cell1)
                if not cell1[0]:
                    cell1[0] = True
                    self.x = cell1[1][0]
                    self.y = cell1[1][1]
                    m_data.my_field[self.row][self.cell] = 0 
                    self.celled = count
                    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    for row in m_data.my_field:
                        print(row)      
                    break
                count += 1 
    # print(m_data.cells)
    for row in m_data.my_field:
        print(row)
# Функція перевірки на полі для кожної клітинки
def check(field, row, cell, values=[0, 5]):
    if row != -1 and -1 != cell:
        if row != 10 and 10 != cell:
            # Перевірка значення в клітинці
            if field[row][cell] == values[0]:
                field[row][cell] = values[1]
                if values[1] == 7:
                    # print(11)
                    image = m_images.Image(
                        progression="game",
                        name="miss",
                        x=725 + 55.7 * cell,
                        y=115 + 55.7 * row,
                        width=55.7,
                        height=55.7
                    )
# Заповнюємо поле
def fill_field(field: list):
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
