def word_count(s):
    # Implement me.
    cache={}
    if len(s) == 0:
        return {}
    count = 0
    s = s.lower().replace(',', '').replace(',', '').replace('.', '').replace('"', '').strip('":;,.-+=/\\|[]{}()*^&').replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    for word in s.split(' '):
        # print(f"{count}: {word.lower().replace(',', '').replace(',', '').replace('.', '')}")
        
        if word in cache:
            cache[word.lower().replace(',', '').replace(',', '').replace('.', '')] += 1
        elif len(word) == 0:
            continue
        else:
            cache[word] = 1
        count += 1
    # print(cache)
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))