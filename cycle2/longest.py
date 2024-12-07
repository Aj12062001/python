list = "help, write out, where is, cut justify, go to line".split(", ")
print(list)
length = max([ len(word) for word in list ])
word = ""
for i in range(len(list)):
    if len(list[i]) == length:
        word = list[i]
print(f"The longest word : {word} \nlength: {length}.")
