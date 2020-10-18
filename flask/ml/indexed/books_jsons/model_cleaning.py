from pprint import pprint
from collections import Counter
import json
import glob
for filename in glob.glob('*.json'):
    with open(filename,'r') as file:
        f = file.read()
        data = eval(f)
        clean_data = []
        for eachobj in data:
            temp = []
            words = [name[0] for name in eachobj['tags']]
            taglist = [word for wordlist in words for word in wordlist.split()]
            tagcount = Counter(taglist)
            tags = [tag for tag in tagcount]
            tagsstring = " ".join(tags)
            temp = tagsstring
            clean_data.append(temp)
    outfile = open(f'{filename[:-5]}.txt','w')
    outfile.write(str(clean_data))
if __name__=="__main__":
    pprint(clean_data)