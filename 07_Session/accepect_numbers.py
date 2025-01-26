#create emmpty list with name L

L = []

while True:
    try:
        ans = int(input("do you want to add new numbers ? [1/0]"))
    except ValueError:
        print("Only Integers are allowed")
        break
    if ans != 1:
        break
    data = int(input("Enter Next number : " ))
    L.append(data)

i = 0 
while i < len(L):
    print(i,L[i])
    i = i + 1 