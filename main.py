sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1's score: "))
p2_score = int(input("Enter player 2's score: "))

if p1_score > p2_score:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

if p1_score == p2_score:
    print("It's a tie!")
    
