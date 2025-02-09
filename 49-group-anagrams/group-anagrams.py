class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq_anagrams = {}
        for string in strs:
            key = str(sorted(string))
            if key in freq_anagrams:
                freq_anagrams[key].append(string)
            else:
                freq_anagrams[key] = [string]

        return list(freq_anagrams.values())
        