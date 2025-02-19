class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies) - extraCandies
        result = [False] * len(candies)

        for i, candy in enumerate(candies):
            if candy >= max_candies:
                result[i] = True
        return result



        