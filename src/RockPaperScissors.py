import random

def convert(s):
    if s == ('r' or 'rock' or 'R' or 'Rock'):
        return 'Rock'
    elif s == ('p' or 'paper' or 'P' or 'Paper'):
        return 'Paper'
    elif s == ('s' or 'scissors' or 'S' or 'Scissors'):
        return 'Scissors'
    elif s == ('q' or 'quit' or 'Q' or 'Quit'):
        return 'q'
    
    else: return 'e'

# return: 0 player, 1 computer, 2 tie
def verdict(i, com):
    if i == com:
        return 2
    
    match i:
        case 'Rock':
            if com == 'Scissors': return 0
            else: return 1

        case 'Paper':
            if com == 'Rock': return 0
            else: return 1

        case 'Scissors':
            if com == 'Paper': return 0
            else: return 1

class RockPaperScissors():
    def __init__(self):
        self.score = [0, 0, 0]
        
                



