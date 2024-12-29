type = "/"
path = __file__.split("/")
if len(path) == 1:
    path = __file__.split("\\")
    type = "\\"
del path[-1]
del path[-1]
path.append("data")
# path.append("data.txt")
path = type.join(path)
read_data = {"nickname": "",
             "ip": "",
             "sound": True,
             "client_server": None,
             'wins':0,
             'loses':0
}
shop_data = {"coins":0,
             
             }
achievements_data = [
    {
        'name':'',
        'description':'',
        'has':False
    }
]
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
        print(error)
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
print(read_data)
# server.COLOR = (0,0,0)
# client.COLOR = (0,0,0)
# self.COLOR =(40,2,255)
# створення словника у якому містяться всі картинки для кожної стадії гри
list_blits = {
    "menu": [],
    "pre-game": [],
    "game": [],
    "lose": [],
    "win": [],
    "shop": []
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
turn = True
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