import os
import nltk
from string import punctuation
from typing import List

nltk.download("stopwords")

def SettStopwords(wordkey: str):
    icomun_stopword = [
        "rt",
        "RT",
        "q",
        str(wordkey).capitalize(),
        str(wordkey).lower(),
        str(wordkey).upper(),
        str(wordkey)
    ]
    stopwords = nltk.corpus.stopwords.words("portuguese")
    all_stopword = icomun_stopword + stopwords + SettPontuation()
    with open("stopwords.env", 'w') as f:
        f.write("STOPWORD={}".format("|".join(all_stopword)))

def SettPontuation() -> List[str]:
    all_pontuation: List[str] = []

    for list_pontuation in punctuation:
        all_pontuation.append(list_pontuation)

    return all_pontuation
