class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        m1 = set(nums)

        for num in m1:
            if num - 1 not in m1: 
                count = 1
                current = num

                while current + 1 in m1:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest