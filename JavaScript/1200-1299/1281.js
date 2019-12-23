/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let nums = (n + '').split('').map(s => parseInt(s))
    let product = nums.reduce((acc, cur) => acc * cur)
    let sum = nums.reduce((acc, cur) => acc + cur)
    return product - sum
}