'''
@author : swapnil Shrungare
@date : 24-02-2025
@goal :
    1) accept xy coordinates of points A,B and C
    2) check if points are non colinear 
    3) Compute length = ab = c, bc = a , and ac = b
    4) Compute area using Horns formula
    5) print the results
'''

import sys

def are_linear(A:tuple[float] , B:tuple[float] , C:tuple[float]) -> bool:
    slope_AB = abs(B[1] - A[1]) / abs(B[0]-A[0])
    slope_BC = abs(C[1] - B[1]) / abs(C[0]-B[0])
    return slope_AB == slope_BC

def distance(A:tuple[float] , B:tuple[float]) -> float:
    return ((B[1] - A[1]) ** 2 + (B[0] - A[0]) **2 ) ** 0.5

def area_from_point_coordinates(A:tuple[float],B:tuple[float],C:tuple[float]) -> float:
    if are_linear(A,B,C):
        raise ValueError("Linear points do not form triangle")
    length_AB = distance(A,B)
    length_BC = distance(B,C)
    length_CA = distance(C,A)

    a = length_BC
    b = length_CA
    c = length_AB

    s = (a+b+c)/2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area

def main() -> None:
    '''
    @input : None
    @output : None
    @goal : a application driver function
    ''' 
    x1 = float(input("Enter x cordinate for point A: "))
    y1 = float(input("Enter y cordinate for point A: "))
    x2 = float(input("Enter x cordinate for point B: "))
    y2 = float(input("Enter y cordinate for point B: "))
    x3 = float(input("Enter x cordinate for point C: "))
    y3 = float(input("Enter y cordinate for point C: "))

    A = (x1,y1)
    B = (x2,y2)
    C = (x3,y3)

    try:
        area_of_triangle = area_from_point_coordinates(A,B,C)
        print(f"Area of triangle is {area_of_triangle}")
    except:
        exc_cls , exc_data, exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep=":")
        sys.exit(-1)
    sys.exit(0)

main()