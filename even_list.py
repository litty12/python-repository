'''
Author:litty
date:22-11-2024
'''
list1=[34,25,12,2,26,76]
list2=[98,76,45,24,12,16]
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)

    else:
         odd_list.append(i)

    even_list.sort()
    odd_list.sort()
list4=even_list+odd_list
print(list4)
