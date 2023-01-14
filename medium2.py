#https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/
nums = [1,13,10,12,31]
inversao = []
def inverte(nums):
    n = len(nums)
    for i in range(0,n):
        nums.append(int(str(nums[i])[::-1]))
        print(len(set(nums)))
        return len(set(nums))
inverte(nums)

#---------------------
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))
