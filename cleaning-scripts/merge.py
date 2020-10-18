import glob
outfilename='electronics.json'
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.json'):
        with open(filename, 'rb') as readfile:
            obj = readfile.read()
            obj = obj[1:-2]
            outfile.write(obj+b',')