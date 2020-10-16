from nltk import tokenize
from string import punctuation
from typing import List
import nltk
import csv

nltk.download("stopwords")


def TokenData(data: str) -> List[str]:
    token_space = tokenize.WhitespaceTokenizer()
    all_words_token = token_space.tokenize(data)
    return all_words_token


def SettStopwords(wordkey: str) -> List[str]:
    icomun_stopword = [
        "rt",
        "RT",
        "q",
        str(wordkey).capitalize(),
        str(wordkey).lower(),
        str(wordkey).upper(),
    ]
    stopwords = nltk.corpus.stopwords.words("portuguese")
    all_stopword = icomun_stopword + stopwords + SettPontuation()
    return all_stopword


def SettPontuation() -> List[str]:
    all_pontuation: List[str] = []

    for list_pontuation in punctuation:
        all_pontuation.append(list_pontuation)

    return all_pontuation


def TransformToCSV(data: str) -> None:
    with open("dataset.csv", mode="a+", newline="") as file:
        writer = csv.writer(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow([data])
