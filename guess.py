import random
number = random.randint(1,15)
chances = 0
while chances < 5:
    count = int (input ('number'))
    if count == number :
        print('YOU WON')
    elif count < number :
        print('guess a higher number')
    else :
        print('guess a lower number')
    chances += 1


