'''
@author : Swapnil Shrungare
@date : 24-02-2025
@Goal : 
    1) Accept mass of two objects in kgs, distance between them in meters 
    2) do a validation check 
    3) compute gravitational force of attraction 
    4) print the result 
'''

import sys

def compute_gravitational_force(mass1:float,mass2:float,r:float) ->float:
    '''
    @input : 
        mass1 : mass of the object1 in kgs 
        mass2 : mass of the object2 in kgs
        r : distance between the objects in meters 
    @output : 
        gravitational force of attraction in newtons
    @exception :
        TypeError/ValueError
    '''

    if type(mass1) != int and type(mass1) != float:
        raise TypeError("Bad Type for mass of object 1")
    if type(mass2) != int and type(mass2) != float:
        raise TypeError("bad type for mass of object m2")
    if type(r) != int and type(r) != float:
        raise TypeError("bad type for distance r")
    
    if mass1 <= 0.0 or mass2 <= 0.0 and r <= 0.0:
        raise ValueError('magnitude of mass and distance must be positive')
    
    G = 6.67 * (10 ** -11)
    F = (G*mass1* mass2) / (r**2)
    
    return F

def main() -> None:
    '''
    @input : None 
    @output : None
    @goal: a driver function of application
    '''
    try:
        mass1 = float(input("Enter mass of object 1 in kgs : "))
        mass2 = float(input("Enter mass of object 2 in kgs : "))
        r = float(input("Enter the distance between the objects in meters : "))
        F  = compute_gravitational_force(mass1,mass2,r)
        print(f"force of attraction is : {F} Nwton")
    except:
        exc_cls , exc_data, exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=":")
        sys.exit(-1)
    
    sys.exit(0)

main()