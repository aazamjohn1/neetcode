class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique = set(nums)
        for num in nums:
            if num - 1 not in unique:
                length = 0
                curr = num
                while curr in unique:
                    length += 1
                    curr += 1
                result = max(result, length)
        return result