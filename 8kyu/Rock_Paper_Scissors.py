#DESCRIPTION:
#Rock Paper Scissors
#Let's play! You have to return which player won! In case of a draw return Draw!.

#Examples(Input1, Input2 --> Output):

#"scissors", "paper" --> "Player 1 won!"
#"scissors", "rock" --> "Player 2 won!"
#"paper", "paper" --> "Draw!"

# My Solution:
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"