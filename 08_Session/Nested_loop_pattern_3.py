print('start')
N  = 5
i = 0
while i<N:
    print("Outer loop start with i ", i)
    j = i + 1
    while j < N:
        print(f"i : {i} ,  j : {j}")
        j = j + 1
    i  = i + 1 

print('end')
