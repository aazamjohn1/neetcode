class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}
        # for index, num in enumerate(numbers):
        #     comp = target - num
        #     if comp in seen:
        #         return [seen[comp] + 1, index + 1]
        #     seen[num] = index

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right+1 ]



