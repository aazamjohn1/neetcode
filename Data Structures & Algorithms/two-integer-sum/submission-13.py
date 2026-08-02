class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indeces; findNum = nums[i] - target
        #  if findNum in freq
        seen = {};

        for i, num in  enumerate(nums):
            indices = target - num;

            if indices in seen:
                return [seen[indices], i ];

            seen[num] = i