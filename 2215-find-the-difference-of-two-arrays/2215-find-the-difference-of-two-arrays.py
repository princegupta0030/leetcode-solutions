class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1=set(nums1)
        s2=set(nums2)
        d1=[]
        d2=[]
        for n in s1:
            if n not in s2:
                d1.append(n)
        for n in s2:
            if n not in s1:
                d2.append(n)
        return [d1,d2]