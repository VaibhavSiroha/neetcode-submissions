class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            seen[num]=i
        for i in range(len(nums)):
            a=target-nums[i]
            if a in seen and i!=seen[a]:
                return [i,seen[a]]