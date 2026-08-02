class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_max = 0

        for num in nums:
            curr_max = max(curr_max, 0) + num
            max_sum = max(max_sum, curr_max)
        return max_sum 
        