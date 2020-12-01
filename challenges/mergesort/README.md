# <p align="center">[title]</p>

<p align="center">
<a href="#execution">Execution</a>
&nbsp; • &nbsp;
<a href="#problem">Problem</a>
&nbsp; • &nbsp;
<a href="#solution">Solution</a>
</p>

### Execution

Run `solution.py`:

```bash
$ make
```

Test solution with `pytest`:

```bash
$ make test
```

### Problem

Implement merge sort.

### Solution

| **Time Complexity** |  `O (n log n)` |
|-------|-------------|
Need to iterate through all elements during merging and splitting, so they are both that is `O(n)` (not nested).
`O (log n)` comes from halving the problem at every step during splitting, and then the inverse during merging.

| **Space Complexity** |  `O (n)` |
|-------|-------------|
Needs a helper array to store the sorted array.
The depth of the recursive call is less than `n`, so its dropped.

```python
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
```
