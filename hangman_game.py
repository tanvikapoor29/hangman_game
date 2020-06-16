word="Delhi"
word=list(word)
gword="_"*len(word)
gword=list(gword)
count=0
ip=input("Enter the letter " )
while True:
    if ip.upper() in word:
        index=word.index(ip.upper())
        gword[index]=ip.upper()
        print(''.join(gword))
        word[index]="_"
    if '_' not in gword:
        print("you have won the match")
        break
    else:
        ip=input("Enter the letter that you have guessed " )
        count=count+1
        if count>2.5*len(word):
            print("you are out of chances, try again")
            
