class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size=len(nums)
        start=0
        end=0
        dq=deque()
        res=[]

        while end<size:
            while  len(dq)>0 and dq[-1]<nums[end]:
                dq.pop()
            dq.append(nums[end])

            if end-start+1<k:
                end+=1
            elif end-start+1==k:
                res.append(dq[0])

                if dq[0]==nums[start]:
                    dq.popleft()
                start+=1
                end+=1

        return res