class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_len = 0
        is_dup = set()

        while right < len(s):
            while s[right]  in is_dup:
                is_dup.remove(s[left])
                left += 1
            is_dup.add(s[right]) 
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            right += 1

          
        return max_len

