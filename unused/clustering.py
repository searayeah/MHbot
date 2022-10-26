from googlebase import GoogleBase
import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

SHEET_KEY = os.environ["sheet_key"]
SHEET_POOP = "poops"
IDS_NAMES = {
    406826633: "andrei",
    204679786: "slava",
    113637897: "danya",
    380058716: "vova",
    482015078: "vanya",
}
TOKEN_NAMES_LIST = [
    "type",
    "project_id",
    "private_key_id",
    "private_key",
    "client_email",
    "client_id",
    "auth_uri",
    "token_uri",
    "auth_provider_x509_cert_url",
    "client_x509_cert_url",
]
TOKEN = {item: os.environ[item].replace("\\n", "\n") for item in TOKEN_NAMES_LIST}


base = GoogleBase(TOKEN, SHEET_KEY, SHEET_POOP, IDS_NAMES.values())

X = base.get_values("slava")

from string import punctuation
from pymystem3 import Mystem

punctuation_chars = set(punctuation)
mystem_analyzer = Mystem(entire_input=False)


def MyTokenizer(sentence):
    tokens = mystem_analyzer.lemmatize(sentence.lower())
    tokens = [x for x in tokens if (len(set(x) & punctuation_chars) == 0)]
    # return ' '.join(tokens)
    return list(set(tokens))


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(tokenizer=MyTokenizer, ngram_range=(1, 2))
X = vectorizer.fit_transform(X)

from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import numpy as np

# clustering = DBSCAN(eps=3, min_samples=2).fit(X)
# print(np.unique(clustering.labels_))

kmeans = KMeans(n_clusters=80).fit(X)

import pandas as pd

X = base.get_values("slava")
dataframe = pd.DataFrame({"text": X, "class": kmeans.labels_})
dataframe.sort_values(by="class", inplace=True)

dataframe.to_csv("test.csv")
