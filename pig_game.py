import random


# Function to roll the dice
def roll():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value, max_value)
    return roll


# Ask the number of players (2-4) 
while True:
    player=input("Enter no. of Players(2-4): ")
    if player.isdigit():
        player=int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between 2-4 ")
    else:         
        print("Invalid, try again")


# Maximum score
max_score = 20
player_score = [0 for _ in range(player)]


# Game loop
while max(player_score) < max_score:

    for player_idx in range(player):
        print("\nPlayer number",player_idx + 1, "turn has just started!\n")
        current_score = 0
    
        while True:
            should_roll = input("Would you like to roll(y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn down! ")
                current_score = 0
                break
            else:
                current_score = current_score + value
                print(f"You rolled a: {value}")
    
            print("Your current soure is: ", current_score)
            
        player_score[player_idx] = player_score[player_idx] + current_score 
        print("Total score is: ",player_score[player_idx])

winner = player_score.index(max(player_score)) + 1
print(f"\nPlayer {winner} wins with a score of {max(player_score)}!")