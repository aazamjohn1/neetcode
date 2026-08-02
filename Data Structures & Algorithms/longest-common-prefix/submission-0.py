class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # first step I will need to have prefix as a first item 

        # and by traversing the strings i will pop them out from the stack 

        # res = ""
        # for i in range(len(strs[0])):
        #     for word in strs:
        #         if i == len(word) or word[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res

        pref = strs[0]

        for word in strs:
            while not word.startswith(pref):
                pref = pref[:-1]
        return pref