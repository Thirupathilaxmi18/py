str=input("enter a string:")
i=0
if i == len(str):
    print("".join(str))
for j in range(i,len(str)):
    words=[c for c in str]
    words[i],words[j]=words[j],words[i]
    print(words)
    i+1,j+1
