"""
Input : non empt6y list of integers
All elements exluding last element is sorted
Write a code so that the entire list is sorted
(in our context it means put the last element in a right position or sorting position and therefore the name of 
file is insert at sorted position )
"""

L = [10,20,30,40,50,60,25]

k = L[len(L)- 1 ]
i = len(L) - 2 
while i >= 0:
    if L[i] > k:
        L[i+1] = L[i]
    else:
        break
    i = i - 1

L[i+1] = k

print(L)

#Entire List 
K = [1,3,4,2]
print(K)
#Get last element 
k = K[len(K) - 1] # i.e = 2
    
#Get last - 1th element index
j = len(K) - 2 #i.e = 3 

while j >= 0: #starting 3 >= 0 
    if K[j] > k:
        K[j + 1] = K[j]
    else:
        break
    j = j - 1
K[j+1] = k
print(K)

import sys

def insert_at_sorting(L:list) -> list:
    if type(L) != list:
        sys.exit()
    k = L[len(L) - 1] # get last element 
    i = len(L) - 2 = # get secondlast elemenets index 
    while i >= 0: # 
        if L[i] > k: # check if 2nd last elemt is greater than K 
            L[i+1] = L[i] # then shift 2nd last to last 
        else: #second last elemet is not greather than last 
            break # break 
        i = i - 1 # set pointer to 3rd last elemenet 
    L[i+1] = k #set loswe

    return L 


L = [1,34,4,5,456,2]
print(L)
new_l = insert_at_sorting(L)
print(new_l)

# repeat 1 
def insert_at_sort_position(L):
    k = L[len(L)- 1] 
    i = len(L) - 2 
    while i >= 0:
        if L[i] > k:
            L[i + 1 ]= L[i]
        else:
            break
        i  = i - 1 
    L[i + 1 ] = K

#repeat 2 

def insert_at_sorting_pos(L):
    k = L[len(L)-1]
    i = len(L) - 2 
    while i >= 0:
        if L[i] < k:
            L[i+1] = L[i]
        else:break
        i = i -1 
    L[i + 1 ] = k

#repeat 3 
def insert_at_sorting_position(L):
    k = L[len(L)- 1]
    i = len(L) - 2 
    while i >= 0:
        if L[i] > k:
            L[i+1] = L[i]
        else:
            break
        i = i - 1 
    L[i + 1 ] = K