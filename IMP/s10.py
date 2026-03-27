list=[1,2,3,2,3,4]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)