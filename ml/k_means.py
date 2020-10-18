import json
import pickle
import numpy as np
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from clean_electronics import tags_list as corpus

ps = PorterStemmer()
sentences = []
for sentence in corpus:
    temp = ""
    for word in sentence.split():
        temp += ps.stem(word) + " "
    sentences.append(temp)

vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
X = vectorizer.fit_transform(sentences)
# print(X.shape)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def get_best_model(min_val, max_val, draw=True, show_top_labels=True):
    K = range(min_val, max_val+1)
    
    costs = []
    min_cost = float('inf')
    best_model = None
    for k in K:
        # NOTE: CAN MAKE THE INIT HERE AS init=np.array(...)
        # "If an ndarray is passed, it should be of shape (n_clusters, n_features) and gives the initial centers.""
        model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
        cost = model.fit(X).inertia_
        costs.append(cost)

        if cost < min_cost:
            best_model = model

    if draw:
        plt.figure(figsize=(16,8))
        plt.plot(K, costs, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Cost')
        plt.title('The Elbow Method showing the optimal k')
        plt.show()

    best_k = costs.index(sorted(costs)[0]) + min_val
    print(f"The {best_k}th is the best cluster size")

    if show_top_labels:
        print("Top terms per cluster:")
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        for k in range(best_k):
            print(f"Cluster {k+1}:", end=" ")
            for i in order_centroids[k, :10]:
                print(terms[i], end=" ")
            print()

    return best_model

def get_predictions(model=None):
    user_input = input("Enter the Query: ").strip()
    cleaned_input = ""
    for word in sorted(user_input.lower().split()):
        cleaned_input += ps.stem(word) + " "

    Y = vectorizer.transform([cleaned_input])
    prediction = model.predict(Y)[0]+1
    print(prediction)

    scores = []
    for center in model.cluster_centers_:
        scores.append(-np.linalg.norm(center-Y))
    
    for score in sorted(softmax(scores), reverse=True):
        print(f"{round(score*100, 2)}%")

if __name__ == "__main__":
    k_min_val = 2
    k_max_val = 20
    model = get_best_model(k_min_val, k_max_val, draw=True)
    pickle.dump(model, open('electronics.model', 'wb'))

    pickle.load(open('electronics.model', 'rb'))
    get_predictions(model)
