"""
@Author :  Swapnil Shrungare
@goal: 
    a) accept mass of two objects in kgs, distance 
    between them in meters, 
    b) do a validation check
    c) compute gravitational force of attraction 
    d) print the result 
"""


import sys


def compute_gravitaional_force(m1:float, m2:float , r:float) -> float:
    '''
    @input : 
        @m1 : Mass of object 1 in KGS
        @m2 : Mass of object 2 in KGS
        @r : Distance between  the objects in meters
    @output: 
        Gravitational force of attraction In Newton
    @exception:
        TypeError/ValueError
    '''
    if type(m1) != int and type(m1) != float:
        raise TypeError('Bad type of mass of object 1')
    if type(m2) != int and type(m2) != float:
        raise TypeError('Bad type of mass of object 2')
    if type(r) != int and type(r) != float:
        raise TypeError('Bad type for distance')
    if m1<= 0.0 or m2 <= 0.0 or r <= 0.0:
        raise ValueError('Magnititude of mass and distance must be positive')
    G = 6.67 * (10**-11)
    F = (G*m1*m2)/(r*r)
    return F


def main() -> None:
    '''
    @input : None
    @output : None
    @goal : a driver function of application
    '''
    m1 = float(input("Enter mass of object 1 in kgs:"))
    m2 = float(input("Enter mass of object 2 in kgs:"))
    r = float(input("Enter the distance between in the objects in meters:"))
    try: 
        F = compute_gravitaional_force(m1, m2, r)
    except: 
        exc_name, exc_data, exc_tb = sys.exc_info() 
        print(exc_name.__name__, exc_data, sep=':')
        sys.exit(-1)
    print(f'Force of attraction is:{F} Newton')
    sys.exit(-1)