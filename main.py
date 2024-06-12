from art import logo, vs
from game_data import data
import random
from replit import clear

def contender():
    return random.choice(data)

def compare(a, b, answer):
    follow_a = a['follower_count']
    follow_b = b['follower_count']
    if follow_a > follow_b:
        return answer == 'a'
    else:
        return answer == 'b'

def game():
    a = contender()
    play_again = True
    score = 0
    print(logo)
    while play_again:
        b = contender()
        while a == b:
            b = contender()
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if compare(a,b, answer):
            a = b
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            play_again = False
            print(f"Sorry, that's wrong. Final score: {score}")
game()   









#print arts
#create compare a and b
#import the compare data
#make the comparison
#replace a for b
#call a new comparator
#count points
#end if wrong