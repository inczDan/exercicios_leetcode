#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
nums = [1,3,6,10,12,15]
total = []
def valor(nums):
    for i in nums:
        if i % 6 == 0:
            total.append(i)
            media = sum(total) // len(total)
    print(media)
valor(nums)


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = []
        for i in nums:
            if i % 6 == 0:
                total.append(i)
        return sum(total) // len(total) if len(total)>0 else 0