# bot.py
import os
try:
    import discord
    import cohere
except:
    os.system('pip install discord cohere')
import discord
import pickle
from deck import *
from draw import draw_spread
from utils import bot_interpret, split_msg
TOKEN = pickle.load(open('token.pkl','rb')) #not gonna show my token to ya :)

class TarotBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!tarot'):
            def is_question(msg):
                return msg.content.endswith('?') and msg.author == message.author
            
            def is_spread(msg):
                is_num = True
                try:
                    num = int(msg.content)
                except:
                    is_num = False
                return is_num and int(num) in range(1,11) and msg.author == message.author
            await message.reply("What is the question you want answered?")
            question = await self.wait_for('message',check=is_question, timeout=600)
            question = question.content
            await message.reply("How many cards would you like to draw?")
            spread = await self.wait_for('message',check=is_spread, timeout=600)
            spread = int(spread.content)            

            cards = draw_spread(spread)
            await message.channel.send("Cards drawn.")
            await message.reply(f"Your question: {question}\n" + '\n'.join([f"{i}. {cards[i-1].title}" for i in range(1,spread+1)]))

            await message.reply("Would you like an interpretation of these cards?")
            def is_yes(msg):
                return msg.content.lower() in ['yes','no'] and msg.author == message.author
            ans = await self.wait_for('message',check=is_yes, timeout=600)
            if ans.content.lower() == 'yes':
                await message.reply("Interpreting...")
                interpretation = bot_interpret(question,spread,cards)
                print('generation successful.')
                result = split_msg(interpretation)
                for i in result:
                    await message.reply(i)
                return
            else:
                return await message.reply("Exited session.")
        
        if message.content.startswith('!explain'):
            await message.reply("What card would you like to know about?")
            def is_card(msg):
                return msg.content.lower() in [card.title.lower() for card in DECK] and msg.author == message.author

            choice = await self.wait_for('message',check=is_card, timeout=600)
            for card in DECK:
                if card.title.lower() == choice.content.lower():
                    return await message.reply(card.__repr__())



intents = discord.Intents.default()
intents.messages = True

client = TarotBot(intents=intents)
client.run(TOKEN)