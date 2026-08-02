class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        let seen = new Map();

        for (let i = 0; i < nums.length; i++){
            const indices = target - nums[i]

            if(seen.has(indices)){
                return [seen.get(indices), i]
            }

            seen.set(nums[i], i)
        }

    }
}
