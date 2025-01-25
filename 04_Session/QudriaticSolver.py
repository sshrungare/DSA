"""
@Author :  Swapnil Shrungare 
@Goal :  Solve Qudriatic equation by accepting coeffiecients, check if real root is possble. 
if yes then compute and print the roots.
"""

import sys 

def  solve_qudriatic_equation(a:float, b:float, c:float) -> tuple[float]:
    '''
    a : Coefficient of x^2 
    b : Coefficient of x
    c : Constant term
    '''
    if type(a) != float or type(b) != float or type(c)  != float:
        raise TypeError
    if a == 0.0:
        raise ValueError('Coefficient of x^2 must be non-zero')
    if b**2 < 4*a*c:
        raise ValueError('Real roots are not possible')
    
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    T = (r1, r2)
    return T

def main() ->  None:
    """
    @input : None 
    @output : None 
    @goal : A driver function off application
    """
    try:
        a = float(input("Enter the coefficient of x^2 :"))
        b = float(input("Enter the coefficient of x :"))
        c = float(input("Enter the constant term :"))
        r1,r2 = solve_qudriatic_equation(a,b,c)
        print(f'R1:{r1} R2:{r2}')
    except:
        exc_cls , exc_data, exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=':')
        sys.exit(-1)
    sys.exit(0)

main()    