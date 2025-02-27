'''
@author : Swapnil Shrungare
@date : 24-02-2025
@goal:
    1) accept x,y co-ordinates of a,b,c
    2) check if points are non colinear
    3) compute : length ab = c , bc = a and ac = b
    4) legth of triangle abc using Horns formula
    5) Print the result 
'''

import sys

def are_linear(A:tuple[float],B:tuple[float],C:tuple[float]) -> bool:
    slope_of_AB = abs(B[1]-A[1]) / abs(B[0]- A[0])
    slope_of_BC = abs(C[1]-B[1]) / abs(C[0]-B[0])
    return slope_of_AB == slope_of_BC

def distance(A:tuple[float] , B:tuple[float]) -> float:
    return ((B[1] - A[1] ) **2 + (B[0] - A[0]) **2 ) ** 0.5

def area_from_point_coordinates(A:tuple[float],B:tuple[float] , C:tuple[float]) -> float:
    if are_linear(A,B,C):
        raise ValueError("Linear point do not form triangle")
    length_ab = distance(A,B)
    length_bc = distance(B,C)
    length_ca = distance(C,A)
    a = length_bc
    b = length_ca
    c = length_ab
    s = (a+b+c) / 2 
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area

def main() -> None:
    '''
    @input : None 
    @output : None 
    @goal : driver function of application
    '''
    x1 = float(input("Enter x cordinate of A : "))
    y1 = float(input("Enter y cordinate of A : "))

    x2 = float(input("Enter x cordinate of B "))
    y2 = float(input("Enter y cordinate of B : "))

    x3 = float(input("Enter x cordinate of C : "))
    y3 = float(input("Enter y cordinate of C : "))

    A = (x1,y1)
    B = (x2,y2)
    C = (x3,y3)

    try:
        area_of_triangle = area_from_point_coordinates(A,B,C)
        print(f"Area of triangle is {area_of_triangle}")
    except:
        exc_cls , exc_data,exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=":")
        sys.exit(-1)
    sys.exit(0)

main()