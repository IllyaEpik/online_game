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
#     "fire_rocket":2,
#     "Anti_fire":10,
select_weapon = None
attack = None
time_for_radar = 0
rect_for_radar = None
coins = 0
list_achievements = []
list_for_radar = []
buffs = []
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

