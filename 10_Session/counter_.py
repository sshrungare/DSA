"""
step 1- take a list from end user 
step 2 - count all unique numbers in the list along with the repetation count
"""
import sys

def input_list():
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
    return L

def get_unique_list_with_repeat_count(L:list):
    output_list = []
    i = 0 
    while i < len(L):
        current_element  = L[i]
        j = 0 
        found_flag = False 
        while j < i:
            if L[j] == current_element:
                found_flag = True
                break
            j = j  + 1

        if found_flag == True:
            i = i + 1 
            continue
        else:
            count = 0 
            j = i 
            while j < len(L):
                if L[j] == current_element:
                    count = count + 1 
                j = j + 1
            T = (current_element,count)
            output_list.append(T)    
        i = i + 1  
    return (output_list)

L = [12312,213,123,123,123,123,123,123,123,22,423,534,6456,456,3456,3456,12345,243]

print(get_unique_list_with_repeat_count(L))