class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums) // 2]
        # major_table = {}
        # for num in nums:
        #     major_table[num] = major_table.get(num, 0) + 1
        #     if major_table[num] > len(nums) // 2:
        #         return num

        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else - 1
        return candidate
