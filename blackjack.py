import p1_random as p1

rng = p1.P1Random()

# Game Checks & Data
user_input = '1'
game_number = 1
player_hand = 0
player_wins = 0
dealer_wins = 0
game_ties = 0


# Function: Displaying Menu for User
def user_menu():
    print()
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit\n")


# Function: Displays Game Statistics
def game_statistics(game_num1, game_num2, game_num3, game_num4):
    print()
    print(f"Number of Player wins: {game_num1}")
    print(f"Number of Dealer wins: {game_num2}")
    print(f"Number of tie games: {game_num3}")
    # Game and Win Check
    if game_num4 == 1:
        print(f"Total # of games played is: {game_num4}")
        game_percentage = (game_num1 / game_num4) * 100
        game_percentage = "%.1f" % game_percentage
        print(f"Percentage of Player wins: {game_percentage}%")
    else:
        print(f"Total # of games played is: {game_num4 - 1}")
        game_percentage = (game_num1 / (game_num4 - 1)) * 100
        game_percentage = "%.1f" % game_percentage
        print(f"Percentage of Player wins: {game_percentage}%")


# Game Generation
while user_input != '4':
    print(f"START GAME #{game_number}")

    # Draw Random Card
    card_name = rng.next_int(13) + 1

    # Transform Card into a Value
    card_value = 0
    if card_name == 13:
        print("Your card is a KING!")
        card_value = 10
    elif card_name == 12:
        print("Your card is a QUEEN!")
        card_value = 10
    elif card_name == 11:
        print("Your card is a JACK!")
        card_value = 10
    elif card_name > 1 & card_name <= 10:
        print(f"Your card is a {card_name}!")
        card_value = card_name
    elif card_name == 1:
        print("Your card is a ACE!")
        card_value = 1

    # Current Hand
    player_hand += card_value
    print(f"Your hand is: {player_hand}\n")

    # Game Options
    current_game = True
    while current_game:

        # User Menu
        user_menu()
        user_input = input("Choose an option: ")
        print()

        # User Choices
        if user_input == '1':  # Draw Card

            # Draw and Transform Again
            card_name = rng.next_int(13) + 1
            card_value = 0
            if card_name == 13:
                print("Your card is a KING!")
                card_value = 10
            elif card_name == 12:
                print("Your card is a QUEEN!")
                card_value = 10
            elif card_name == 11:
                print("Your card is a JACK!")
                card_value = 10
            elif card_name > 1 & card_name <= 10:
                print(f"Your card is a {card_name}!")
                card_value = card_name
            elif card_name == 1:
                print("Your card is a ACE!")
                card_value = 1

            player_hand += card_value

            # Player Hand Check
            if player_hand > 21:
                print(f"Your hand is: {player_hand}\n")
                print("You exceeded 21! You lose.")
                dealer_wins += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
            elif player_hand == 21:
                print(f"Your hand is: {player_hand}\n")
                print("BLACKJACK! You win!")
                player_wins += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
            else:
                print(f"Your hand is: {player_hand}")
                print()
        elif user_input == '2':  # Hold Hand
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()

            # Dealer Hand Check
            if dealer_hand > 21:
                print("You win!")
                player_wins += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
            elif dealer_hand > player_hand & dealer_hand <= 21:
                print("Dealer wins!")
                dealer_wins += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                game_ties += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
            elif dealer_hand < player_hand:
                print("You win!")
                player_wins += 1
                player_hand = 0
                dealer_hand = 0
                print()
                current_game = False
        elif user_input == '3':  # Print Game Statistics
            game_statistics(player_wins, dealer_wins, game_ties, game_number)
        elif user_input == '4':  # Exit Game
            player_hand = 0
            dealer_hand = 0
            current_game = False
        else:  # Invalid Input Check
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue

    # Incrementing Number of Games
    game_number += 1
