# <p align="center">Merge Sorted Lists</p>

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

**Description**

Given two sorted lists, merge them into a single sorted list.

**Examples**

```
Input:
	head1: 5->7->9
	head2: 4->6->8 
Output : 4->5->6->7->8->9
```
```
Input:
	head1: 1->3->5->7
	head2: 2->4
Output : 1->2->3->4->5->7
```

### Solution

| **Time Complexity** |  `O(n)` |
|-------|-------------|
Where `n` is the length of the shortest array.

| **Space Complexity** |  `O(n+m)` |
|-------|-------------|
Need the space equivalent to the length of array `n` and array `m` in order to hold the newly sorted list.

```python
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
```
