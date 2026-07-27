class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for n in nums:
            if n>a:
                b=a
                a=n
            elif n>b:
                b=n
        return (a-1)*(b-1)