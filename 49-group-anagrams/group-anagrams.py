from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups a list of strings into anagrams.
        
        :param strs: List[str] - List of strings to be grouped
        :return: List[List[str]] - List of groups of anagrams
        """
        freq_anagrams = defaultdict(list)

        def generate_key(s):
            histo = [0] * 26
            for c in s:
                histo[ord(c) - ord('a')] += 1
            return tuple(histo)

        for string in strs:
            key = generate_key(string)
            freq_anagrams[key].append(string)

        return list(freq_anagrams.values())