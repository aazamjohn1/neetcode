class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {

        let leftIndex = 0;
        let rightIndex = nums.length - 1
     while(leftIndex <= rightIndex){
        let middleIndex = Math.floor((leftIndex + rightIndex) / 2) 
        if(target == nums[middleIndex]){
            return middleIndex
        }

        if(target < nums[middleIndex]){
            rightIndex = middleIndex - 1
        }else{
            leftIndex = middleIndex + 1
        }
     }
     return -1
      
    }
}
