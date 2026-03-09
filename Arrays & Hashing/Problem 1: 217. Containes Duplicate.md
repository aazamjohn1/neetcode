### Intuition
<!-- Given an array of numbers, we need to check if any value repeats. -->

  - Return `True`  -> if any value repeats
  - Return `False` -> if all values are unique

### Good to know 

1. `Array`  -> a data structure that can hold a fixed number of values of the same type. It is a collection of elements identified by index or key.

2. `Duplicate` -> an element that appears `more than once` in a given array.

3. Distinct -> an element that appears `only once` in a given array.

# Approach

<!-- Describe your approach to solving this problem -->

1. Create an empty set to store unique elements.

      ```
      unique_elements = set()
      ```
2. Iterate through each element in the input array.

      ```
      for num in nums:
      ```
3. For each element, check if it is already in the set of unique elements.

      ```
      if num in unique_elements:
          return True
      ```
4. If the element is not in the set, add it to the set.
      ```
      unique_elements.add(num)
      ```
5. If the loop completes without finding any duplicates, return `False`.
      ```
      return False
      ```

# Complexity Analysis
- Time Complexity: O(n) -> where n is the number of elements in the input array. We need to iterate through the array once to check for duplicates.

- Space Complexity: O(n) -> in the worst case, if all elements are unique, we will store all n elements in the set.

# Code Implementation

```python
def containsDuplicate(nums):
    unique_elements = set()
    for num in nums:
        if num in unique_elements:
            return True
        unique_elements.add(num)
    return False
```







<h1> Approach </h1>


