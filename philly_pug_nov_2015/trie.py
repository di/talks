from collections import defaultdict

infinitedict = lambda: defaultdict(infinitedict)
trie = infinitedict()

trie['b']['a']['r'] = True

def is_word(trie, word):
    return reduce(
       lambda trie, letter: trie.get(letter) if trie else False,
       word,
       trie
    ) == True

print bool(trie['b']['a']['r'])
print bool(trie['f']['o']['o'])
