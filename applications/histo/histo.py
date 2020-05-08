import sys
import operator
sys.path.append('../word_count')
from word_count import word_count

def histo(cache={}):
    with open('robin.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = word_count(line)
            for word in words.items():
                if word[0] in cache:
                    cache[word[0]] += '#'
                else:
                    cache[word[0]] = '#'
    
    items = list(cache.items())
    items = sorted(items, key=operator.itemgetter(0))
    items = sorted(items, key=operator.itemgetter(1), reverse=True)

    for item in items:
        print(f'{item[0].ljust(20)} {item[1]}')
        # print(item[0] + '\t\t' + "#" * item[1])

histo()