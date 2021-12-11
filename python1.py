
#string concatination
# ytuber = "prateek"
# print("Subscribe to " + ytuber)
# print("Subscribe to {}".format(ytuber))
# print(f"Subscribe yo {ytuber}")
#basic project1 : madlib
# name = input("your name: ")
# username= input("username: ")

# madlib = f"Hello {name},\nfrom now your name is {username}"
# print(madlib)
# project: Guess the number 
import random
# def guess(x):
#     random_n = random.randint(1,x)
#     guess = 0
#     while guess != random_n :
#         guess = int(input(f'guess the number between 1 and {x}: '))
#         if guess < random_n:
#             print('lower value entered')
#         elif guess > random_n :
#             print('higher value entered')

#     print(f'got it :{random_n}')

# def comp_guess(x):
#     low = 1
#     high = x
#     feedb = ''
#     while feedb != 'c':
#         guess = random.randint(low, high)
#         feedb = input(f'Is {guess} high, low, or correct').lower()
#         if feedb == ' ':
#             print('please input')
#         elif feedb == 'h':
#             high = guess-1
#         elif feedb == 'l':
#             low = guess+1   
#     print('computer got your number')             
# comp_guess(7)                
#Rock, Paper, Scissor
# def play():
#     user = input("'r' for Rock, 'p' for paper, 's' for scissor   " ).lower()
#     computer = random.choice(['r','p','s'])

#     if  user == computer:
#         return 'Tie'

#     if win(user, computer):
#         return 'Won'

#     return 'Lose'

# def win(first, second):
#     if (first =='r' and second == 's') or (first =='p' and second == 'r') \
#         or (first =='s' and second == 'p'):
#          return True 

# print(play())

#hangman game start
words = ['abc','def','ghi','jkl','mno']
wrds =set(words)
word = random.choice(words)

# lives = 5
def guess_word():
    i = 0
    lives =5
    guesses = set()
    while i == 0 and lives > 0:
        guess = str(input('Enter word: '))
        if guess == word:
            print('you got the word')
            i = 1
        else:
            if guess in guesses:
                print('already typed') 
                lives = lives -1       
            else:
                print('wrong guess: ')
                guesses.add(guess) 
                lives = lives -1
    if lives == 0:
        print(f'you lost, the word was {word}')
guess_word()
