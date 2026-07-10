class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        def backtrack(path):
            if len(path)==len(nums):
                a.append(path[:])
                return
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return a