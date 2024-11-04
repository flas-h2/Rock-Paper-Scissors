import random

def title_printout():
    print("""
.-. .-. .-. . .     .-. .-. .-. .-. .-.     .-. .-. .-. .-. .-. .-. .-. .-. 
|(  | | |   |<      |-' |-| |-' |-  |(      `-. |    |  `-. `-. | | |(  `-. 
' ' `-' `-' ' ` ,   '   ` ' '   `-' ' ' ,   `-' `-' `-' `-' `-' `-' ' ' `-' 
    _______           _______               _______ 
---'   ____)      ---'   ____)____     ---'    ____)____ 
      (_____)               ______)               ______) 
      (_____)               _______)           __________) 
      (____)               _______)           (____) 
---.__(___)       ---.__________)      ---.__(___)
            """)


def player_move(round_num, user_choice):
    """Function that handles the players move."""
    choices = ["Rock", "Paper", "Scissors"]
    print(f"\nRound {round_num}")
    print("Enter 1 for Rock, 2 for Paper, or 3 for Scissors:")
    print(f"You played {choices[user_choice - 1]}")
    return user_choice


def computer_move():
    """Function that handles the computers move."""
    comp_choice = random.randint(1, 3)
    choices = ["Rock", "Paper", "Scissors"]
    print(f"The computer played {choices[comp_choice - 1]}")
    return comp_choice


def check_win(player, computer):
    """Checks for who wins each turn."""
    if player == computer:
        return "Tie"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "Win"
    else:
        return "Loss"


def meta_data(outcome):
    """Displays the outcome of each play."""
    outcomes = {"Win": "You win!", "Loss": "You lose!", "Tie": "It's a tie!"}
    print(outcomes[outcome])
    return outcome


def display_final_report(game_data):
    """Prints out the final table with all the games meta data"""
    print("\n" + "#" * 52)
    print("##########  Paper, Rock, Scissors Report  ##########")
    print("#" * 52)
    print("| Round | User Played | Computer Played | Outcome |")
    print("-" * 52)
    
    wins, ties, losses = 0, 0, 0
    for round_num, (user_played, comp_played, outcome) in enumerate(game_data, start=1):
        print(f"|  {round_num:^5} | {user_played:^12} | {comp_played:^14} | {outcome:^7} |") # fills whitespace inside the board so the board isn't wacky
        if outcome == "Win":
            wins += 1
        elif outcome == "Tie":
            ties += 1
        else:
            losses += 1
    
    total_rounds = len(game_data)
    print("-" * 52)
    print(f"Summary: {int(wins / total_rounds * 100)}% Wins, {int(losses / total_rounds * 100)}% Losses, {int(ties / total_rounds * 100)}% Ties")
    print("You won the series" if wins > losses else "You lost the series" if losses > wins else "The series was a tie")


def main():
    """Main function of the code."""
    title_printout()
    rounds = 5
    game_data = []
    round_num = 1

    while round_num <= rounds:
        try:
            user_input = int(input("\nEnter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
            if user_input not in [1, 2, 3]:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        player_choice = player_move(round_num, user_input)
        computer_choice = computer_move()
        outcome = check_win(player_choice, computer_choice)
        meta_data(outcome)
        game_data.append((["Rock", "Paper", "Scissors"][player_choice - 1], ["Rock", "Paper", "Scissors"][computer_choice - 1], outcome))
        round_num += 1

    display_final_report(game_data)


if __name__ == "__main__":
    main()