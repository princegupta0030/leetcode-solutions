class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=len(nums)
        a=(nums[l-1]-1)*(nums[l-2]-1)
        b=(nums[0]-1)*(nums[1]-1)
        return max(a,b)