class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current=0
        max_altitude=0
        for i in gain:
            current+=i
            if current>max_altitude:
                max_altitude=current
        return max_altitude