class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest=min(nums)
        largest=max(nums)

        for i in range(1,smallest+1):
            if smallest%i==0 and largest%i==0:
                gcd=i
        return gcd

