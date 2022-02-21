
aliens = [] 

for alien_num in range(1,27):

    new_alien = {
        "color" : "green",
        "points" : 5,
        "speed" : "slow"
    }
    aliens.append(new_alien)

for alien in aliens:
    print(alien)
