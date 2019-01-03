#Indra Ratna
#CS-UY 1114
#2 Nov 2018
#Lab 9
#Problem 5

def k_shift(lst,k):
    return lst[k:]+lst[:k]

def k_shift_inplace(lst,k):
    for i in (len(lst)):
        temp = lst[i]
        lst.insert(i,lst.pop(i+k))
    
myList = [1,2,3,4,5] 
print(k_shift(myList,2))

