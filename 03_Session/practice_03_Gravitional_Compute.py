"""
@author : Swapnil Shrungare
@goal : To accept mass of two objects in kgs , distance between 
        then in meters , to do a validation check and compute 
        gravitaion force off attraction and print the result
"""

import sys
def main() --> None:
    """
    @input : None
    @output : None 
    @goal : a driver function of application
    """
    m1 = float(input("Enter mass of object m1 in KGS:"))
    m2 = float(input("Enter mass of objcet m2 in KGS:"))
    r = float(input("Enter the distance between the ojects in meters:"))

    try : 
        F = computeGravitionalForce(m1,m2,r)
    except:
        exc_name , exc_data , exc_tb = sys.exc_info()
        print(exc_name.__name__, exc_data, sep = ":")
        sys.exit(-1)
    print(f'Force of attraction is:{F} Newton')
    sys.exit(-1)