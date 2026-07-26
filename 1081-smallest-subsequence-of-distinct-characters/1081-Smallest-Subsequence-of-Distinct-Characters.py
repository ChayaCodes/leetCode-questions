class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        1. create counter for frequncy of eny char in the string
        for any char:
            if the 
            if the first char in the current substring is bigger the the current char and it
        """
        not_saw_counter = Counter(s)
        res_sub_string = []
        chars_in = set()
        for c in s:
            not_saw_counter[c] -= 1
            if c in chars_in:
                continue
            while res_sub_string and res_sub_string[-1] > c and not_saw_counter[res_sub_string[-1]] > 0:
                chars_in.remove(res_sub_string.pop())
            res_sub_string.append(c)
            chars_in.add(c)


        return "".join(res_sub_string)
