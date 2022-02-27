
aliens = [] 


for alien_num in range(30):

    new_alien = {
        "color" : "green",
        "points" : 5,
        "speed" : "slow"
    }
    aliens.append(new_alien)

for alien in aliens[10:20]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    

for alien in aliens[20:30]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'


def alien_total():
    print("\n\nNumber of green aliens : {}".format(len([alien for alien in aliens[0:10] if isinstance(alien, dict)])))
    print("Number of yellow aliens : {}".format(len([alien for alien in aliens[10:20] if isinstance(alien, dict)])))
    print("Number of red aliens : {}".format(len([alien for alien in aliens[20:30] if isinstance(alien, dict)])))


for alien in aliens:
    alien['x_coordinate'] = 0
    alien['y_coordinate'] = 15


def speed(a):
        if a == 'green':
            x_increment = 3
            y_increment = 6

        elif a == 'yellow':
            x_increment = 5
            y_increment = 10

        else:
            x_increment = 7
            y_increment = 14

        print("\n\nNew " + str(a) + " alien coordinate is : {}\n\n".format((alien['x_coordinate'] + x_increment, alien['y_coordinate'] + y_increment)))


alien_total()
speed('green')
