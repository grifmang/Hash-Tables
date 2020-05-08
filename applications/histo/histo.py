import sys
sys.path.append('../word_count')
from word_count import word_count

def histo(cache={}):
    with open('robin.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = word_count(line)
            for word in words.items():
                if word[0] in cache:
                    cache[word[0]] += 1
                else:
                    cache[word[0]] = 1
    
    items = list(cache.items())
    items.sort(key=lambda e: e[1], reverse=True)

    for item in items:
        print(item[0] + ':' + "#" * item[1])

histo()