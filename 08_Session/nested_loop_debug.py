print('start')
i = 0
while i < 5 :
    print(f"Start of outer look with value of i {i}")
    j = 0
    while j< 3:
        print(i,j)
        j = j + 1
    i = i +1
print("End")
