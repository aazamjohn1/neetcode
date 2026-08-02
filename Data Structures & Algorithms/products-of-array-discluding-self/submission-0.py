class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n #first loop: [1, 1, 2, 6]

        left_prod = 1
        # input [1, 2, 3, 4]
        # 1st iter: 1 * 1
        for i in range(n):
            res[i] *= left_prod
            # i = 0 -> 1 * 1 = 1
            # i = 1 -> 1 * 1 = 1
            # i = 2 -> 1 * 2 = 2
            # i = 3 -> 1 * 6 = 6
            left_prod *= nums[i]
            # i = 0 -> 1 * 1 = 1
            # i = 1 -> 1 * 2 = 2
            # i = 2 -> 2 * 3 = 6
            # i = 3 -> 6 * 4 = 24
        
        #second loop: res = [24, 12, 8, 6]
        right_prod = 1 
        for i in range(n - 1, -1, -1):
            res[i] *= right_prod 
            # i = 3 -> 6 * 1 = 6
            # i = 2 -> 2 * 4 = 8
            # i = 1 -> 1 * 12 = 12
            # i = 0 -> 1 * 24 = 24
            right_prod *= nums[i]
            # i = 3 -> 1 * 4 = 4
            # i = 2 -> 4 * 3 = 12
            # i = 1 -> 12 * 2 = 24
            # i = 0 -> 24 * 1 = 24
        return res


