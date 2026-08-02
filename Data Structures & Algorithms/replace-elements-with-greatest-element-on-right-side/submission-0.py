class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        for i in range(len(arr) -1, -1, -1):
            curr = arr[i]
            arr[i] = max_num
            max_num = max(max_num, curr)

        return arr