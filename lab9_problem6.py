#Indra Ratna
#CS-UY 1114
#2 Nov 2018
#Lab 9
#Problem 6

def get_common_elems(lst1,lst2):
    acc=[]
    for element1 in lst1:
        for element2 in lst2:
            if(element1==element2):
                acc.append(element1)
    return acc
print(get_common_elems([5,1,4,3,6],[6,1,8,3]))
