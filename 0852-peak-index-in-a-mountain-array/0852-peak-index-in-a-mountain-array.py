class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=0
        r=len(arr)-1
        while l<r:
            c=(l+r)//2
            if arr[c]<arr[c+1]:
                l=c+1
            else:
                r=c
        return l