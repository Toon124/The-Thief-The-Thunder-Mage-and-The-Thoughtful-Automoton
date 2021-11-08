from TheDice import D20, D12, D10, D8, D6, D4
from CharacterStats import strength, dexterity, constitution, wisdom, intelligence, charisma
from AbilityModifiers import initiative, ability_mod

def main():
    character_name = input("What is your characters name?\n")

    strength_stat = strength()
    dexterity_stat = dexterity()
    constitution_stat = constitution()
    wisdom_stat = wisdom()
    intelligence_stat = intelligence()
    charisma_stat = charisma()

    str_mod = ability_mod(strength_stat)
    dex_mod = ability_mod(dexterity_stat)
    con_mod = ability_mod(constitution_stat)
    wis_mod = ability_mod(wisdom_stat)
    int_mod = ability_mod(intelligence_stat)
    cha_mod = ability_mod(charisma_stat)

    health = 10 + D20() + con_mod

    AC = 10 + dex_mod

    print("Your strength is {}\n".format(strength_stat))
    print("Your dexterity is {}\n".format(dexterity_stat))
    print("Your constitution is {}\n".format(constitution_stat))
    print("Your wisdom is {}\n".format(wisdom_stat))
    print("Your intelligence is {}\n".format(intelligence_stat))
    print("Your charisma is {}\n".format(charisma_stat))
    print("Your health is {}\n".format(health))
    print("Your Armor Class is {}\n".format(AC))

    print("You wake up in the woods on the outskirts of a small town with no recollection of how you got there.")

    choice = input("1. Walk towards the town\n2. Explore deeper into the woods\n3. Head to the clearing on the left\n")

    if choice == str(1):
        print("As you are walking towards the town a group of bandits jump out of the treeline!")
        choice = input("1. Roll for initiative\n 2. Run\n")
        if choice == str(1):
            init = initiative(dex_mod)
            print("Your initiative is {}".format(init))
            enemy_hp = D20() + 3
            enemy_ac = 10
            if init > 10:
                print("You go first!")
                while enemy_hp > 0:
                    print("What do you do?\n")
                    choice = input("1. Attack 2. Use a Potion")
                    if choice == str(1):
                        hit = D20() + 2
                        print("Rolling to hit...{}".format(hit))
                        if hit < enemy_ac:
                            print("You missed! Bandits turn!")
                        else:
                            damage = D8() + 2
                            print("You hit! Rolling for damage...{} damage!".format(damage))
                            enemy_hp -= damage
                            print("Bandits turn!")
                    else:
                        potion = D6()
                        healed = potion + health
                        print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                    enemy_hit = D20() + 2
                    if enemy_hit > AC:
                        enemy_damage = D6() + 2
                        print("The bandit attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                        health -= enemy_damage
                        print(health)
                        print("Your turn!")
                    else:
                        print("The bandit attacks...and misses!")
                        print("Your turn!")
            else:
                print("You go second!")
                while enemy_hp > 0:
                    enemy_hit = D20() + 2
                    if enemy_hit > AC:
                        enemy_damage = D6() + 2
                        print("The bandit attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                        health -= enemy_damage
                        print(health)
                        print("Your turn!")
                    else:
                        print("The bandit attacks...and misses!")
                        print("Your turn!")

                    print("What do you do?\n")
                    choice = input("1. Attack 2. Use a Potion 3. Run")
                    if choice == str(1):
                        hit = D20() + 2
                        print("Rolling to hit...{}".format(hit))
                        if hit < enemy_ac:
                            print("You missed! Bandits turn!")
                        else:
                            damage = D8() + 2
                            print("You hit! Rolling for damage...{} damage!".format(damage))
                            enemy_hp -= damage
                            print("Bandits turn!")
            print("After beating the bandit, you continue on your way towards the town.")
            print("Upon entering the town, you find that most of the residents are not present, except for a single old man towards the center of the town.")
            print("The old man approaches you and says 'Everyone left when the bandits came, and nobody's been back since. But then some monster came into town and ran off the bandits. It holed up in my home, and I haven't left because a family heirloom is in there. Dear adventurer would you please retrieve it for me so that I may leave?'")
            print("He points you towards the house and you make your way towards the house. The closer you get, the more clearly you can hear the growling of the monster living in the home.")
            choice = input("Do you 1. Enter through the front door or 2. Try to go through the back?")
            if choice == str(1):
                print("Upon entering the house you are immediately greeted with the face of a werewolf. Without a second thought the werewolf jumps at you, roll for initiative!")
                init = initiative(dex_mod)
                print("Your initiative is {}".format(init))
                enemy_hp = D20() + D20 + 15
                enemy_ac = 14
                if init > 15:
                    print("You go first!")
                    while enemy_hp > 0:
                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
                        else:
                            potion = D6()
                            healed = potion + health
                            print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")
                else:
                    print("You go second!")
                    while enemy_hp > 0:
                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")

                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion 3. Run")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
            else:
                enemy_hp = D20() + D20 + 15
                print("You walk around the back of the house and enter. Upon entering you find a werewolf sleeping and decide to make a preemptive strike, dealing {} damage".format(enemy_hp // 2))
                print("The werewolf wakes up and attacks, roll for initiative!")   
                init = initiative(dex_mod)
                print("Your initiative is {}".format(init))
                enemy_ac = 14
                if init > 15:
                    print("You go first!")
                    while enemy_hp > 0:
                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
                        else:
                            potion = D6()
                            healed = potion + health
                            print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")
                else:
                    print("You go second!")
                    while enemy_hp > 0:
                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")

                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion 3. Run")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!") 
            choice = input("Do you 1. Take the Gem for yourself or 2. Return the gem to the old man?")
            if choice == str(1):
                print("You leave the house with the gem in hand, not looking back, hoping the old man thinks you lost.\n GAME OVER")
            elif choice == str(2):
                print("You return the gem to the old man, he thanks you, and leaves ith the heirloom in hand, leaing you to your adventures.\n GAME OVER")
        elif choice == str(2):
            print("You run past the bandits and begin to close in on the small town")
            print("Upon entering the town, you find that most of the residents are not present, except for a single old man towards the center of the town.")
            print("The old man approaches you and says 'Everyone left when the bandits came, and nobody's been back since. But then some monster came into town and ran off the bandits. It holed up in my home, and I haven't left because a family heirloom is in there. Dear adventurer would you please retrieve it for me so that I may leave?'")
            print("He points you towards the house and you make your way towards the house. The closer you get, the more clearly you can hear the growling of the monster living in the home.")
            choice = input("Do you 1. Enter through the front door or 2. Try to go through the back?")
            if choice == str(1):
                print("Upon entering the house you are immediately greeted with the face of a werewolf. Without a second thought the werewolf jumps at you, roll for initiative!")
                init = initiative(dex_mod)
                print("Your initiative is {}".format(init))
                enemy_hp = D20() + D20 + 15
                enemy_ac = 14
                if init > 15:
                    print("You go first!")
                    while enemy_hp > 0:
                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
                        else:
                            potion = D6()
                            healed = potion + health
                            print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")
                else:
                    print("You go second!")
                    while enemy_hp > 0:
                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")

                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion 3. Run")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
            else:
                enemy_hp = D20() + D20 + 15
                print("You walk around the back of the house and enter. Upon entering you find a werewolf sleeping and decide to make a preemptive strike, dealing {} damage".format(enemy_hp // 2))
                print("The werewolf wakes up and attacks, roll for initiative!")   
                init = initiative(dex_mod)
                print("Your initiative is {}".format(init))
                enemy_ac = 14
                if init > 15:
                    print("You go first!")
                    while enemy_hp > 0:
                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!")
                        else:
                            potion = D6()
                            healed = potion + health
                            print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")
                else:
                    print("You go second!")
                    while enemy_hp > 0:
                        enemy_hit = D20() + 2
                        if enemy_hit > AC:
                            enemy_damage = D8() + 3
                            print("The werewolf attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                            health -= enemy_damage
                            print("Your turn!")
                        else:
                            print("The werewolf attacks...and misses!")
                            print("Your turn!")

                        print("What do you do?\n")
                        choice = input("1. Attack 2. Use a Potion 3. Run")
                        if choice == str(1):
                            hit = D20() + 2
                            print("Rolling to hit...{}".format(hit))
                            if hit < enemy_ac:
                                print("You missed! Werewolf's turn!")
                            else:
                                damage = D8() + 2
                                print("You hit! Rolling for damage...{} damage!".format(damage))
                                enemy_hp -= damage
                                print("Werewolf's turn!") 
            choice = input("Do you 1. Take the Gem for yourself or 2. Return the gem to the old man?")
            if choice == str(1):
                print("You leave the house with the gem in hand, not looking back, hoping the old man thinks you lost.\n GAME OVER")
            elif choice == str(2):
                print("You return the gem to the old man, he thanks you, and leaves ith the heirloom in hand, leaing you to your adventures.\n GAME OVER")
            else:
                print("Hey! That's not a choice!")
        else:
            print("Hey! That's not a choice!")

    elif choice == str(2):
        print(
            "\n Walking deeper into the woods, it seems to continue to get darker. You eventually reach the end of the path, where it splits into two directions."
        )
        choice = input("Do you 1. Take the path that leads to the left\n or 2. Take the path that leads to the right?\n")
        if choice == str(1):
            print("\n As you're walking down the left path you pass by a sign that says 'Elder Fairy Grove'. You eventually come up on a big hotspring with a large fairy tied up. She looks up at you and says 'Please free me, I need help'." )
            
            choice = input("\n Do you 1. Untie the fairy \n or 2.Turn around to go down the other path.\n")
            
            if choice == str(1):
                print("\n Upon untying the fairy she bursts into laughter and floats above you 'Oh yes finally a hero worry to be my servant.' She raises her hand and casts a spell.\n")
                
                wisdom_save = D20() + wis_mod

                if wisdom_save < 17:
                    print("\n You become charmed by the fairy and lose your will to act on your own motivation. As days pass by she makes you act as her champion. You start to lose memories of your past life as you replay them over and over as they are the only remnants of your past. You eventually become a mindless servant and your only desires and memories are that of fulfilling the tasks of the fairy.\n")
                    print("GAME OVER")
                else:
                    print("As you watch her cast the spell you are unaffected and she stares in awe \n 'WHY AREN'T YOU MY SERVANT?! I THOUGHT YOU WERE FIT TO BE MY CHAMPION BUT YOU ARE PRIDEFUL JUST LIKE THE REST AND FOR THAT YOU SHALL SUFFER!'\n")
                    print("She casts another spell but this time vines and leaves wrap around you and cover you and you can no longer move. You sit there parlyized and constrained and slowly starve to death and continue standing as a living tree.\n")
                    print("GAME OVER")

            elif choice == str(2):
                print("As you turn around your legs become heavy and rough. When you look down at them to see what is causing it you notice your legs have become rooted into the ground and bark is growing up your body parts. The fairy flies in front of you and begins speaking \n 'You adventurers only care about wealth! Now you will suffer.'\n You turn into a tree and slowly your conciousness starts to fade.\n")
                print("GAME OVER")
        
        elif choice == str(2):
            print("\n You begin walking down the right hand path. You are walking for a while and begin to lose your way. You start frantically going different directions before you realize you have become stuck in forest labrynth. You come up to another split in paths.")

            left_counter = 0
            right_counter = 0
            direction_counter = 0

            while left_counter < 4 and right_counter < 6 or direction_counter < 10:
                choice = input("You are at a split in the path, which direction do you choose?1. left \n or 2. right\n")
                if choice == str(1):
                    left_counter += 1
                    direction_counter += 1
                elif choice == str(2):
                    right_counter += 1
                    direction_counter += 1

            if direction_counter == 10 and left_counter < 4 and right_counter < 6:
                print(" \n You become lost in in the maze for the rest of your life and lose all hope of making it out. Some days you wander around and hope you find the exit.")
            if left_counter >= 4 and right_counter >= 6:
                print(" \n You make it out of the dreaded forest maze and in the distance see your house. You decide that you've had enough adventuring for one day and head inside and fall asleep.")

    elif choice == str(3):
        print("Upon reaching the clearing, you find a large stone building with a young man standing outside of it, he is holding a sign which says 'Finish the maze and win 100 gold'.\n")
        print("The man motions you over and begins to explain the maze, 'Listen listen! I have a quick way for you to make money! All you have to do is finish the maze! if you finish the maze you win 100 gold, but if you get stuck you'll have to fight whats in the maze! So, are you gonna do it?'")
        choice = input("1. Agree to take on the maze\n2. Decline his offer")

        if choice == str(1):
            print("That's great! Well, go on ahead! I'll wait at the other end for you!")
            print("You hesitantly enter the maze, and the door behind you shuts and locks.")
            choice = input("You are presented with three directions:\n1. Left\n2. Right\n3. Middle")
            
            if choice == str(1):
                choice = input("You are presented with two more options:\n1. Left\n2. Middle")
                if choice == str(1):
                    print("Uh oh! That's a dead end, a trap door opens below you and you fall in, Game Over!")
                elif choice == str(2):
                    choice = input("You are presented with 2 more options:\n1. Left\n2. Right")
                    if choice == str(1):
                        print("You can see the end! You make your way towards the door and make it outside, where you see the man from before. 'Well! it looks like you solved it! Here's your money!' He then hands you the money and you go about your adventure. Good Job!")
                    elif choice == str(2):
                        print("You step on a pressure plate and the walls all close, leaving you stuck in one spot forever, Game over!")

            elif choice == str(2):
                print("It's a dead end! You start to feel sleepy, and suddenly collapse, Game Over!")

            elif choice == str(3):
                print("As you walk through the middle you notice that all of the paths line up so that it is a straight shot to the end. However upon reaching the end you see that the man from before isn't there. Knowing that you've been scammed, you continue about your adventure, feeling a bit defeated. Good job?")

        elif choice == str(2):
            print("'You won't do my maze? How dare you!' The man jumps at you with a dagger, Roll for initiative!")
            init = initiative(dex_mod)
            print("Your initiative is {}".format(init))
            enemy_hp = D20() + 5
            enemy_ac = 12
            if init > 13:
                print("You go first!")
                while enemy_hp > 0:
                    print("What do you do?\n")
                    choice = input("1. Attack 2. Use a Potion")
                    if choice == str(1):
                        hit = D20() + 2
                        print("Rolling to hit...{}".format(hit))
                        if hit < enemy_ac:
                            print("You missed! Maze-Keeper's turn!")
                        else:
                            damage = D8() + 2
                            print("You hit! Rolling for damage...{} damage!".format(damage))
                            enemy_hp -= damage
                            print("Maze-Keeper's turn!")
                    else:
                        potion = D6()
                        healed = potion + health
                        print("You have {} health, the potion heals you...{}, You have {} health now!".format(health, potion, healed))

                    enemy_hit = D20() + 2
                    if enemy_hit > AC:
                        enemy_damage = D8() + 2
                        print("The Maze-Keeper attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                        health -= enemy_damage
                        print(health)
                        print("Your turn!")
                    else:
                        print("The Maze-Keeper attacks...and misses!")
                        print("Your turn!")
            else:
                print("You go second!")
                while enemy_hp > 0:
                    enemy_hit = D20() + 2
                    if enemy_hit > AC:
                        enemy_damage = D8() + 2
                        print("The Maze-Keeper attacks...and hits! Rolling for damage...{} damage!".format(enemy_damage))
                        health -= enemy_damage
                        print(health)
                        print("Your turn!")
                    else:
                        print("The Maze-Keeper attacks...and misses!")
                        print("Your turn!")

                    print("What do you do?\n")
                    choice = input("1. Attack 2. Use a Potion 3. Run")
                    if choice == str(1):
                        hit = D20() + 2
                        print("Rolling to hit...{}".format(hit))
                        if hit < enemy_ac:
                            print("You missed! Maze-Keeper's turn!")
                        else:
                            damage = D8() + 2
                            print("You hit! Rolling for damage...{} damage!".format(damage))
                            enemy_hp -= damage
                            print("Maze-Keeper's turn!")
            print("Upon beating the Maze-Keeper you find the 100 gold he promised on a pouch on his side. You see he no longer needs it, so you take it for yourself, and continue about your journey. Good job!")
    else:
        print("Hey! That's not a choice!")

if __name__ == "__main__":
    main()
