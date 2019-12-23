/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    // Initiate a variable count to 0. 
    // For every stone in S, if it is included in J, increase count by one, otherwise pass it as it is.
    // Return the final count
    return S.split('').reduce((count, current) => J.includes(current)? count + 1: count, 0)
}


// var numJewelsInStones = function(J, S) {
//     let count = 0
//     let jewels = J.split('').sort()
//     let stones = S.split('').sort()
//     let indexOfJ = 0
//     let indexOjS = 0
//     while(indexOfJ < jewels.length && indexOjS < stones.length) {
//         if(jewels[indexOfJ] < stones[indexOjS])
//             indexOfJ++
//         else if(jewels[indexOfJ] === stones[indexOjS]) {
//             indexOjS++
//             count++
//         } else
//             indexOjS++
//     }
//     return count
// }


// var numJewelsInStones = function(J, S) {
//     let count = 0
//     for(item of J) {
//         for(stone of S) {
//             if(item === stone)
//                 count++
//         }
//     }
//     return count
// }