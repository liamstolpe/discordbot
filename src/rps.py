from main import client
import random

# Play the classic game of Rock, Paper, Scissors

def convert(s):
    if s == 'r' or 'rock' or 'R' or 'Rock':
        return 'Rock'
    elif s == 'p' or 'paper' or 'P' or 'Paper':
        return 'Paper'
    elif s == 's' or 'scissors' or 'S' or 'Scissors':
        return 'Scissors'
    elif s == 'q' or 'quit' or 'Q' or 'Quit':
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
        
@client.event
async def on_message(self, message):
    if message.author == self.client.user:
        return

    if message.content == '!rps':
        player = message.author
        await message.channel.send("Let's play rock paper scissors.  The computer will randomly pick an option.", '\n')
        game = RockPaperScissors()

        while True:
            
            com = random.choice(['Rock', 'Paper', 'Scissors'])
            
            if message.author != player:
                continue
            
            i = message.content.game.convert(i)

            if i == 'q':
                await message.channel.send('Thanks for playing!')
                break
            elif i == 'e':
                await message.channel.send('Not valid option!  Please enter r/R/rock/Rock or p/P/paper/Paper or s/S/scissors/Scissors')
                continue

            v = game.verdict(i, com)

            match v:
                case 0:
                    await message.channel.send(f'{i} beats {com} - Player wins!')
                    game.score[0] += 1
                    
                case 1:
                    await message.channel.send(f'{com} beats {i} - Computer wins!')
                    game.score[1] += 1
                    
                case 2:
                    await message.channel.send(f'Both picked {i} - Tie!')
                    game.score[2] += 1    
            
            await message.channel.send(f'Player won {game.score[0]}   Computer won {game.score[1]}   {game.score[2]} Ties', '\n')
            await message.channel.send("Enter your choice: ")
