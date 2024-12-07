sentence = "The most fastest thing in the world is the worlds was always the fastest".split(" ")
print(sentence)
word_count = [str(sentence.count(word)) for word in sentence]
dictionary = dict(zip(sentence,word_count))
print(dictionary)
