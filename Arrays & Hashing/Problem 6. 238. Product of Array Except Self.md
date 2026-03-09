# Intuition 
<!-- Product of Array Except Self: Given an array of integers, return an array where each element at index i is the product of all elements in the input array except the one at index i.

e.g [1,2,3,4] -> [24,12,8,6]
Here, the product of all elements except the one at index 0 is 2*3*4 = 24, the product of all elements except the one at index 1 is 1*3*4 = 12, the product of all elements except the one at index 2 is 1*2*4 = 8, and the product of all elements except the one at index 3 is 1*2*3 = 6. --> 

  - Return an array where each element at index i is the product of all elements in the input array except the one at index i.


### Good to know
1. `Product` -> the result of multiplying a sequence of numbers together.
2. `Array`  -> a data structure that can hold a fixed number of values of the same type. It is a collection of elements identified by index or key.

### Approach 1. Brute Force works only for small input sizes. For larger input sizes, it will be inefficient due to its O(n^2) time complexity.
1. Create an empty list to store the result.
      ```
      result = []
      ```
2. Iterate through each element in the input array.
      ```
      for i in range(len(nums)):
      ```
3. For each element, calculate the product of all elements in the input array except the one at index i.
      ```
      product = 1
      for j in range(len(nums)):
          if i != j:
              product *= nums[j]
      ```
4. Append the calculated product to the result list.
      ```
      result.append(product)
      ```
5. Return the result list.
      ```
      return result
      ```
# Complexity Analysis
- Time Complexity: O(n^2) -> where n is the number of elements in the input array. We need to iterate through the array twice to calculate the product for each element.

- Space Complexity: O(n) -> we need to store the result in a new list of the same size as the input array.

```python
def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
```

### Approach 2. Optimal Solution with O(n) time complexity and O(1) space complexity (excluding the output array). 

1. Create an empty list to store the result and initialize it with 1s.
      ```
      result = [1] * len(nums)
      ```
2. Create a variable to keep track of the product of elements to the left of the current
  element and initialize it to 1.
      ```
      left_product = 1
      ```
3. Iterate through the input array from left to right and update the result list with the product of elements to the left of the current element.
      ```
      for i in range(len(nums)):
          result[i] *= left_product
          left_product *= nums[i]
      ```
4. Create a variable to keep track of the product of elements to the right of the current
  element and initialize it to 1.
      ```
      right_product = 1
      ```
5. Iterate through the input array from right to left and update the result list with the product of elements to the right of the current element.
      ```
      for i in range(len(nums) - 1, -1, -1):
          result[i] *= right_product
          right_product *= nums[i]
      ```
6. Return the result list.
      ```
      return result
      ``` 
# Complexity Analysis
- Time Complexity: O(n) -> where n is the number of elements in the input array. We need to iterate through the array twice to calculate the products for each element.

- Space Complexity: O(1) -> we are using only a constant amount of extra space to store the left and right products, and the result list is not counted as extra space since it is the output.

```pythondef productExceptSelf(nums):
    result = [1] * len(nums)
    left_product = 1
    for i in range(len(nums)):
        result[i] *= left_product
        left_product *= nums[i]   
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result
```   
# STEP BY STEP LEFT PRODUCT CALCULATION
### Initialize `left_product` to 1.
``` shell
left_product = 1
```
### i = 0:
``` shell
res[0] = 1 * 1 = 1
left_prod = 1 * 1 = 1
```
### i = 1:
``` shell
res[1] = 1 * 1 = 1
left_prod = 1 * 2 = 2
```
### i = 2:
``` shell
res[2] = 1 * 2 = 2
left_prod = 2 * 3 = 6
```
### i = 3:
``` shell
res[3] = 1 * 6 = 6
left_prod = 6 * 4 = 24
```



# STEP BY STEP RIGHT PRODUCT CALCULATION
### Initialize `right_product` to 1.

``` shell
right_product = 1
```

### i = 3 (last index):

``` shell
res[2] = 2 * 4 = 8
right_prod = 4 * 3 = 12
```

### i = 2:

``` shell
res[1] = 1 * 12 = 12
right_prod = 12 * 2 = 24
```
### i = 1:

``` shell
res[0] = 1 * 24 = 24
right_prod = 24 * 1 = 24
```
### i = 0:

``` shell
res[-1] = 1 * 24 = 24
right_prod = 24 * 1 = 24
```
