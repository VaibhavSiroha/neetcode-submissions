class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size=len(numbers)
        l=0
        r=size-1
        while True:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>=target:
                r -= 1
            elif numbers[l]+numbers[r]<=target:
                l += 1