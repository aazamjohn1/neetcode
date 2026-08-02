class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indeces; findNum = nums[i] - target
        #  if findNum in freq
        seen = {};

        for i, num in  enumerate(nums):
            complement = target - num; #4
            if complement in seen:
                return [seen[complement], i]

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
