# Intuition 
 <!-- Top K frequent elements: Find the k most frequently occurring elements in an array. 
 
 e.g. [1,1,1,2,2,3], k = 2 -> [1,2]
 here, 1 appears 3 times, 2 appears 2 times, and 3 appears 1 time. The top 2 frequent elements are 1 and 2. -->

  - Return the k most frequently occurring elements in an array.

### Good to know
1. `Frequency` -> the number of times an element appears in a given array.

# Approach
1. Create a frequency dictionary to count the occurrences of each element in the input array.
      ```
      frequency = {}
      for num in nums:
          frequency[num] = frequency.get(num, 0) + 1
      ```
2. we need res = [] -> to store the k most frequent elements.
      ```
      res = []
      ```
3. Iterate through the frequency dictionary and add the elements to the result list based on their frequency.
      ```
      for num, freq in frequency.items():
          res.append([freq, num])
      ```
4. Sort the result list based on frequency in descending order.
      ```
      res.sort()
      ```
5. Create an empty list to store the top k frequent elements.
      ```
      arr = []
      ```
6. Pop the last k elements from the sorted result list and add the corresponding numbers to the top k frequent elements list.
      ```
      while len(arr) < k:
          arr.append(res.pop()[1])
      ```
7. Return the list of top k frequent elements.
      ```
      return arr
      ```   

# Complexity Analysis
- Time Complexity: O(n log n) -> where n is the number of unique elements in the input array. Sorting the frequency list takes O(n log n) time.

- Space Complexity: O(n) -> in the worst case, if all elements are unique, we will store all n elements in the frequency dictionary and the result list.

```python
def topKFrequent(nums, k):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    res = []
    for num, freq in frequency.items():
        res.append([freq, num]) 
    res.sort()

    arr = []
    while len(arr) < k:
        arr.append(res.pop()[1])
    return arr 
    
```

 