#Indra Ratna
#CS-UY 1114
#2 Nov 2018
#Lab 9
#Problem 3

def powers_of_two_lst(n):
    powers = []
    for power in range (1,n+1):
        powers.append(2**(power))
    return powers



print(powers_of_two_lst(5))




