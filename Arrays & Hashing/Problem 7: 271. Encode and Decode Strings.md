# Intuition
<!-- Given an array of strings, we need to encode a list of strings to a single string and decode a single string to a list of strings. 

 e.g. ["Hello","World"] -> "5#Hello5#World"
Here, we encode the list of strings by concatenating the length of each string followed by a '#' character and then the string itself. To decode the encoded string, we can split the string by the '#' character and extract the original strings based on their lengths. -->

  - Return an encoded string for a list of strings and decode a single string to a list of strings.
### Good to know
1. `Encoding` -> the process of converting data into a different format using a specific scheme.
2. `Decoding` -> the process of converting encoded data back into its original format.

# Approach
1. To encode a list of strings, we can iterate through each string in the list and concatenate the length of the string followed by a '#' character and then the string itself to create the encoded string.
      ```
      def encode(strs):
          encoded_string = ''
          for s in strs:
              encoded_string += str(len(s)) + '#' + s
          return encoded_string
      ``` 
2. To decode the encoded string, we can iterate through the encoded string and extract the original strings based on their lengths. We can use a while loop to read the length of each string, then read the string itself, and add it to the list of decoded strings.
      ```
      def decode(encoded_string):
          decoded_strings = []
          i = 0
          while i < len(encoded_string):
              j = i
              while encoded_string[j] != '#':
                  j += 1
              length = int(encoded_string[i:j])
              decoded_strings.append(encoded_string[j+1:j+1+length])
              i = j + 1 + length
          return decoded_strings
      ```
# Complexity Analysis
- Time Complexity: O(n) -> where n is the total length of the encoded string. We need to iterate through the encoded string once to decode it.  
- Space Complexity: O(n) -> in the worst case, if all strings are of length 1, we will store all n characters in the list of decoded strings.

```python
def encode(strs):
    encoded_string = ''
    for s in strs:
        encoded_string += str(len(s)) + '#' + s
        # ["Hello", "World"] -> "5#Hello5#World"
    return encoded_string 


def decode(encoded_string):
    decoded_strings = []
    i = 0
    while i < len(encoded_string):
        j = i
        while encoded_string[j] != '#':
            j += 1
        length = int(encoded_string[i:j])
        decoded_strings.append(encoded_string[j+1:j+1+length])
        i = j + 1 + length
    return decoded_strings
```

### Step-by-Step Walkthrough

#### String:
``` shell
"4#leet4#code2#is3#fun"
```
#### Step 1: Initialize variables
``` shell
decoded_strings = []
i = 0
```
#### Move j until #
``` shell
4#leet...
 ^
 j
```

``` shell
length = int("4") = 4
```

### Extract the string based on the length
``` shell
s[2:6] = "leet"
```
#### Add the extracted string to the list of decoded strings
``` shell
decoded_strings = ["leet"]
```#### Move i to the next position after the extracted string
``` shell
i = 6
```

#### Move j until #
``` shell
4#leet4#code...
      ^
      i 
```
#### Find #
``` shell
length = int("4") = 4
```
#### Extract the string based on the length
``` shell
s[8:12] = "code"
```
#### Add the extracted string to the list of decoded strings
``` shell
decoded_strings = ["leet", "code"]
```
#### Move i to the next position after the extracted string
``` shell
i = 12
```
#### Step 3: Find the next '#'
``` shell
2#is
length = int("2") = 2
```
#### Extract the string based on the length
``` shell
s[14:16] = "is"
```
#### Add the extracted string to the list of decoded strings  
``` shell
decoded_strings = ["leet", "code", "is"]
```
#### Move i to the next position after the extracted string
``` shell
i = 16
```
#### Step 4: Find the next '#'
``` shell
3#fun
length = int("3") = 3
```
#### Extract the string based on the length
``` shell
s[18:21] = "fun"
```
#### Add the extracted string to the list of decoded strings
``` shell
decoded_strings = ["leet", "code", "is", "fun"]
```
#### Move i to the next position after the extracted string
``` shell
i = 21
```
#### Step 5: Return the list of decoded strings
``` shell
# FINAL OUTPUT
return ["leet", "code", "is", "fun"]
```   





