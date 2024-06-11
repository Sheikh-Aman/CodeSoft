import random


def Computer_Turn():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def Check_Winner(user_input, computer_input):

    if user_input == computer_input:
        return 'Draw Match'
    elif (user_input == 'rock' and computer_input == 'scissors') or \
            (user_input == 'scissors' and computer_input == 'paper') or \
            (user_input == 'paper' and computer_input == 'rock'):
        return 'user'
    else:
        return 'computer'


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or (exit) to quit: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing ! [Better Luck Next Time!!! ]")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

        computer_choice = Computer_Turn()
        print(f"Computer Turn: {computer_choice}")

        result = Check_Winner(user_choice, computer_choice)

        if result == 'Draw Match':
            print("It's a Draw !")
        elif result == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        print(f"Current Scores: You : {user_score} | Computer : {computer_score}")

        playMore = input("Do you want to play again? ['rock', 'paper', 'scissors'] (yes/no): ").lower()
        if playMore != 'yes':
            print("Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thank You for Playing!")
            break


if __name__ == "__main__":
    main()
