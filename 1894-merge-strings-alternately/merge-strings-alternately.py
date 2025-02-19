class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_len = max(len(word1), len(word2))
        len_1 = len(word1)
        len_2 = len(word2)
        res = ""
        for i in range(max_len):
            if i < len_1:
                res += word1[i] 
            if i < len_2:
                res += word2[i] 
        return res
        



        