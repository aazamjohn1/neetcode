class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        # {2,20,4,10,3,4,5}


        for num in nums:
            streak = 0
            curr = num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)

        return res
            