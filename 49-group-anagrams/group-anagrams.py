class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq_anagrams = {}
        for string in strs:
            if str(sorted(string)) in freq_anagrams:
                freq_anagrams[str(sorted(string))].append(string)
            else:
                freq_anagrams[str(sorted(string))] = [string]

        return list(freq_anagrams.values())
        