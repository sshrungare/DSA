'''
@Author :  Swapnil Shrungare
@date : 24-02-2025
@goal : 
    1) accept coef of x^2 , x and Constant
    2) check if rots are real 
    3) compute and return the results
'''

import sys

def quadriatic_solver(cf1 : float,cf2: float,constant:float) -> tuple[float]:
    '''
    @input : 
        cf1 :  coef of x^2 
        cf : coef of x 
        constant : constant of equation
    @output : roots of equation
    @exception :
        TypeError/ValueError
    '''
    if type(cf1) != float or type(cf2) != float or type(constant) != float:
        raise TypeError("Invalid type")
    if cf1 == 0.0:
        raise ValueError("coef of x^2 can not be zero")
    if cf2**2 < 4*cf1*constant:
        raise ValueError("Equation does not have real roots")
    
    r1 = (-cf2 + (cf2**2 - 4*cf1*constant) ** 0.5)/ (2**cf1)
    r2 = (-cf2 - (cf2**2 - 4*cf1*constant) ** 0.5)/ (2**cf1)
    T = (r1,r2)
    return T

def main()->None:
    '''
    @iput : None
    @output: None 
    @goal : driver function
    '''
    try:
        cf1 = float(input("Enter coef of x^2 : "))
        cf2 = float(input("Enter coef of x : "))
        constant = float(input("Enter constant of equation: "))
        r1 , r2 = quadriatic_solver(cf1,cf2,constant)
        print(f"roots r1 {r1} , roots r2 : {r2}")
    except:
        exc_cls , exc_data, exc_tb =sys.exc_info()
        print(exc_cls.__name__,exc_data,sep= ":")
        sys.exit(-1)
    sys.exit(0)

main()