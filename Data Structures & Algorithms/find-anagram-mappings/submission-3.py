class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
        # Output: [1,4,3,2,0]
        # res = []
        # for i, num in enumerate(nums1):
        #     for j, jnum in enumerate(nums2):
        #         if num == jnum:
        #             res.append(j)
        #             break
        # return res
        mapping = {}
        res = []

        for i in range(len(nums2)):
            mapping[nums2[i]] =  i # O(n)
        for num in nums1:
            if num in mapping:
                res.append(mapping[num])
        return res


"""
- Edge cases:
- What if the input is empty -> never be an empty
- are the lenght also be similar -> nums2.length == nums1.length
- if [40, 40] and [40, 40]
- Brute force approach:

    res = [1, 4, 3, 2, 0]
    -first nums1 iteration
    -second nums2 iteration

- Hash Table approach:
    table = {"50" : 0, "12": 1 ...}
"""