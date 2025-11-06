import random 

def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
   players = input('Enter the number of players (1-4): ')
   if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
         break
    else:
       print("Invalid, try again")
    
max_score = 50
player_scores = [0 for _ in range(players)] 

while max(player_scores) < max_score:
    for i in range(players):
      print("\nPlayer", i + 1, "'s turn\n")
      print("Current scores:", player_scores[i], "\n")
      current_scores = 0

    while True:
            should_roll = input("Do you want to roll the dice? (yes/no): ")
            if should_roll.lower() != 'yes':
                print("Game ended by user.")
                break
    
            value = roll()
            if value == 1:
                print("Rolled a 1! No points this turn.")
                current_scores = 0
                break
            else:
                 current_scores += value
                 print("You rolled a:", value)
    
    print("Current turn score:", current_scores)

    player_scores[i] += current_scores
    print("Total scores:", player_scores[i])

max_score  = max(player_scores)
winner_i = player_scores.index(max_score)
print("player number", winner_i + 1, "wins with a score of", max_score)
