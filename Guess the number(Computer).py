import random

while True:
    try:
        print('\nWelcome to the game\nGuess the number')
        number = random.randint(1, 10)
        attempts = 5
        attempt = 0
        for i in range(5):
            print("\nattempts left:", attempts)
            x = int(input('Guess the number between 1,10: '))
            attempt += 1
            attempts -= 1
            if attempts <= 0:
                print("\nYou lose!, the number is", number)
                break

            if x == number:
                print("You won, attempts:", attempt)
                break
            else:
                print("Try again")
                continue
    except ValueError:
        print("Try again")
        continue

    user_choice = input("Play again (Yes/Exit): ").title()
    if user_choice == "Yes":
        continue
    else:
        break
