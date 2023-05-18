import random
guesses_made = 0
var = random.randint(1, 100)
while True:
    user_input = int(input('Hi,guess the number from 1 till 100'))
    if user_input == var:
        guesses_made += 1
        print(f'WoW,! Bingo! You guessed it! It was your {guesses_made} attempt')
        break
    elif user_input < var:
        print("Nice try, but the number is bigger, please try again")
        guesses_made += 1
    if user_input > var:
        print('Nice try, but the number is less, please try again')
        guesses_made += 1