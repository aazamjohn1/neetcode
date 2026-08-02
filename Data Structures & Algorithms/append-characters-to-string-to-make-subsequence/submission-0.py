class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        left = right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
               right += 1
            left += 1
        return len(t)  - right