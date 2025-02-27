import random

L  = [random.randint(1,20) for _ in range(3)]

def insert_at_sorting_position(L,N):
    """
    L : List to be sorted
    N : Length to be sorted
    """
    k = L[N- 1] 
    i = N - 2 
    print(k,i)
    while i >= 0:
        print(L)
        if L[i] > k:
            L[i+1] = L[i]
        else:
            break
        i = i - 1 
    L[i+1] = k
    return L

def insertion_sort(L):
    N = 2 
    while N <= len(L):
        insert_at_sorting_position(L,N)
        N = N + 1 

print(L)
insertion_sort(L)
print(L)