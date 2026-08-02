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




# class Solution {
#     /**
#      * @param {number[]} nums
#      * @param {number} target
#      * @return {number[]}
#      */
#     twoSum(nums, target) {
        
#         let seen = new Map();

#         for (let i = 0; i < nums.length; i++){
#             const indices = target - nums[i]

#             if(seen.has(indices)){
#                 return [seen.get(indices), i]
#             }

#             seen.set(nums[i], i)
#         }

#     }
# }
