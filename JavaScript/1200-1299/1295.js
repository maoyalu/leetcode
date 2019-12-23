/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let count = 0
    for(num of nums) 
    {
        if(nums.toString().length % 2 == 0) {
            count++
        }
    }
    return count
}