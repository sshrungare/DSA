'''
@author : Swapnil Shrungare
@date :  24-02-2025
@goal :
    1) accept coef of qudriatic equations
    2) check if real roots are possib;e
    3) compute and return results
'''

import sys

def qudriatic_solver(first:float,second:float,constant:float) -> tuple[float]:
    '''
    @input : 
        first : coef of x^2 
        second : coef of x 
        constant : constant of equation
    @output : 
        roots 
    @exception:
        TypeError/ValueError
    '''

    if type(first) != float or type(second) != float or type(constant) != float:
        raise TypeError("invalid type")
    if first == 0.0 :
        raise ValueError("coef of x^2 can not be zero")
    if second**2 < 4*first*constant:
        raise ValueError("equation does not have real rooyts")
    r1 = (-second + (second**2 - 4*first*constant) **0.5 ) / (2*first)
    r2 = (-second - (second**2 - 4*first*constant) **0.5 ) / (2*first)
    T = (r1,r2)
    return T

def main() -> None:
    '''
    @input : None 
    @output : None 
    @goal : a application driver function
    '''
    try:
        first = float(input("Enter coef of x^2 : "))
        second = float(input("Enter coef of x : "))
        constant = float(input("Enter constant of equation : "))
        r1 , r2 = qudriatic_solver(first,second,constant)
        print(f"root1 :{r1} , root2 : {r2}")
    except:
        exc_cls , exc_data , exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=":")
        sys.exit(-1)
    sys.exit(0)

main()