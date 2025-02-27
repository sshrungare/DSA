L = [10,20,30,40,50]

#1 add one more elemet 60 at the end of list
#2 shift all elements 10 to 50 to one place right
#3 put integer value 60 at index 0 

L.append(60)
print(L)
 
end = L[len(L) - 1 ]

for i in range(len(L)):
    L[i+1] = L[i]

print(L)
