import random

user_score = 0
computer_score = 0

print("===== ROCK-PAPER-SCISSORS GAME =====")

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1/2/3): ")

    choices = ["Rock", "Paper", "Scissors"]

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Please choose 1, 2, or 3.")
        continue

    user = choices[int(user_choice) - 1]
    computer = random.choice(choices)

    print("\nYour choice     :", user)
    print("Computer choice :", computer)

    # Game Logic
    if user == computer:
        print("Result: It's a TIE!")

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):

        print("Result: YOU WIN!")
        user_score += 1

    else:
        print("Result: YOU LOSE!")
        computer_score += 1

    # Display Score
    print("Score - You:", user_score, "| Computer:", computer_score)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===== FINAL SCORE =====")
        print("Your Score     :", user_score)
        print("Computer Score :", computer_score)
        print("Thank you for playing!")
        break