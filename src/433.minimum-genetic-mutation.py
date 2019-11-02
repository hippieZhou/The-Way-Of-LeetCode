import collections


class Solution:
    def validChange(self, start: str, end: str):
        changes = 0
        for i in range(len(end)):
            if start[i] != end[i]:
                changes += 1
        return changes == 1

    def minMutation(self, start: str, end: str, bank: list) -> int:
        queue = collections.deque()
        queue.append([start, start, 0])
        while queue:
            current, previous, num_steps = queue.popleft()
            if current == end:
                return num_steps
            for s in bank:
                if self.validChange(current, s) and s != previous:
                    queue.append([s, current, num_steps+1])
        return -1
