#Indra Ratna
#CS-UY 1114
#2 Nov 2018
#Lab 9
#Problem 7

def count_and_print_digits(val):
    count = [0,0,0,0,0,0,0,0,0,0]
    value = val
    while(value>0):
        for index in range(10):
            digit = value%10
            if(index==digit):
                count[index]+=1
        value //=10
    return count
print(count_and_print_digits(123))
