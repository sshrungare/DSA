"""
@Author : Swapnil Shrungare
@date : 24-02-2025
@goal: 
    1) Accept xy cordinates of points A,B, and C
    2) check if points are linear 
    3) compute AB = c , BC = a and AC = b
"""
import sys

def are_linear(A:tuple[float],B:tuple[float],C:tuple[float]) -> bool:
    slope_AB = abs(B[1]-A[1]) / abs(B[0] - A[0])
    slope_BC = abs(C[1] - B[1]) / abs(C[0] - B[0])
    return slope_AB == slope_BC

def distance(A:tuple[float],B:tuple[float]) -> float:
    return ((B[1]- A[1]) ** 2 + (B[0] - A[0]) ** 2) ** 0.5

def area_from_point_cordinates(A:tuple[float] , B:tuple[float] ,C:tuple[float]) -> float:
    if are_linear(A,B,C):
        raise ValueError("Linear points do not form a triangle")
    length_AB = distance(A,B)
    length_BC = distance(B,C)
    length_CA = distance(C,A)

    a = length_BC
    b = length_CA
    c = length_AB
    s = (a+b+c) / 2 
    area = (s*(s-a) * (s-b) * (s-c)) ** 0.5
    return area


def main() ->None:
    '''
    @input :None 
    @output :None
    @goal: a application driver function
    '''

    x1 = float(input("Enter x cordinates of Point A : "))
    y1 = float(input("Enter y cordinates of point A : "))

    x2 = float(input("Enter x cordinates of Point B : "))
    y2 = float(input("Enter y cordinates of point B : "))

    x3 = float(input("Enter x cordinates of Point C : "))
    y3 = float(input("Enter y cordinates of point C : "))

    A = (x1,y1)
    B = (x2,y2)
    C = (x3,y3)

    try:
        area_of_triangle = area_from_point_cordinates(A,B,C)
        print(f"Area of triangle {area_of_triangle}")
    except:
        exc_cls , exc_data,exc_tb = sys.exc_info()
        print(exc_cls.__name__,exc_data,sep =":")
        sys.exit(-1)
    sys.exit(0)

main()