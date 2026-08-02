class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sString = s.split("").sort().join("")
        const tString = t.split("").sort().join("")
        return sString === tString
    }
}
