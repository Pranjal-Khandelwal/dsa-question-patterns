from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size=len(nums)
        start=end=0
        res=[]
        dq=deque()

        while(end<size):
            while dq and nums[dq[-1]] < nums[end]:
                dq.pop()
        
            dq.append(end)

        #Until window size not reached
            if end-start+1<k:
                end+=1
        
        #Window size reached we need to calculate answer
            elif end-start+1==k:
                res.append(nums[dq[0]])

                if dq[0]==start:
                    dq.popleft()
                end+=1
                start+=1
        
        return res