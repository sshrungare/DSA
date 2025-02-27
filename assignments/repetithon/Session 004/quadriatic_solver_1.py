'''
@author : swapnil shurngare
@date : 24-02-2025
@goal : 
    1)accept coef of qudriatics equations
    2) check if roots are possible
    3) compute and return 
'''

import sys

def qudriatic_solver(a:float , b:float, c:float) -> tuple[float]:
    """
    a : coef of x^2 , 
    b : coef of X,
    c : constant
    """
    if type(a) != float or type(b) != float and type(c) != float:
        raise TypeError("Invalid type for coefs")
    if a == 0.0:
        raise ValueError("Coef of x^2 can not be zero")
    if b**2 < 4*a*c:
        raise ValueError("equation does not have real roots")
    
    r1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
    T = (r1,r2)
    return T

def main() -> None:
    '''
    @input : None
    @output: None
    @goal : A driver function of appplciation
    '''
    try:
        a = float(input("Enter Coef of X^2 : "))
        b = float(input("Enter coef of x : "))
        c = float(input("enter constant of equation : "))
        r1 , r2 = qudriatic_solver(a,b,c)
        print(f"root 1 : {r1} , root 2 : {r2}")
    except:
        exc_cls,exc_data,exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep = ":")
        sys.exit(-1)
    sys.exit(0)

main()