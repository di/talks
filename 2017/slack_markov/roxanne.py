import markovify

corpus = open('roxanne_lyrics.txt').read()
model = markovify.NewlineText(corpus)
print(model.make_sentence())

output = set()
for _ in range(100):
    sentence = model.make_sentence()
    if sentence:
        output.add(sentence)

for x in output:
    print(x)
