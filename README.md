# Domain-Specific Search Engine
**DSSE**, pronounced *dɐs'ɪ*, is a comprehensive implementation of the entire stack required for Search Engines. DSSE uses Term Frequency–Inverse Document Frequency to predict cluster levels, and works on the concept of a knowledge base, creating an ontology for the domain-specific data that exists. DSSE is implemented on all layers, from a web crawler, to indexing (including a refinement using the above mentioned clustering algorithm) and a web application with a chatbot interface for queries.

The domain for this Implementation is Walmart, a hugely popular e-commerce website.

## Table of Contents
- [About](#About)
    - [Our Idea](#Our-Idea)
    - [Web Crawling](#Web-Crawling)
    - [Indexing](#Indexing)
    - [Clustering](#Clustering)
    - [Search Engine](#Search-Engine)
- [Members](#Members)
- [Basic Working Version](#Basic-Working-Version)

## About

### Idea
Walmart expects customers from all over the world. It needs a product search engine that can cater to a lot of people from diverse background and culture, which in turn requires the search engine to be **simple and user-friendly**. And this is exactly what we have attempted to achieve.

Our aim, thus, was not only to manage a **sophisticated** enough model that produces relevant result on search queries, but also maintain a UI that ensures maximal convenience and satisfaction for the user.

And well, here is the result!

<img src="https://cdn.discordapp.com/attachments/766879223897653272/767426472628846623/unknown.png">

As you can see, we have implemented a **search assistant** associated with the the search service that effectively enables the user to pass his queries in plain ol' English.

Why is this important?
- Provide Instant Support With The Right Context
- 98% of your visitors will leave without converting if you don't engage them proactively on your website
- Save Time Answering FAQs With Automation

<img src="https://cdn.discordapp.com/attachments/766879223897653272/767414774420996156/unknown.png">


### Web-Crawling
We crawled through about 2k pages - to get 20k objects, This was done through parcel, in Python. All the lists came from a top category and a sub-category.

### Indexing
We indexed all the crawled objects using their links, and the categories they belonged to, in an hierarchical structure, using a Knowledge Base. The data was cleaned, and the categorical similarity was expressed using the "related tags" information we scraped.

### Clustering
We start with the numerical statistic, the TF-IDF, commonly used in Information Retrieval tasks in NLP. This numeric effectively converts the unique tags of a product, and creates a singular data-point per product for the next algorithm.

Now, we use the K-means algorithm from the scikit-learn library to efficiently cluster the similar products. Since this is an Unsupervised Machine Learning Algorithm, it becomes tricky to evaluate the models. However, using the elbow method, we were able to find the best 'K', the cluster size, for each and every domain; be it movies or books or personal-care items. We compared this with K-modes algorithm, which did not yield better results. Thus, we went with a more robust approach using TF-IDF and K-Means algorithm.

### Searching
The Search Engine works on a Semantic Similarity Model, weighted with a modified ratings score (the one IMDB uses for their ranking), which is sped up by a hierarchical knowledge base model, made using the categories and subcategories used when web-crawling.

*PsuedoCode:*

```
    assume a weighted knowledge tree
    
    go through the hierarchy:
        for each hierarchy:
            find the node semantically the closest:
    at lowest hierarchy:
        find the semantically closest object 
        and weight it with the rating (after normalization)
```
The queries are recieved via a bot which usues Google Cloud's DiagnolFlow API to extract intent from the sentence and then converts the sentence to a query
which is further executed. The main focus of using of the bot was to provide an user friendly way to do queries.
Apart from this, when using a search engine, we use a semantic similarity based on Stanford's WordNet to fetch the index to search the key from.

        
    
## Members
Original contributors to the project were Vishva Saravanan, Mayank Goel, Tanishq Chowdhary and Kunwar Shaanjeet Singh Grover.

## Basic Working Version

<img src="https://cdn.discordapp.com/attachments/766879223897653272/767424781817085992/unknown.png">
