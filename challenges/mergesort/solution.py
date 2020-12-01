# Solution
def merge_sort(array): 
    
    if len(array) <= 1: return array
    
    middle = len(array)//2
    
    # build back up with merge
    head = merge_sort(array[:middle])
    tail = merge_sort(array[middle:])
    
    return merge(head, tail)
    
def merge(a, b):
    
    print('merging {} and {}'.format(a, b))
    
    new_list = list()
    
    while len(a) > 0 and len(b) > 0:
        
        if a[0] < b[0]:
            new_list.append(a[0])
            a = a[1:]
        else:
            new_list.append(b[0])
            b = b[1:]
            
    if len(a) > 0: new_list += a
    elif len(b) > 0: new_list += b
        
    return new_list