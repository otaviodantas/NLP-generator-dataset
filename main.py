import os
from dotenv import load_dotenv

from auth import create_api
from call_stream import calling_stream

load_dotenv('config.env')

if __name__ == "__main__":
    wordkey = os.getenv("WORDKEY")
    calling_stream(wordkey, create_api())
