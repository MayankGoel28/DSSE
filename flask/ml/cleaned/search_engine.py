#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


# In[2]:


def best_file(keyword):
    top = os.getcwd()
    dir_names = []
    for subdir, dirs, files in os.walk(r"./ml/cleaned/"):
        for diry in dirs:
            dir_names.append(diry)
    dir_names = dir_names[1:]
    synkey = wn.synsets(keyword)[0]
    most_similar_score = 0
    for name in dir_names:
        try:
            synname = wn.synsets(name)[0]
            x = synkey.path_similarity(synname)
            if x > most_similar_score:
                most_similar_score = x
                category = name
        except:
            continue
    most_similar_score = 0
    subcats = []
    for subdir, dirs, files in os.walk(r"./ml/cleaned/"):
        for file in files:
            if category in file and file.endswith(".json"):
                subcats.append(file.split("_")[2].split(".")[0])
    print(subcats)
    most_similar_score = 0
    for name in subcats:
        try:
            synname = wn.synsets(name)[0]
            x = synkey.path_similarity(synname)
            if x > most_similar_score:
                most_similar_score = x
                sub_category = name
        except:
            continue

    return (category, sub_category)


# In[3]:


cat, subcat = best_file("dog")


# In[4]:


def best_object(word, cat, subcat):
    stopwordsy = stopwords.words("english")
    file = open(f"./ml/cleaned/{cat}/clean_{cat}_{subcat}.json", "r")
    f = file.read()
    data = eval(f)
    try:
        synkey = wn.synsets(word)[0]
    except:
        print("We can't identify this word.")
    max_sim_score = 0
    max_score = 0
    min_score = data[0]["relevancy_score"]
    for things in data:
        max_score = max(max_score, things["relevancy_score"])
        min_score = min(min_score, things["relevancy_score"])
    for things in data:
        sem_score, totes = 0, 0
        for tag in things["tags"]:
            if tag in stopwordsy or not tag.isalpha():
                continue
            else:
                try:
                    synword = wn.synsets(word)[0]
                    x = synkey.path_similarity(synword)
                    sem_score += x
                    totes += 1
                except:
                    continue
        try:
            avg_score = sem_score / totes
        except:
            continue
        avg_score = avg_score * (things["relevancy_score"] - min_score / max_score)
        if avg_score > max_sim_score:
            buy_this = things
            max_sim_score = avg_score
    return buy_this


# In[5]:


best_object("dog", "toys", "girls")


# In[ ]:
