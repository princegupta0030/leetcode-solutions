class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n_map={}
        for i,n in enumerate(nums):
            c=target-n
            if c in n_map:
                return[n_map[c],i]
            n_map[n]=i
        return []
        