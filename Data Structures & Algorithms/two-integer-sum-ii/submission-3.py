class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp] + 1, index + 1]
            seen[num] = index