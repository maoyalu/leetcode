/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    // Match exactly one .
    return address.replace(/\.{1}/g, '[.]')
}