word='dictionary'
secret_word=list(word)
new_word=['*'for i in range(len(secret_word))]
penalty=0
letters_used=[]
while '*' in new_word and penalty < 7:
    guess=input('Enter any letter, No capital letters \n')
    print(guess)
    if guess not in secret_word or guess in letters_used:
        penalty+=1
    else:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                new_word[i]=secret_word[i]
    letters_used.append(guess)
    print('Penalty', penalty)
    print(letters_used)
    print(new_word)
print('Thanks For Playing :)')
exit()