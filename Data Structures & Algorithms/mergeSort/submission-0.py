# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # insertion sort
        # bacause it should be stable:
        # [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
        length = len(pairs)
        if length <= 1:
            return pairs
        midd = length // 2
        left = self.mergeSort(pairs[:midd])
        right = self.mergeSort(pairs[midd:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        return res
