'''
@author : Swapnil Shrungare
@date : 24-02-2025
@Goal : 
    1) Accept mass of two objects in kgs , distance between them in meters 
    2) do a validation check 
    3) compute gravitational force of attraction 
    4) print the result 
'''

import sys

def compute_gravitational_force(m1:float,m2:float,r:float) ->float:
    '''
    @input : 
        m1 : mass of the object1 in kgs 
        m2 : mass of the object2 in kgs
        r : distance between the objects in meters 
    @output : 
        gravitational force of attraction in newtons
    @exception :
        TypeError/ValueError
    '''

    if type(m1) != int and type(m1) != float:
        raise TypeError("Bad Type for mass of object 1")
    if type(m2) != int and type(m2) != float:
        raise TypeError("bad type for mass of object m2")
    if type(r) != int and type(r) != float:
        raise TypeError("bad type for distance r")
    
    if m1 <= 0.0 or m2 <= 0.0 and r <= 0.0:
        raise ValueError('magnitude of mass and distance must be positive')
    
    G = 6.67 * (10 ** -11)
    F = (G*m1*m2)/(r**2)
    return F

def main() -> None:
    '''
    @input : None 
    @output : None
    @goal : a driver function of application
    '''
    try:
        m1 = float(input("Enter mass of object 1 in kgs : "))
        m2 = float(input("Enter mass of object 2 in kgs : "))
        r = float(input("Enter the distance between the objects in meters : "))
        F  = compute_gravitational_force(m1,m2,r)
        print(f"force of attraction is : {F} Newton")
    except:
        exc_cls , exc_data, exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=":")
        sys.exit(-1)
    
    sys.exit(0)

main()