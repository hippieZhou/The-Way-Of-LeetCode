class Solution:
    # def combine(self, n: int, k: int) -> list:
    #     return [[]] if k == 0 else [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

    def combine(self, n: int, k: int) -> list:
        from itertools import combinations
        return list(combinations(range(1, n+1), k))
