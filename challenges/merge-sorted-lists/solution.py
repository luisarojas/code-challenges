# Solution
def merge(array_a, array_b):
    
    results = list()
    while len(array_a) > 0 and len(array_b) > 0:
        
        if array_a[0] < array_b[0]:
            results.append(array_a[0])
            array_a = array_a[1:]
        else:
            results.append(array_b[0])
            array_b = array_b[1:]
            
    if (len(array_a) > 0): results += array_a
    elif (len(array_b) > 0): results += array_b
        
    return results