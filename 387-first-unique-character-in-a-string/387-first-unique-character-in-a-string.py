class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, j in enumerate(s):
            d[j] = i if j not in d else 10 ** 5
        ans = min(d.values())
        return ans if ans < 10 ** 5 else -1