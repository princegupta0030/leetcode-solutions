class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        for i in range (1,102):
            ans=k*i
            if ans not in nums:
                return ans
