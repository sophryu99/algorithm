# Sorting

## Binary Search

Looking for a specific item: **Linear Time O(N)**

If the array is sorted, we can perform binary search: **Logarithmic Time** **OLog(N)**

- Divide and conquer



Use sorting as a data compression, computer graphics



### Insertion Sort

```markdown
Question:

For i = 1, 2, ... n, insert A[i] into sorted array A[0: i - 1] by pairwise swaps down to the correct positions. 
```



```python
# Unsorted array
# Key = arr[1], 2
arr = [5, 2, 4, 6, 1 ,3]

# Step1: Swap elements pairwise if arr[i] > arr[i + 1]
# key = arr[2], 5
arr = [2, 5, 4, 6, 1, 3]

# key = arr[3], 5
arr = [2, 4, 5, 6, 1, 3]

# key = arr[4], 6
arr = [2, 4, 5, 6, 1, 3]

# key = arr[5], 1
# Swap occurs
# The key keeps swapping places until it reaches to a position where arr[i] < arr[i + 1]
arr = [2, 4, 5, 6, 1, 3]
arr = [2, 4, 5, 1, 6, 3]
arr = [2, 4, 1, 5, 6, 3]
arr = [2, 1, 4, 5, 6, 3]
arr = [1, 2, 4, 5, 6, 3]

# key = arr[5], 3
arr = [1, 2, 4, 5, 6, 3]
arr = [1, 2, 4, 5, 3, 6]
arr = [1, 2, 4, 3, 5, 6]
arr = [1, 2, 3, 4, 5, 6]
```

Total of **theta(n)** steps in terms of key positions. 

- Each step is **theta(n)** compares(steps)



**Compares** are more expensive than **swaps**

### Merge sort

- Assume there are two sorted array, and merge them



