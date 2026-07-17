class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        def backtrack(r,combination,start):
            if r==0:
                arr.append(list(combination))
                return
            if r<0:
                return
            for i in range (start,len(candidates)):
                combination.append(candidates[i])
                backtrack(r-candidates[i],combination,i)
                combination.pop()
        backtrack(target,[],0)
        return arr