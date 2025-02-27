import sys

L = []

while True:
    response = int(input("Do you want to input data 0,1 :" ))
    if response == 0:
        break
    if response != 1:
        print("Invalid response, exiting..........")
        sys.exit() 
    
    data = int(input("Enter integer data value : "))
    L.append(data)

print("User Input List : ",L )