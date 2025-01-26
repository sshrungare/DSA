"""
@Author : Swapnil Shrungare
@goal : 1) Accept list of integers 1 to 30:L 
        2) Accept number bteween 40 anf 60 number : N 
        3) Find out and print all pairs in the list greater than N    
"""

import sys 

L = []

while True: 
    ans = int(input("Do you want to add number to list ? [0/1] : "))
    if ans != 1 :
        break
    num = int(input("Enter number between 1 to 30:"))
    if num <= 0 >=30:
         print("Enter number within 1 - 30 ")
    else:
        L.append(num)


N = int(input("Enter Sum Pairs : "))

P = []

i = 0 

while i < len(L):
    j = i + 1
    while j < len(L):
        if(L[i] + L[j]) > N:
            P.append((L[i] , L[j]))
        j = j + 1             
    i += 1                 

print(P)