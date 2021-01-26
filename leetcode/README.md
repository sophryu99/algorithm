## Python basics

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
