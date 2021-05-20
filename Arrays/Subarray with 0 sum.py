"""Write Python code to find if all the numbers in a given list of integers are part of the series defined by the following. 
f(0) = 0 f(1) = 1 f(n) = 9*f(n-1) - 4*f(n-2) for all n > 1. def is_part_of_series(lst):
"""
def SumZeroInList(l):
    pre_sum=0
    h=set()
    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum==0 or pre_sum in h:
            print(" Sum zero exsits")
            return
        h.add(pre_sum)
    return False

SumZeroInList([5,4,-3,-2,1])