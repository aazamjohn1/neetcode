# Intuiton 
Given two strings `s` and `t` we need to check if `t` is an anagram of `s`.

- return `True`  -> if `t` is an anagram of `s`
- return `False` -> if `t` is not an anagram of `s`

### Good to know

1. `Anagram` -> a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Approach
1. Create a frequency dictionary to count the occurrences of each character in string `s`.

      ```
      frequency = {}
      for char in s:
          if char in frequency:
              frequency[char] += 1
          else:
              frequency[char] = 1
       <!-- frequency[char] = frequency.get(char, 0) + 1 -->
      ```
2. Iterate through each character in string `t` and update the frequency dictionary.

      ```
      for char in t:
          if char in frequency:
              frequency[char] -= 1
              if frequency[char] < 0:
                  return False
          else:
              return False
      ```
3. If the loop completes without returning `False`, return `True` as `t` is an anagram of `s`.
      ```
      return True
      ``` 
# Complexity Analysis
- Time Complexity: O(n) -> where n is the length of the longer string between `s` and `t`. We need to iterate through both strings to build the frequency dictionary and check

- Space Complexity: O(1) -> since the frequency dictionary will at most contain 26 characters (assuming only lowercase letters), the space complexity is constant.

```python
def isAnagram(s, t):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    for char in t:
        if char in frequency:
            frequency[char] -= 1
            if frequency[char] < 0:
                return False
        else:
            return False
    return True
```

