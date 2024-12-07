sentence=input("enter the sentence: ")
word=sentence.split(" ")
occdict=dict()

for i in word:
	if i in occdict:
		occdict[i]=occdict[i]+1
	else:
		occdict[i]=1
print(occdict)

