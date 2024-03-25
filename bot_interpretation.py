from cohere_utils import query
from draw import get_reading

def bot_interpret(question,spread,cards):
    cards_format = "\n".join(f"{i}. {cards[i-1].title}" for i in range(1,spread+1))
    prompt = f"I have requested a Tarot card reading. The question that I want answered is:\n{question}\nThe cards I have drawn are:\n{cards_format}\nWhat does this mean?"
    return query(prompt)

if __name__=='__main__':
    question, spread, cards = get_reading()
    print(bot_interpret(question,spread,cards))