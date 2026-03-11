# duplicate value ko remove karana.
number=[1,2,3,4,5,1,2,4]
dupli=[]
for i in number:
    if i not in dupli:
        dupli.append(i)
print(dupli)