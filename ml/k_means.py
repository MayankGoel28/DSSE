import json
import pickle
import os
import numpy as np
# from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

# ps = PorterStemmer()
vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')

def get_X_from_corpus(corpus=None):
    # sentences = []
    # for sentence in corpus:
    #     temp = ""
    #     for word in sentence.split():
    #         temp += ps.stem(word) + " "
    #     sentences.append(temp)

    X = vectorizer.fit_transform(corpus)
    return X

def get_best_model(X=None, min_val=2, max_val=20, draw=False, show_top_labels=False):
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

    if show_top_labels:
        print(f"The {best_k}th is the best cluster size")
        print("Top terms per cluster:")
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        for k in range(best_k):
            print(f"Cluster {k+1}:", end=" ")
            for i in order_centroids[k, :10]:
                print(terms[i], end=" ")
            print()

    result = []
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()    
    for k in range(best_k):
        temp = []
        for i in order_centroids[k, :10]:
            # print(terms[i], end=" ")
            temp.append(terms[i])
        # print()
        result.append(temp)
    return best_model, best_k, result

if __name__ == "__main__":
    hierarchy = {
        'books': [
            'biographies',
            'children',
            'entertainment',
            'fiction',
            'history',
            'money',
            'psychology',
            'religion',
        ],
        'electronics': [
            'accessories',
            'automobiles',
            'cameras',
            'computers',
            'drones',
            'surveillance',
            'video',
        ],
        'food': [
            'baking',
            'candy',
            'coffee',
            'condiments',
            'fresh',
            'frozen',
            'meals',
            'snacks',
        ],
        'home': [
            'appliances',
            'bath',
            'college',
            'decor',
            'furniture',
            'kids',
            'kitchen',
            'matteresses',
        ],
        'movies': [
            'animated',
            'comedy',
            'drama',
            'horror',
            'kids',
            'romance',
            'science',
        ],
        'music': [
            'kids',
            'nineties',
            'reggage',
        ],
        'personal-care': [
            'body',
            'dental',
            'deodrants',
            'hand',
            'mouthwash',
            'razors',
            'toothpaste',
        ],
        
    }

    # os.chdir('.')
    # with os.scandir('.') as dirs:
    #     for entry in dirs:
    #         print(entry)

    for x in hierarchy.keys():
        for y in hierarchy[x]:
            ### LOAD INPUT HERE
            f = open(f"./indexed/{x}_jsons/{x}_{y}.txt", 'r').read()
            corpus = eval(f)
            ### DONE LOADING THE CLEANED INPUT

            X = get_X_from_corpus(corpus)
            model, z, search = get_best_model(X)
            
            # x is category
            # y is sub-category
            # z is k size selected
            pickle.dump(model, open(f'./models/{x}_{y}.model', 'wb'))
            pickle.dump(vectorizer, open(f'./models/{x}_{y}.vectorizer', 'wb'))
            with open(f'./models/{x}_{y}.search_indexing', 'w') as f:
                json_str = json.dumps(search, indent=4)
                f.write(json_str)
            break
        break
        