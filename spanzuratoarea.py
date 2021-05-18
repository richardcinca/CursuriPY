# input word
word=list(input('word>> '))
secret_word=[]

lives=int(7)
visible_letters=[word[0],word[-1]]

for i in range(0,len(word)):
    # print(word[i])
    if word[i] not in visible_letters:
       secret_word.append('_')
    else:
        secret_word.append(word[i])

print(' '.join(secret_word))

guess_list=[]
lives=int(7)

while '_' in secret_word:
    guess = input("Guess >> ")  

    while guess in guess_list or guess in secret_word:
            guess = input("Already have it. Guess again >> ") 

    if lives==0:
        print('game over')
        break
    
    elif guess not in word:
        print(f"wrong. You have {lives} left")
        lives-=1
        print(lives)
    

   
    for i in range(0,len(word)):        

        if  guess == word[i] :
            secret_word[i] = guess
            print(' '.join(secret_word))
            guess_list.append(guess)
            #print(guess_list)

       

        
    
            

        
    

