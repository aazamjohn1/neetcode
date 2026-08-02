class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # max_num = -1
        # for i in range(len(arr) -1, -1, -1):
        #     curr = arr[i]
        #     arr[i] = max_num
        #     max_num = max(max_num, curr)

        # return arr

        # Brute force yechm:
    
        for i, num in enumerate(arr):
            max_num = -1
            for j in range(i + 1, len(arr)):
                if max_num < arr[j]:
                    max_num = arr[j]
            arr[i] = max_num
        return arr
