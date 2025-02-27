import sys 
from geh  import geh
import random

try:    
    f_handle = open('abc.txt','w') #a = append , r = read , w = write 
    print("Yesssssddferfssssssss",file=f_handle)
    L = [random.randint(1,10) for _ in range(33)]
    for u in L:
        print(u,file=f_handle)

    
except:
    geh(should_exit=True,exit_msg= "sssss")

 