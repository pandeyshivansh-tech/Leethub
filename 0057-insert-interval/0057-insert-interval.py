class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        s = intervals[0][0]
        e = intervals[0][1]
        n = len(intervals)
        v = []
        for i in range(1, n):
            if e>=intervals[i][0]:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
            else:
                v.append([s, e])
                s = intervals[i][0]
                e = intervals[i][1]
        v.append([s, e])
        return v