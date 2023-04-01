global location
location = 'развилка'


def crossroads():
    location = input('Куда пойдем? ')
    return location


def shop():
    t = input('Чо купим? ')
    return t


world = {
    'развилка': 'crossroads()',
    'лавка': 'shop()'
}


eval(world[location])
