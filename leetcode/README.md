## Basics

### Strings

```python3
# parse a word into alphabet
word = "haha"
parsed = list(word)

print(parsed)
>>> ["h", "a","h","a"]
```


```python3
# convert alphabet to numerical values
num_a = ord("a") - 96 
num_b = ord("b") - 96 

print(num_a)
print(num_b)
>>> 1
>>> 2
```

```python3
# Return reversed value (palindrome)
# For string 
seqString = 'geeks'
print(list(reversed(seqString))) 
>>> ['s', 'k', 'e', 'e', 'g']

# For tuple 
seqTuple = ('g', 'e', 'e', 'k', 's') 
print(list(reversed(seqTuple))) 
>>> ['s', 'k', 'e', 'e', 'g']
  
# For range 
seqRange = range(1, 5) 
print(list(reversed(seqRange))) 
>>> [4, 3, 2, 1]

# For list 
seqList = [1, 2, 4, 3, 5] 
print(list(reversed(seqList))) 
>>> [5, 3, 4, 2, 1]

```

```python3
# Return the index of a certain element in a list
nums = [1,2,3,4,5]
nums.index(1)
>>> 0
```

```python3
# Remove '' from each elements in list
ans = ['1', '2', '-', '4', '5', '-', '7']
print(" ".join(ans))
>>> 1 2 - 4 5 - 7
```

```python3
# receive input for N X N grid with integers
maze = [list(map(int, list(input()))) for _ in range(4)]
print(maze)
>>> 1111
>>> 2342
>>> 3456
>>> 2467
>>> [[1, 1, 1, 1], [2, 3, 4, 2], [3, 4, 5, 6], [2, 4, 6, 7]]
```


### Hash
```python3
# Declaring hash table
hash_table = defaultdict(int)
```

```python3
# Incrementing count of certain key in hash table
for i in nums:                          
    hash_table[i] +=1                   
```

```python3
# Iterating over hashtable
hashtb = {'s': 2, 'd': 1, 'k': 1, 'a': 1, 'f': 1, 'n': 1}
for key, value in hashtb.items():
  print(key, value)
>>> s 2
>>> d 1
>>> k 1
>>> a 1
>>> f 1
>>> n 1
```

### Recursion
```python3
# Calling recursive function twice
return self.isSameTree(p.right, q.right) and \
    self.isSameTree(p.left, q.left)
```
