class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        c=sum(nums[:k])
        max_s=c
        for i in range (k,len(nums)):
            c+=nums[i]-nums[i-k]
            if c>max_s:
                max_s=c
        return float(max_s)/k