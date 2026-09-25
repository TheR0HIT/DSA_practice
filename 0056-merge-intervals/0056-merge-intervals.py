class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for start,end in intervals[1:]:
            left_end=result[-1][1]
            if start<=left_end:
                result[-1][1]=max(left_end,end)
            else:
                result.append([start,end])
        return result