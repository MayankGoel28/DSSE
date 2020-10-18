from pprint import pprint
from collections import Counter

file = open('electronics.json', 'r')
f = file.read()
data = eval(f)
clean_data = []
smoothing = 30
tot, num = 0, 0
for eachobj in data:
    tot += float(eachobj['stars'])
    num += 1
avg = tot/num
for eachobj in data:
    temp = {}
    temp['title'] = eachobj['title']
    words = [name[0] for name in eachobj['tags']]
    taglist = [word for wordlist in words for word in wordlist.split()]
    tagcount = Counter(taglist)
    tags = [tag for tag in tagcount]
    tagsstring = " ".join(tags)
    temp['tags'] = tagsstring
    stars = float(eachobj['stars'])
    ratings = int(eachobj['ratings'])
    temp['relevancy_score'] = (
        (stars*ratings)+(avg*ratings)/(ratings+smoothing))
    clean_data.append(temp)
if __name__ == "__main__":
    pprint(clean_data)
