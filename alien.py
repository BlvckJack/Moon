aliens = [] 


for alien_num in range(30):

    new_alien = {
        "color" : "green",
        "points" : 5,
        "speed" : "slow"
    }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("\t\n Total number of aliens : {}".format(len(aliens)))
