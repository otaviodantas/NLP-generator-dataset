import re
import string
from typing import List

from unidecode import unidecode

from aux_mod import TokenData


class TwitterDataCleaner:
    def __init__(self, list_stopword: List[str]):
        self.stopword = list_stopword

    def clean(self, data: str):
        cleaned_data = self.__remove_stopwords(data)
        cleaned_data = self.__remove_user(cleaned_data)
        cleaned_data = self.__remove_URL(cleaned_data)
        cleaned_data = self.__remove_emoji(cleaned_data)
        cleaned_data = self.__remove_hashtag(cleaned_data)
        cleaned_data = self.__remove_punct(cleaned_data)
        return cleaned_data

    def __remove_stopwords(self, data: str) -> str:
        list_clean_data: List[str] = []
        list_separete_sentence: List[str] = TokenData(data)

        for word in list_separete_sentence:
            not_accent = unidecode(word)
            if not_accent not in self.stopword:
                list_clean_data.append(word)

        phrase_complete = " ".join(list_clean_data)
        return phrase_complete

    def __remove_user(self, data: str) -> str:
        pattern = re.compile(r"@\w+: |@\w+|@\w+ ")
        data_without_user = pattern.sub(r"", str(data))
        return data_without_user

    def __remove_URL(self, data: str) -> str:
        url = re.compile(r"https?://\S+|www\.\S+|https+|tco?")
        data_without_url = url.sub(r"", data)
        return data_without_url

    def __remove_emoji(self, data: str) -> str:
        emoji_pattern = re.compile(
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

        data_without_emoji = emoji_pattern.sub(r"", str(data))
        return data_without_emoji

    def __remove_punct(self, data: str) -> str:
        table = str.maketrans("", "", string.punctuation)
        data_without_punct = data.translate(table)
        return data_without_punct

    def __remove_hashtag(self, data: str) -> str:
        pattern = re.compile(r"#\w+")
        data_without_hashtag = pattern.sub(r"", str(data))
        return data_without_hashtag
