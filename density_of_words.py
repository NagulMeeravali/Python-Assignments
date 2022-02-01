
file=open("Python_Practice/Data.txt","r")
fr=1

data=file.read()
words=data.lower().split(" ")
twords=len(words)
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i]==words[j]:
            fr=fr+1
            words[j]=None
    if words[i]!=None:
        print(words[i]," : ",(fr/twords)*100)
    fr=1
            
    
    