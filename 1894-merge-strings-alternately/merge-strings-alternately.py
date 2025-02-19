class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_len = min(len(word1), len(word2))
        res = ""
        for i in range(min_len):
            res += word1[i]
            res += word2[i]
        res += word1[min_len:]
        res += word2[min_len:]
        return res
        



        