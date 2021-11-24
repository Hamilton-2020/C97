intro= input("Enter your introduction:- ")
characters= 0
words= 1

for i in intro: 
    characters=characters+1
    
    if(i==" "): 
        words=words+1

        
print (characters)
print (words)