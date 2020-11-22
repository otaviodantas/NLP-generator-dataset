import os
from dotenv import load_dotenv

from auth import create_api
from stream import calling_stream
from stopword import SettStopwords

load_dotenv("wordkey.env")

if __name__ == "__main__":
    SettStopwords(os.getenv("WORDKEY"))
    calling_stream(create_api())
