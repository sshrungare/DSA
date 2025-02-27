import sys

def get_num_from_file(file_path:str) ->[int]:
    try:
        f_handle = open(file_path)
    except:
        print("error opening file...")
        sys.exit()
    L = []
    for line in f_handle:
        line = line.strip()
        try:
            n = int(line)
            L.append(n)
        except:
            print("bad format for int")
        
    return L


lst  = get_num_from_file('num.txt')
print(lst)
        
        
        