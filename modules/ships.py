import modules.images as m_images
import modules.data as m_data
import pygame 

class Ship(m_images.Image):
    def __init__(self, x: int, y: int, name='1', row = 0, cell = 0, field_cor = [59, 115], rotate = 0,add = True):
        self.width = int(name[0]) * 50
        self.height = 50
        print(self.height)
        super().__init__(self.width, self.height, x, y, name, "F", rotate)
        self.x += (cell * 55.7)
        self.y += (row * 55.7)
        if add :
            m_data.all_ships.append(self)
        print(self.y)
        self.select = False
        self.row = row
        self.cell = cell
        
        for count in range(int(name[0])):
            if rotate %180 == 0:
                m_data.my_field[row][cell+count] = int(name[0])
            else:
                m_data.my_field[row+count][cell] = int(name[0])
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
        self.celled = None


    def activate(self, event):
        if self.rect.collidepoint(event.pos):
            self.select = True
            print('eqw')
        else:
            self.place(event.pos)
            self.select = False

    def rotate_ship(self): 
        print(2132132312123123231213231)

        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell+count] = 0
            else:
                m_data.my_field[self.row+count][self.cell] = 0
        self.rotate = self.rotate + 90
        fill_field(m_data.my_field)
        no_yes= True 
        try:
            for count in range(int(self.name[0])):
                if self.rotate % 180 == 0:
                    if m_data.my_field[self.row][self.cell+count] != 0:
                        no_yes = False
                else:
                    if m_data.my_field[self.row+count][self.cell] != 0:
                        no_yes = False
        except:no_yes = False
        if no_yes: 
            self.update_image()
            if self.rotate%180 ==0 :
                self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
            else: 
                self.rect = pygame.Rect(self.x, self.y,self.height,self.width)
        else: 
            self.rotate -= 90
            # self.select = True
        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell+count] = int(self.name[0])
                
            else:
                m_data.my_field[self.row+count][self.cell] = int(self.name[0])
        
    def place(self, pos):
        # print(pos)
        if self.select:
            print(self.field.collidepoint(pos))
            for row in range(10):
                for cell in range(10):
                    
                    #if m_data.my_field[row][cell] == 5:
                    yes_no = False
                    try:
                        yes_no_1 = True
                        for count in range(int(self.name[0])):
                            # print(count,(self.name[0]),row,cell)
                            if self.rotate % 180 == 0:
                                if m_data.my_field[row][cell+count] != 0 and m_data.my_field[row][cell+count] != 5 :
                                    yes_no_1 = False    
                            else:                                
                                if m_data.my_field[row][cell+count] != 0 and m_data.my_field[row][cell+count] != 5:
                                    yes_no_1 = False   
                        if yes_no_1:

                            for count in range(int(self.name[0])):
                                # print(count,(self.name[0]),row,cell)
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = 0
                                else:
                                    m_data.my_field[self.row+count][self.cell] = 0
                            fill_field(m_data.my_field)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = int(self.name[0])
                                else:
                                    m_data.my_field[self.row+count][self.cell] = int(self.name[0])
                            yes_no_1 = True
                            for count in range(int(self.name[0])):
                            # print(count,(self.name[0]),row,cell)
                                if self.rotate % 180 == 0:
                                    if m_data.my_field[row][cell+count] != 0:
                                        yes_no_1 = False    
                                else:                                
                                    if m_data.my_field[row][cell+count] != 0:
                                        yes_no_1 = False   
                            yes_no = True
                    except:print("капибара")
                    # try:
                        # m_data.my_field[row][cell] = 0
                    # except:
                    if yes_no:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7,
                            self.field_cor[1] + row * 55.7,
                            55.7,55.7)
                        if rect.collidepoint(pos):
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = 0
                                else:
                                    m_data.my_field[self.row+count][self.cell] = 0
                            if self.celled:
                                m_data.cells[self.name[0]][self.celled][0] = False
                                self.celled = None
                            self.row = row
                            self.cell = cell
                            self.x = (cell * 55.7) + self.field_cor[0]
                            self.y = (row * 55.7) + self.field_cor[1]
                            self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[row][cell+count] = int(self.name[0])
                                else:
                                    m_data.my_field[row+count][cell] = int(self.name[0])
                            self.select = False
                            fill_field(m_data.my_field)
                            
                            for row in m_data.my_field:
                                print(row)
                            return True
            count = 0
            # print(int(self.name[0])
            for cell1 in m_data.cells[self.name[0]]:
                print(cell1)
                if not cell1[0]:
                    cell1[0] = True
                    self.x = cell1[1][0]
                    self.y = cell1[1][1]
                    m_data.my_field[self.row][self.cell] = 0 
                    self.celled = count
                    self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
                    for row in m_data.my_field:
                        print(row)      
                    break
                count += 1 
            # if self.field_cor[0] + 10 * 55.7 > cor[0]:
            #     pax = 59, y = 115ss
    print(m_data.cells)
    for row in m_data.my_field:
        print(row)
def check(field, row, cell):
    if row != -1 and -1 != cell:
        if row != 10  and 10 != cell:
            # print(row,cell)
            if field[row][cell] == 0:
                field[row][cell] = 5

def fill_field(field:list):
    clear_field(field)
    for row in range(10):
        for cell in range(10):
            cell_on_field = field[row][cell]
            if cell_on_field != 5 and cell_on_field != 0:
                check(field= field, row= row+1, cell= cell+1)
                check(field= field, row= row-1, cell= cell-1)
                check(field= field, row= row-1, cell= cell+1)
                check(field= field, row= row+1, cell= cell-1)
                
                check(field= field, row= row+1, cell= cell)
                check(field= field, row= row, cell= cell+1)
                check(field= field, row= row-1, cell= cell)
                check(field= field, row= row, cell= cell-1)

def clear_field(field):
    for row in range(10): 
        for cell in range(10):
            if field[row][cell] == 5:
                field[row][cell] = 0
size_ship = "1"
for count in range(10):
    ship = Ship(x = 59, y = 115, name = size_ship)
    ship.select = True
    ship.place((684, 220))
    ship.select = False
    if count == 3:
        size_ship = "2"
    if count == 6:
        size_ship = "3"
    if count == 8:
        size_ship = "4"

# ship1 = Ship(x = 59, y = 115, cell = 8, row = 1)
# ship2 = Ship(x = 59, y = 115, cell = 5, row = 2)
# ship3 = Ship(x = 59, y = 115, cell = 2, row = 3)
fill_field(m_data.my_field)
ship.place((1,1))