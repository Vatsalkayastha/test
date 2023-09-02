import openai
from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    openai_key = os.getenv('OPENAI_API_KEY')
    serpapi_key = os.getenv('SERPAPI_KEY')
    
    @staticmethod
    def get_openai_key():
        return Config.openai_key
    
    @staticmethod
    def get_serpapi_key():
        return Config.serpapi_key


