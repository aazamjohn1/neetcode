class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # neetcode
        for i in range(n):
            print(haystack[i: m + i])
            if haystack[i: m + i] == needle:
                return i
        return -1

