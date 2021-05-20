from collections import Counter

def isPal(s):
    count=Counter(s)
    odd=0
    for freq in count.values():
        if freq%2 != 0:
            odd +=1
            if odd>1:
                return False
    return True
    
    