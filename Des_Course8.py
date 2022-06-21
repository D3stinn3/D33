import time


starter = {'njugu': 3, 'kashata': 2, 'jaba': 2, 'chaser': 3}  # this represents a global variables used in two functions


def string_justification(itemsDict, leftwidth, rightwidth):  # key argumaents then make up the local variables
    """string justification is considered during data arrangements"""
    man1 = 'Niaje si tushike jaba leo'
    man2 = 'Poa sana unadai tubuy starter inakaaje?'
    print(man1.rjust(5, '='))
    time.sleep(3)
    print(man2.ljust(5, '*'))
    if itemsDict['jaba'] >= 3:
        print('hio ndo size fiti ya jaba inatutosha sote!')
    else:
        print('Hio size ni kidogo labda tushike tena')

    print('EVENTS ZA SIKU YA JABA'.center(leftwidth + rightwidth))

    starter_ya_jaba = 'njugu'
    ni_ngapi = itemsDict[starter_ya_jaba]  # 'jaba' becomes the returned value in the starter dict
    for start in itemsDict:
        print('ndo hi jaba tools zetu ni gani?')
        time.sleep(2)
        print(f'baadhi ya tools zetu ndo hizi...{start}')
        if start == 'njugu' or start == 'kashata' and start == 'chaser':
            print('tools zote ziko inadi!')
            time.sleep(2)
            return ni_ngapi


string_justification(starter, 10, 5)


def list_ya_jabling(itemsDict, leftwidth, rightwidth):
    print('Jaba Items In Cart'.center(leftwidth + rightwidth))
    for k, v in itemsDict.items():
        print(k.ljust(leftwidth, '-') + str(v).rjust(rightwidth))


list_ya_jabling(starter, 20, 5)
list_ya_jabling(starter, 30, 10)


def the_glass_house(j, k):
    name = 'destinne'
    name1 = 'maria'
    for j in name:
        j += '*'
        print(name.rjust(5, '-') + '\t' + j)
        break
    for k in name1:
        k += '#'
        print(name1.rjust(5, '-') + '\t' + k)
        break


def the_glass_house1():
    guests_at_party = {('guest1', 'guest2'): 'kiruma', 'guest': 'kiruma_double'}
    type_of_guest = 'guest'
    type_of_food = 'kiruma_double'
    good_samaritan = guests_at_party[type_of_guest]
    bad_samaritan = guests_at_party.keys()

    for gue in guests_at_party:
        print('the meeting  in this room involved a number of people including ' + '\t' + str(gue))
        print('type of food: ' + str(type_of_food))
        if gue == good_samaritan and gue == bad_samaritan:  # derives from the key in guests_at_party dict
            print('the next room number of people in the meeting changed to ' + '\t' + str(gue))
            print('type of food: ' + str(type_of_food))
            break


the_glass_house('*', '#')
the_glass_house1()