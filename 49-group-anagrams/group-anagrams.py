
class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups a list of strings into anagrams.
        
        :param strs: List[str] - List of strings to be grouped
        :return: List[List[str]] - List of groups of anagrams
        """
        freq_anagrams = {}

        def generate_key(s):
            histo = [0] * 26
            for c in s:
                histo[ord(c) - ord('a')] += 1
            return tuple(histo)

        for string in strs:
            key = generate_key(string)
            if key in freq_anagrams:
                freq_anagrams[key].append(string)
            else:
                freq_anagrams[key] = [string]

        return list(freq_anagrams.values())
        