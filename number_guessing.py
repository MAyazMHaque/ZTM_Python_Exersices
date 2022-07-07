import random

while True:
    try:
        guess_num = int(input('Please enter a number from 0 to 9: '))
        rand_num = random.randint(0, 9)
        if 9 > guess_num > 0:
            if guess_num == rand_num:
                print(f'the computer generated number is {rand_num}')
                print('You got the right number')
                break
        else: print('Please put a number between 0 and 9')

    except ValueError:
        print('Please put a number between 0 and 9')








