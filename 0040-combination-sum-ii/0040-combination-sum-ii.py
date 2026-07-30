class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        r=[]
        def backtrack(start, target, arr):
            if target==0:
                r.append(arr[:])
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break

                arr.append(candidates[i])
                backtrack(i+1,target-candidates[i],arr)
                arr.pop()
        backtrack(0,target,[])
        return r