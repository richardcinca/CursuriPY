iterator=0
reversed_word=""

word = input("Insert word: ")
print("Your word is '{}'".format(word))
length=len(word)
print("The length of the word is {} letters".format(length))

for var in word:
    #print("Var is {}".format(var))
    #print(word[iterator])
    #iterator+=1
    #reversed_word=var+reversed_word
    #print(reversed_word)
    #print("......")
    print("{} must be equal to {}".format(word[iterator],var))
    iterator = iterator+1
    reversed_word=var+reversed_word
    
print("Reversed word is:{}".format(reversed_word))

input("\n\n P <enter> to exit.")