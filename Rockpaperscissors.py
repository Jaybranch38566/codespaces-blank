def Rockpaperscissors():
    import random

    choices = {"r": "rock", "p": "paper", "s": "scissors"}
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    print("Welcome to the Rock Paper Scissors game!")
    print("r=rock,p=paper,s=scissors")
    print("To quit the game,press 'q' and hit enter.")
    print("To play the game,enter your choice and hit enter.")
    print("The computer will randomly choose rock,paper,or scissors.")
    print("This game is played in a best of 3 format,so the first player to win 2 rounds wins the game.")

    while True:
        player_score = 0
        computer_score = 0

        while player_score < 2 and computer_score < 2:
            entry = input("Choose r, p, s, or q to quit: ").strip().lower()
            if entry == "q":
                print("Thanks for playing!")
                return
            if entry not in choices:
                print("Invalid choice. Please enter r, p, s, or q.")
                continue

            player = choices[entry]
            computer = random.choice(list(choices.values()))
            print(f"You chose {player}; the computer chose {computer}.")
            if player == computer:
                print("This round is a tie.")
            elif beats[player] == computer:
                player_score += 1
                print("You win this round!")
            else:
                computer_score += 1
                print("The computer wins this round!")
            print(f"Score: You {player_score} - {computer_score} Computer")

        if player_score == 2:
            print("You win! Would you like to play again?")
        else:
            print("You lose! Would you like to play again?")
        if input("Play again? (y/n): ").strip().lower() not in ("y", "yes"):
            print("Thanks for playing!")
            return
        Rockpaperscissors()