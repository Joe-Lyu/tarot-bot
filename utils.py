from cohere_utils import query
from draw import get_reading
import re
def bot_interpret(question,spread,cards):
    cards_format = "\n".join(f"{i}. {cards[i-1].title}" for i in range(1,spread+1))
    prompt = f"I have requested a Tarot card reading. The question that I want answered is:\n{question}\nThe cards I have drawn are:\n{cards_format}\nWhat does this mean?"
    return query(prompt)

def split_msg(msg, limit=2000):
    if len(msg) <= limit:
        return [msg]
    else:
        sentence_endings = re.compile(r'[.!?]+')
        chunks = sentence_endings.split(msg)
        result = []
        current_chunk = ''
        for i, chunk in enumerate(chunks):
            if i != 0:
                current_chunk += chunk
            if len(current_chunk) > limit:
                result.append(current_chunk[:limit-1] + '...')
                current_chunk = current_chunk[limit-1:]
        if current_chunk:
            result.append(current_chunk)
        for i in range(1,len(result)):
            result[i] = '...' + result[i]
        return result


if __name__=='__main__':
    question, spread, cards = get_reading()
    print(bot_interpret(question,spread,cards))