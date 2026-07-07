class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        outlist=sorted(seen.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for key,value in outlist[:k]:
            ans.append(key)
        return ans