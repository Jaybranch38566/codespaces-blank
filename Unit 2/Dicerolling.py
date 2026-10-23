def Dicerolling():
    print("Welcome to the Dice Rolling Game!")
    print("Roll the dice by pressing 'r' and hitting enter.")
    print("To quit the game, press 'q' and hit enter.")

    choice = input().lower()

    if choice == 'r':
        import random
        roll = random.randint(1, 7)
        print(f"You rolled a {roll}.")

        if roll == 7:
            print("You rolled a 7! You win the game and score 10 points!")
        else:
            print("You didn't roll a 7! You lose the game and lose 5 points.")
    elif choice == 'q':
        print("Thanks for playing!")
    else:
        print("Invalid input.")

Dicerolling()