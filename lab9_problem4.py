#Indra Ratna
#CS-UY 1114
#2 Nov 2018
#Lab 9
#Problem 4

def mycount(lst,n):
    count=0
    for element in lst:
        if(element == n):
            count+=1
    return count
print(mycount([7,2,1,3,7,9],7))
