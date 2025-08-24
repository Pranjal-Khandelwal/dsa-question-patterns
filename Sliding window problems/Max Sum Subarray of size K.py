class Solution:
    def maxSubarraySum(self, arr, k):
        size=len(arr)
        total_sum=0
        max_sum=0
        
        start=0
        end=0
        
        while(end<size):
            total_sum+=arr[end]
            
            if end-start+1<k:
                end+=1
            
            elif end-start+1==k:
                max_sum=max(max_sum,total_sum)
                total_sum-=arr[start]
                end+=1
                start+=1
        
        return max_sum