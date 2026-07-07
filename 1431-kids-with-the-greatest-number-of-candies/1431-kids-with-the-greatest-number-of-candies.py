class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m_candies=max(candies)
        r=[]
        for c in candies:
            r.append(c+extraCandies>=m_candies)
        return r