import re

def my_atoi(string): # string to integer
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    res = re.match(r'\s*([-+]?\d+)(.*)', string)    
    if res:

        n = int(res.group(1))
        n = min(INT_MAX, n)
        n = max(INT_MIN, n)
        
        return n
    
    else:
        return 0