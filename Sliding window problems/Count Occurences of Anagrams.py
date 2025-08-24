#User function Template for python3
from collections import defaultdict

class Solution:
	def search(self,pat, txt):
		size=len(txt)
		k=len(pat)
		start=end=0
		ans=0
		store_dict = defaultdict(int)
		for patn in pat:
			store_dict[patn]+=1
			
		count=len(store_dict)
		
		while(end<size):
			store_dict[txt[end]]-=1
			if store_dict[txt[end]]==0:
				count-=1
				if end-start+1<k:
					end+=1
				elif end-start+1==k:
					if count==0:
						ans+=1
				store_dict[txt[start]]+=1
				
				if  store_dict[txt[start]]==1:
					count+=1
					
				end+=1
				start+=1
				
		return ans