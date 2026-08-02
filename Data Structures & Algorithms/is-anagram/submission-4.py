from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counter = Counter(s)

        for num in t:
            if num in char_counter:
                if char_counter[num] > 0:
                    char_counter[num] = char_counter[num] - 1
                    if char_counter[num] == 0:
                        del char_counter[num]
            else: 
                return False

        return True
