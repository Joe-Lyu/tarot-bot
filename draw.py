from deck import *
import random
import time

def draw_spread(spread):
    cards = random.sample(DECK,spread)
    return cards

def get_reading():
    question = input("What would you like to know?\n")
    spread = eval(input("Choose the number of cards in your spread\n"))

    cards = draw_spread(spread)
    print("Cards drawn.")
    print(f"Your question: {question}")
    for i in range(1,spread+1):
        print(f"{i}. {cards[i-1].title}")
    print('-'*20)

    return question, spread, cards
        
if __name__ == '__main__':

    question, spread, cards = get_reading()
    
    print("Cards drawn.")
    while True:
        num = input("Which card would you like to know about?\n")
        if int(num) in range(1,spread+1):
            print(cards[int(num)-1])
            print('-'*20)
            time.sleep(1)
        else:
            print("Invalid input.")

