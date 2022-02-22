# ROCK-PAPER-SCISSOR

print(" What do you want to choose? rock, paper or scissors?")
p1 = input()
print(" What do you want to choose? rock, paper or scissors?")
p2 = input()

def game(a, b):
    if a == b:
        return "It's a tie!"
    elif a == 'rock':
        if b == 'scissors':
            return "Rock beats scissors!"
        else:
            return "Paper beats rock!"
    elif a == 'scissors':
        if b == 'paper':
            return "Scissors beats paper!"
        else:
            return "Rock beats scissors!"
    elif a == 'paper':
        if b == 'rock':
            return "Paper beats rock!"
        else:
            return "Scissors beat paper!"
    else:
        return "You have not entered rock, paper or scissors. "
    
print(game(p1, p2))
