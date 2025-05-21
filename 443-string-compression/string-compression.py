from itertools import groupby
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []

        for char, group in groupby(chars):
            count = sum(1 for _ in group)
            result.append(char)
            if count > 1:
                result.extend(list(str(count)))

        chars[:] = result  # overwrite the original list
        return len(chars)
