global location
location = 'развилка'

player_inv = list()


def crossroads():
    location = input('Куда пойдем? ')
    world[location]()


def shop():
    t = input('Чо купим? ')
    player_inv.append(t)
    world['развилка']()


def quit_game():
    print(player_inv)
    exit()


world = {
    'развилка': lambda: crossroads(),
    'лавка': lambda: shop(),
    'выйти': lambda: quit_game()
}


world[location]()
