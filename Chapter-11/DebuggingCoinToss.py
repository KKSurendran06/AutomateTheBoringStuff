import random

def setGuess(HT):
    global guess
    if HT == 'heads':
       guess = 1
    else :
       guess = 0    

guess = ''       

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)
setGuess(guess)

if guess == toss:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    setGuess(guess)
    
    if guess == toss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        