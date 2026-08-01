class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=sum(nums)
        etotal=n*(n+1)//2
        return etotal-total