class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        j=0
        s=0 #this is sum initial
        l=float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                l=min(l,i-j+1)
                s-=nums[j]
                j+=1
        if l!=float('inf'):
            return l
        else:
            return 0