class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        max_water=0
        r=len(height)-1
        while l<r:
            c_width=r-l
            c_height=min(height[l],height[r])
            c_area=c_width*c_height

            max_water=max(max_water,c_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_water