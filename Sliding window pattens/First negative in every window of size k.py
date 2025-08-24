#User function Template for python3
class Solution:
    def firstNegInt(self, arr, k): 
        size = len(arr)
        my_list = []  # will hold indices of negative numbers
        res = []
        
        start = 0
        end = 0
        
        while end < size:
            # if current element is negative, add its index to list
            if arr[end] < 0:
                my_list.append(end)
            
            # check window size
            if end - start + 1 < k:
                end += 1
            elif end - start + 1 == k:
                # append first negative in window
                if len(my_list) == 0:
                    res.append(0)
                else:
                    res.append(arr[my_list[0]])
                
                # remove element going out of window
                if my_list and my_list[0] == start:
                    my_list.pop(0)
                
                start += 1
                end += 1
        
        return res