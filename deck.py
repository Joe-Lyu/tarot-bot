class TarotCard():
    def __init__(self,description,name,number=None):
        self.description = description
        self.name = name
        self.number = number
        if number is None:
            self.title = name
        else:
            self.title = number + " of " + name
        
    def __repr__(self):
        return '---\n' + self.title + '\n' + self.description
    
numbers = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Page','Knight','Queen','King']

minor_arcana = {'Cups':"Emotions, relationships, and creativity.",
         'Pentacles':" Material aspects, finances, and the physical world.",
         'Swords':"Intellect, challenges, and communication.",
         'Wands':"Action, passion, and spiritual growth."
}
major_arcana = {
    "The Fool": "Represents new beginnings, spontaneity, and a leap of faith.",
    "The Magician": "Represents self-discovery, manifestation, and personal power.",
    "The High Priestess": "Represents intuition, spiritual connection, and inner wisdom.",
    "The Empress": "Represents nurturing, abundance, and motherhood.",
    "The Emperor": "Represents structure, discipline, and authority.",
    "The Lovers": "Represents love, relationships, and choices.",
    "The Chariot": "Represents willpower, control, and the manifestation of personal desires.",
    "Strength": "Represents resilience, endurance, and inner strength.",
    "The Hermit": "Represents introspection, solitude, and spiritual awakening.",
    "The Wheel of Fortune": "Represents change, cycles, and the law of karma.",
    "Justice": "Represents balance, fairness, and the pursuit of righteousness.",
    "The Hanged Man": "Represents sacrifice, letting go, and emotional release.",
    "Death": "Represents transformation, mortality, and the end of cycles.",
    "Temperance": "Represents balance, harmony, and the art of moderation.",
    "The Devil": "Represents temptation, personal deception, and the shadow self.",
    "The Tower": "Represents shock, trauma, and the disruption of personal and emotional structures.",
    "The Star": "Represents hope, guidance, and the divine spark within each person.",
    "The Moon": "Represents intuition, emotions, and the cyclical nature of life.",
    "The Sun": "Represents awakening, enlightenment, and personal growth.",
    "Judgement": "Represents self-evaluation, inner criticism, and the need for personal change.",
    "The World": "Represents completion, fulfillment, and the integration of personal and universal themes.",
}

DECK = []
for name in major_arcana:
    card = TarotCard(major_arcana[name],name)
    DECK.append(card)
for suit in minor_arcana:
    for number in numbers:
        card = TarotCard(minor_arcana[suit],suit,number)
        DECK.append(card)

if __name__ == '__main__':
    for card in DECK:
        print(card)