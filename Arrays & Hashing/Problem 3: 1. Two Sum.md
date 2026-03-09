# Intuition
<!-- Given an array of numbers, we need to find two numbers that add up to a specific target. -->

  - Return the indices of the two numbers that add up to the target.

### Good to know
1. `Array`  -> a data structure that can hold a fixed number of values of the same type. It is a collection of elements identified by index or key.

2. `Hash Map` -> a data structure that implements an associative array abstract data type, a structure that can map keys to values. 

3. `Target` -> a specific value that we want to achieve by adding two numbers from the array.

# Approach

1. Create an empty hash map to store the indices of the numbers we have seen so far.

      ```
      num_to_index = {}
      ```
2. Iterate through each number in the input array along with its index.
      ```
      for i, num in enumerate(nums):
      ```
3. For each number, calculate the complement by subtracting the current number from the target.

      ```
      complement = target - num
      ```

4. Check if the complement exists in the hash map. If it does, return the indices of the current number and the complement.

      ```
      if complement in num_to_index:
          return [num_to_index[complement], i]
      ```
5. If the complement does not exist in the hash map, add the current number and its
  index to the hash map.
  
        ```
        num_to_index[num] = i
        ```
6. If the loop completes without finding a pair that adds up to the target, return an empty list.
      ```
      return []
      ```

# Complexity Analysis
- Time Complexity: O(n) -> where n is the number of elements in the input array

- Space Complexity: O(n) -> in the worst case, if all elements are unique, we will store all n elements in the hash map.

```python
def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
```
