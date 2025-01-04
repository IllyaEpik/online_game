import pygame, os, time, threading
import modules.data as m_data
width = 400
height = 120
y = 0
x = 1280
# rect = pygame.Rect(x,y,width,height)
# achievement = False

class achievement():
    def __init__(self,name):
        global x,y,width,height
        if m_data.achievements_data[name]['has'] == "False" or 1:
            self.FONT = pygame.font.SysFont("algerian", 40)
            self.rect = pygame.Rect(x,y,width,height)
            m_data.list_achievements.append(self)
            self.text = name.split(' ')
            size = self.FONT.size(" ".join(self.text))
            if size[0] < 300:
                self.text = [" ".join(self.text)]
            elif len(self.text)-2:
                list_text = []
                text = ''
                
                for text_for in self.text:
                    
                    size = self.FONT.size(text+text_for)
                    if size[0] < 280:
                        text += text_for+' '
                    print(size,text,text_for,list_text)
                    if size[0] > 280:
                        
                        list_text.append(text)
                        text = text_for
                    elif self.text[-1] == text_for:
                        list_text.append(text)
                if not text_for in list_text[-1]:
                    size = self.FONT.size(text+text_for)
                    if size[0] < 280:
                        text += text_for+' '
                    print(size,text,text_for,list_text)
                    if size[0] > 280:
                        
                        list_text.append(text)
                        text = text_for
                    elif self.text[-1] == text_for:
                        list_text.append(text)
                self.text = list_text
            self.time = 5
            self.activate_timer = False
            self.deactivate_timer = False
            text_cor = []
            self.name = name
            with open(m_data.path+m_data.type+'achievements'+m_data.type+name+'.txt', "w") as file:
                file.write('True')
                # самонаводящая ракета попадает в случайный кораблик
                # мину 3*3
                # радар 5*5
                # огонь 
                # ремонт и огнетушитель
                # монеты не сохраняются в базе данных
    def move(self):
        global x,y,width,height
        print('achievement')
        # if self.rect.x < 1280-395:
        if not self.activate_timer:
            if self.rect.x < 1280-395 and not self.deactivate_timer:
                self.activate_timer = True
            
                threading.Thread(target=self.timer,daemon=1).start()
            elif self.rect.x > 1280 and self.deactivate_timer:
                m_data.list_achievements.remove(self)
            else:
                if not self.deactivate_timer:
                    self.rect.x -= 15
                else:
                    self.rect.x += 15
                
        # achievement = True
        # rect = pygame.Rect(x,y,width,height)
        # 1280 832

    def blit(self,screen:pygame.Surface,multiplier_x,multiplier_y):
        self.img = pygame.image.load(os.path.abspath(f"{__file__}/../../images/achievements/{self.name}.png"))
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.img.set_colorkey((0, 0, 0))
        rect = pygame.Rect(
            self.rect.x*multiplier_x,
            self.rect.y*multiplier_y,
            self.rect.width*multiplier_x,
            self.rect.height*multiplier_y
            )
        square = pygame.Surface((rect.width,rect.height))
        square.fill((69, 69, 69))
        square.set_alpha(200)
        screen.blit(square,rect)
        screen.blit(self.img, ((self.rect.x+10)*multiplier_x,(self.rect.y)*multiplier_y))
        count = 0
        for text in self.text:
            if multiplier_x > multiplier_y:
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
            else:
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
            height = self.FONT.size(text)[1]
            
            y = (self.rect.y+10+height*count) * multiplier_y
            # задаємо x для тексту
            x = (self.rect.x + 120)*multiplier_x
            # відображення тексту на екрані
            print((self.rect.x+10))
            screen.blit(self.FONT.render(text,True,(0,0,0)), (x, y))
            count += 1
        # rect.
        # pygame.draw.rect(screen,(69, 69, 69),rect)
    def timer(self):
        while self.time != 0:
            self.time -= 1
            time.sleep(1)
        self.deactivate_timer = True
        self.activate_timer = False
    # def get_achievement(name,multiplier_x,multiplier_y,screen):
    #     global x,y,width,height,rect
    #     print('achievement')
    #     # achievement = True
    #     rect = pygame.Rect(x,y,width,height)
    #     # 1280 832
    #     rect.x *=multiplier_x
    #     rect.y *=multiplier_y
    #     rect.width *=multiplier_x
    #     rect.height *=multiplier_y

    #     