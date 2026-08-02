class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
     // map dan foydalanamiz. 

    //  agar mapni ichida bo'lsa false qaytarimiz bo'ldi. 
    let seen = new Map();

    for(let num of nums){
        if(seen.has(num)){
            return true
        }
      seen.set(num)
    }

    return false





    // for (let i = 0; i < nums.length; i++){
    //     for(let j = i + 1; j < nums.length; j++){
    //         if(nums[i] === nums[j]){
    //             return true
    //         }
    //     }
    // }
    // return false
    }
}
