import sys
import random

L = []
def input_list():
    while True:
        response = int(input("Do you want to input data 0,1 :" ))
        if response == 0:
            break
        if response != 1:
            print("Invalid response, exiting..........")
            sys.exit() 
        
        data = int(input("Enter integer data value : "))
        L.append(data)
    return L


def insert_at_sorting_position(L,N:int):
    """
    L : is a list of element comtaining min 2 elements 
    2 <= N < len(L) 
    N :first 'N' element are to be considered i.e. 0..............N-1
    """
    k = L[N-1]
    i = N - 2 
    while i >= 0:
        if L[i] > k:
            L[i+1] = L[i]
        else:
            break
        i = i - 1 
    L[i+1] = k


def insertion_sort(L):
    N = 2 
    while N <= len(L):
        insert_at_sorting_position(L,N)
        N = N + 1 

def display(L,msg):
    print(msg)
    for i in range(len(L)):
        print(i,L[i])

def main():
    #L = input_list()
    L = [ random.randint(1,10) for  _  in range(4)]
    display(L,"before Sort")
    insertion_sort(L)
    display(L, "After Sort")

main()

    