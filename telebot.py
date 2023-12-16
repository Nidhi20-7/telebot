from dotenv import load_dotenv
import os
from aiogram import Bot,Dispatcher,types,executor
from aiogram.utils import executor
import openai
import sys

class Reference:
    '''
    class to store previous responses from chatgpt api
    
    '''
    
    def __init__(self) -> None:
        self.response=""
        
        
        
        
        
load_dotenv()
openai.api_key=os.getenv("OpenAI_API_KEY")

reference=Reference()

TOKEN=os.getenv("TOKEN")

MODEL_NAME="gpt-3.5-turbo"

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

def clear_past(): # function to clear previous conversation
    reference.response=""
    
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` or /help command
    """
   
    await message.reply(" Helloo \n Kem cho")
    
@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler receives command to clear
    """
    
    clear_past()
    await message.reply("previous convo deleted")
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """
    This handler receives messages with  /help command
    """
    help_command="""
    Hey there,I am chatgpt bot created by Nidhii ! Follow these commands
    /start- to start conversation
    /clear - to clear past conversation
    /help - to get help menu
    THANK YOU :)
    """
   
    await message.reply(help_command)
    
@dp.message_handler()
async def chatgpt(message: types.Message):
    print(f">>> USER: \n\t")
    
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)