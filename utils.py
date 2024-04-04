from cohere_utils import query
from draw import get_reading
def bot_interpret(question,spread,cards):
    cards_format = "\n".join(f"{i}. {cards[i-1].title}" for i in range(1,spread+1))
    prompt = f"I have requested a Tarot card reading. The question that I want answered is:\n{question}\nThe cards I have drawn are:\n{cards_format}\nWhat does this mean?"
    return query(prompt)

def split_msg(msg, limit=1800):
    # Split a message into multiple messages if it exceeds the limit.
    if len(msg) <= limit:
        return [msg]
    else:
        breaks = []
        win_start = 0
        while win_start < len(msg) - limit:
            for i in range(win_start+limit-1, win_start-1, -1):
                if msg[i] in ['.','!','?']:
                    breaks.append(i)
                    win_start = i+1
                    break
        msgs = []
        breaks = [-1] + breaks
        for i in range(1,len(breaks)):
            msgs.append(msg[breaks[i-1]+1:breaks[i]+1])
        msgs.append(msg[win_start:])

        for i in range(len(msgs)):
            msgs[i] = msgs[i].lstrip(' ').rstrip(' ')
        return msgs


if __name__=='__main__':
    question, spread, cards = get_reading()
    print(bot_interpret(question,spread,cards))