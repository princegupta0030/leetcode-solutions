class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r=[]
        c={}
        for n in nums:
            c[n]=c.get(n,0)+1
        def backtrack(path):
            if len(path)==len(nums):
                r.append(list(path))
                return
            for n in c:
                if c[n]>0:
                    path.append(n)
                    c[n]-=1
                    backtrack(path)
                    c[n]+=1
                    path.pop()
        backtrack([])
        return r