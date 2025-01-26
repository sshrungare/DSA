
#define class 
class Date:
    def  __init__(self, initday, initmonth, inityear):
        self.day = initday
        self.month = initmonth
        self.year = inityear


d = Date(11,1,2025)
print(d.__dict__)
