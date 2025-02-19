import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        len_1 = len(str1)
        len_2 = len(str2)

        if len_1 == len_2:
            return str1

        elif len_1 < len_2:
            return self.gcdOfStrings(str1, str2[len_1:])
            
        return self.gcdOfStrings(str2, str1[len_2:])


