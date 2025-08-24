from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        size = len(arr)
        my_deque = deque()  # will hold indices of negative numbers
        res = []
        
        start = 0
        end = 0
        
        while end < size:
            # if current element is negative, add its index
            if arr[end] < 0:
                my_deque.append(end)
            
            # check window size
            if end - start + 1 < k:
                end += 1
            elif end - start + 1 == k:
                # append first negative in window
                if len(my_deque) == 0:
                    res.append(0)
                else:
                    res.append(arr[my_deque[0]])
                
                # remove element going out of window
                if my_deque and my_deque[0] == start:
                    my_deque.popleft()
                
                start += 1
                end += 1
        
        return res
