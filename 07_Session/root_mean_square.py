"""
@author: swapnil Shrungare 
@goal : 1) Acdcept list of  integers from end user :
        2) Print list numbers index wise 
        3) Calculate RMS
        4) Print RMS
"""

import sys

L = []

while True:
    ans = int(input("Do you want to enter more numvber : 1/0 "))
    if ans != 1:
        break
    num = int(input("Enter a number : "))
    L.append(num)

if len(L) > 0:
    i = 0 
    while(i < len(L)):
        print(1,L[i],sep= " : ")
        i = i + 1
    
    rms = (sum( x ** 2 for x in L ) / len(L)) ** 0.5 
    print(f"rms is {rms:.02f}")
else:
    print("List can not be empty")
    sys.exit()

