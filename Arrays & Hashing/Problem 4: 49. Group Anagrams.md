# Intuition
<!-- Given an array of strings, we need to group anagrams together. An anagram is a word formed by rearranging the letters of another word. -->

  - Return a list of groups of anagrams.
### Good to know
1. `Anagram` -> a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
2. `Hash Map` -> a data structure that implements an associative array abstract data type, a structure that can map keys to values.

# Approach
1. Create an empty hash map to store the groups of anagrams.
      ```
      anagram_groups = {}
      ```
2. Iterate through each string in the input array.
      ```
      for word in strs:
      ```
3. For each string, sort the characters in the string to create a key for the hash map.
      ```
      anagram_key = ''.join(sorted(word))
      ```
4. Check if the anagram key exists in the hash map. If it does, append the original string to the list of anagrams for that key. If it does not exist, create a new list with the original string.
      ```
      if anagram_key in anagram_groups:
          anagram_groups[anagram_key].append(word)
      else:
          anagram_groups[anagram_key] = [word]
      ```
5. After iterating through all the strings, return the values of the hash map as a
list of groups of anagrams.
      ```
      return list(anagram_groups.values())
      ```
# Complexity Analysis
- Time Complexity: O(n * k log k) -> where n is the number of strings in the input array and k is the maximum length of a string. Sorting each string takes O(k log k) time.

- Space Complexity: O(n * k) -> in the worst case, if all strings are anagrams of each other, we will store all n strings in the hash map, and each string can take up to O(k) space.

```python
def groupAnagrams(strs):
    anagram_groups = {}
    for word in strs:
        anagram_key = ''.join(sorted(word))
        if anagram_key in anagram_groups:
            anagram_groups[anagram_key].append(word)
        else:
            anagram_groups[anagram_key] = [word]
    return list(anagram_groups.values())
```
