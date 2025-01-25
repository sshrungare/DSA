'''
@author: Swapnil Shrungare
@Date: 12th jan 2025
@Goal: 
    1) Accept : x -y Coordinates of points A , B , C
    2) Assert : Points A, B and C are non collinear
    3) Compute : 
        a) Length of side AB = c 
        b) length of side BC = a
        c) length of side AC = b 
        d) Area of triangle ABC using Horn's formula
    4) Print : the area computed in 3d 
'''

import sys

def areLinear(A:tuple[float],B:tuple[float],C:tuple[float]) -> bool:
    slope_AB = abs(B[1]-A[1])/(B[0]-A[0])
    slope_BC = abs(C[1]-B[1])/(C[0]-B[0])
    slope_AC = abs(C[1]-A[1])/(C[0]-A[0])
    return slope_AB == slope_BC == slope_AC

def distance(A:tuple[float],B:tuple[float]) -> float:
    return ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5

def compute_area_of_triangle(A:tuple[float],B:tuple[float],C:tuple[float]) -> float:
    '''
    @input : 
    ''' 
    if areLinear(A,B,C):
        raise ValueError('Points A,B and C are collinear')
    a = distance(B,C)
    b = distance(A,C)
    c = distance(A,B)
    s = (a+b+c)/2
    area = (s * (s-a) * (s-b) * (s-c))  ** 0.5
    return area

def main():
    x1 = float(input("Enter x1:"))
    y1 = float(input("Enter y1:"))

    x2 = float(input("Enter x2:"))
    y2 = float(input("Enter y2:"))

    x3 = float(input("Enter x3:"))
    y3 = float(input("Enter y3:"))

    A = (x1,y1)
    B = (x2,y2)
    C = (x3,y3)

    area_of_triangle = compute_area_of_triangle(A,B,C)
    print(f'Area of triangle is :{area_of_triangle}')

    sys.exit(0)
    

main()