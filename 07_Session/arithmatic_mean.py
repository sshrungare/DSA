"""
@Author : Swapnil Shrungare
@goal : 1) Accept list of Positive Integers 
        2) Print the numbers in indexwise numbers 
        3) Caculate AM  = SUM[ ]/Len(L)
        4) Print arithmantic mean
"""

L = []

while True:
    ans = int(input("Do you want to enter number [1/0] : "))
    if ans != 1:
        break
    num = int(input("Enter Number : "))
    L.append(num)

if len(L) >  0:
    am = sum(L)/ len(L)
    print(f"AM of list : {am:.02f}")