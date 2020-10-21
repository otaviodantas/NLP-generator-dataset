import os
from dotenv import load_dotenv

from call_stream import calling_stream
from auth import create_api

load_dotenv("wordkey.env")

if __name__ == "__main__":
    wordkey = os.getenv("WORDKEY")
    calling_stream(wordkey, create_api())
