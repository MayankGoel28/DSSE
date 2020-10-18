# UTILITY
import numpy as np
import pickle
import json

# NLP
from nltk.stem import PorterStemmer

ps = PorterStemmer()

# ML
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(analyzer="word", stop_words="english")


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def get_predictions(user_input, category, sub_category):
    """
    inputs:
        user_input:
            is a string of intents of the user,
            with sorted (internal requirement) intents, spaced with whitespace.
        category:
            the larger class
        sub_category:
            the specific of the above
    """

    model = pickle.load(open(f"ml/models/{category}_{sub_category}.model", "rb"))
    vectorizer = pickle.load(open(f"ml/models/{category}_{sub_category}.vectorizer", "rb"))
    terms_indexed = json.load(open(f"ml/models/{category}_{sub_category}.search_indexing", "rb"))

    cleaned_input = ""
    for word in sorted(user_input.lower().split()):
        cleaned_input += word + " "

    Y = vectorizer.transform([cleaned_input])
    prediction = model.predict(Y)[0] + 1
    # print(prediction)

    scores = []
    for center in model.cluster_centers_:
        scores.append(-np.linalg.norm(center - Y))

    # for score in sorted(softmax(scores), reverse=True):
    #     print(f"{round(score*100, 2)}%")
    # sorted(softmax(scores), reverse=True)
    return prediction, terms_indexed[prediction]


if __name__ == "__main__":
    cluster_number, terms_indexed = get_predictions("Hello", "books", "biographies")
    print(cluster_number)
    print(terms_indexed)
