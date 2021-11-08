from TheDice import D6


def strength():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    STR = highest_roll + second_highest_roll + third_highest_roll
    return STR


def dexterity():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    DEX = highest_roll + second_highest_roll + third_highest_roll
    return DEX


def constitution():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    CON = highest_roll + second_highest_roll + third_highest_roll
    return CON


def wisdom():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    WIS = highest_roll + second_highest_roll + third_highest_roll
    return WIS


def intelligence():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    INT = highest_roll + second_highest_roll + third_highest_roll
    return INT


def charisma():
    first_roll = D6()
    second_roll = D6()
    third_roll = D6()
    fourth_roll = D6()

    first_roll_2counter = 0
    second_roll_2counter = 0
    third_roll_2counter = 0
    fourth_roll_2counter = 0

    if first_roll == 1:
        first_roll = D6()
    if first_roll == 2 and first_roll_2counter < 1:
        first_roll = D6()
        first_roll_2counter += 1
    if second_roll == 1:
        second_roll = D6()
    if second_roll == 2 and second_roll_2counter < 1:
        second_roll = D6()
        second_roll_2counter += 1
    if third_roll == 1:
        third_roll = D6()
    if third_roll == 2 and third_roll_2counter < 1:
        third_roll = D6()
        third_roll_2counter += 1
    if fourth_roll == 1:
        fourth_roll = D6()
    if fourth_roll == 2 and fourth_roll_2counter < 1:
        fourth_roll = D6()
        fourth_roll_2counter += 1

    highest_roll = max(first_roll, second_roll, third_roll, fourth_roll)

    if highest_roll == first_roll:
        second_highest_roll = max(second_roll, third_roll, fourth_roll)
        if second_highest_roll == second_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(second_roll, third_roll)
    elif highest_roll == second_roll:
        second_highest_roll = max(first_roll, third_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(third_roll, fourth_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, third_roll)
    elif highest_roll == third_roll:
        second_highest_roll = max(first_roll, second_roll, fourth_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, fourth_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, fourth_roll)
        elif second_highest_roll == fourth_roll:
            third_highest_roll = max(first_roll, second_roll)
    else:
        second_highest_roll = max(first_roll, second_roll, third_roll)
        if second_highest_roll == first_roll:
            third_highest_roll = max(second_roll, third_roll)
        elif second_highest_roll == second_roll:
            third_highest_roll = max(first_roll, third_roll)
        elif second_highest_roll == third_roll:
            third_highest_roll = max(first_roll, second_roll)

    CHA = highest_roll + second_highest_roll + third_highest_roll
    return CHA