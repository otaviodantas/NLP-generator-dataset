import os
import re
import string
from typing import List

from dotenv import load_dotenv
from unidecode import unidecode
load_dotenv("stopwords.env")

NO_URL = re.compile(r"https?://\S+|www\.\S+|https+|tco?")
NO_USER = re.compile(r"@\w+: |@\w+|@\w+ ")
NO_EMOJI = re.compile(
    "["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002500-\U00002BEF"  # chinese char
    u"\U00002702-\U000027B0"
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"
    u"\u2640-\u2642"
    u"\u2600-\u2B55"
    u"\u200d"
    u"\u23cf"
    u"\u23e9"
    u"\u231a"
    u"\ufe0f"  # dingbats
    u"\u3030"
    "]+",
    flags=re.UNICODE,
)
NO_HASHTAG = re.compile(r"#\w+")
NO_STOPWORDS = re.compile(r"{}".format(os.getenv("STOPWORD")))

def TwitterDataCleaner(data: str):
    # cleaned_data = processing_data(data)
    cleaned_data = remove_stopwords(data)
    cleaned_data = remove_user(cleaned_data)
    cleaned_data = remove_URL(cleaned_data)
    cleaned_data = remove_emoji(cleaned_data)
    cleaned_data = remove_hashtag(cleaned_data)
    cleaned_data = remove_punct(cleaned_data)
    return cleaned_data

def processing_data(data: str):
    return unidecode(data.lower())

def remove_stopwords(data: str) -> str:
    return NO_STOPWORDS.sub(r"", data)

def remove_user(data: str) -> str:
    return NO_USER.sub(r"", str(data))

def remove_URL(data: str) -> str:
    return NO_URL.sub(r"", data)

def remove_emoji(data: str) -> str:
    return NO_EMOJI.sub(r"", str(data))

def remove_punct(data: str) -> str:
    table = str.maketrans("", "", string.punctuation)
    data_without_punct = data.translate(table)
    return data_without_punct

def remove_hashtag(data: str) -> str:
    return NO_HASHTAG.sub(r"", str(data))
