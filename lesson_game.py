import random

PAPER = 1
ROCK = 2
SCISSORS = 3


def greeting():
    print()
    print()
    print('Please make your choice:')
    print('-------')
    print('1: PAPER')
    print('2: ROCK')
    print('3: SCISSORS')
    print('-------')
    print('q: Exit')


def who_is_winner(user_choice, computer_choice):
    result = True
    if user_choice == PAPER and computer_choice == SCISSORS:
        result = False
    elif user_choice == ROCK and computer_choice == PAPER:
        result = False
    elif user_choice == SCISSORS and computer_choice == ROCK:
        result = False
    return result

def game():
    print('Hello from Game!')

    while True:
        greeting()
        user_choice = input('> ')

        if user_choice == 'q':
            print('Bye!')
            break

        # if int(user_choice) >= 1 and int(user_choice) <=3:
        valid_user_choice = user_choice.isnumeric() and 1 <= int(user_choice) <= 3

        if valid_user_choice:

            user_choice = int(user_choice)
            computer_choice = random.randint(1, 3)
            if computer_choice == user_choice:
                print('Tie!')
            else:
                user_winner = who_is_winner(user_choice, computer_choice)
                if user_winner:
                    print('User is winner! %d vs %d' % (user_choice, computer_choice))
                else:
                    print('Computer is winner! %d vs %d' % (user_choice, computer_choice))

                #print('Winner:', winner)
        else:
            print("Enter valid data: 1..3 or 'q'!")

game()