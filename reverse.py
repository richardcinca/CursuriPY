
word=input("type your word:  ")
length=len(word)
reversedWord=""
for i in range(length-1,-1,-1):
   reversedWord=reversedWord+word[i]
print("Your reversed word is: {}".format(reversedWord))