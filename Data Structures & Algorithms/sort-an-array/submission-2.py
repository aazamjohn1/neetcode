class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # doing with insertion sort:

        # for i in range(1, len(nums)):
        #     key = nums[i]
        #     j = i - 1
        #     while j >= 0 and nums[j] > key:
        #         nums[j + 1] = nums[j]
        #         j -= 1
        #     nums[j + 1] = key
        # return nums
    #     if len(nums) <= 1:
    #         return nums
    #     midd = len(nums) // 2

    #     left = self.sortArray(nums[:midd])
    #     right = self.sortArray(nums[midd:])
    #     return self.merge(left, right)

    # def merge(self, left, right):
    #     result = []
    #     i = j = 0

    #     while i < len(left) and j < len(right):
    #         if left[i] <= right[j]:
    #             result.append(left[i])
    #             i += 1
    #         else:
    #             result.append(right[j])
    #             j += 1
    #     result.extend(left[i:])
    #     result.extend(right[j:])
    #     return result
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


        