import sys 

def get_listof_numbers_from_file(file_path:str) -> [int]:
    try :
        f_handle = open(file_path,"r")
    except:
        print("Error in opening file")
        sys.exit()
    
    L = []
    for line in f_handle:
        line = line.strip()
        try:
            n = int(line)
            L.append(n)
        except:
            print("Bad integer format")
            f_handle.close()
            sys.exit()
    f_handle.close()
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
    #L = [ random.randint(1,10) for  _  in range(4)]
    L = get_listof_numbers_from_file('num.txt')
   
    display(L,"before Sort")
    insertion_sort(L)
    display(L, "After Sort")

main()