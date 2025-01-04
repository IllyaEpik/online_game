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
shop_data = {"tier":0,
             
             }
list_achievements = []
# achievements_data = [
#     {
#         'name':'',
#         'description':'',
#         'has':False,
#         'tier':0
#     }
# ]
achievements_data = {
    "Total Domination":{
        'description':'Destroy 4 ships in one turn',
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
    "Minted Coin":{
        'description':'Earn money for the first time',
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
        'description':'Destroy an "Oreshnik" using AA defense',
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
    "Launched Oreshnik":{
        'description':'Launch an Oreshnik',
        'has':False,
        'tier':1
    },
    "Into the Sunset... ":{
        'description':'Unlock all achievements',
        'has':False,
        'tier':1
    },
    "Extrovert":{
        'description':'Play with 10 friends',
        'has':False,
        'tier':1
    },
    "Losing Streak":{
        'description':'Lose three times in a row',
        'has':False,
        'tier':1
    },
    "Big Spender":{
        'description':'Spend 1000 tier',
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
    },
    # tier
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
for achievement in achievements_data:
    # name = achievement['name']
    name = achievement
    try:
        with open(path+type+'achievements'+type+name+'.txt', "r") as file:
            achievements_data[achievement]['has'] = file.read()
            print(achievements_data[achievement]['has'])
    except:
        with open(path+type+'achievements'+type+name+'.txt', "w") as file:
            file.write('False')
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

