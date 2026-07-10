class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        r=[intervals[0]]
        for i in range (len(intervals)):
            if intervals[i][0]<=r[-1][1]:
                r[-1][1]=max(r[-1][1],intervals[i][1])
            else:
                r.append(intervals[i])
        return r