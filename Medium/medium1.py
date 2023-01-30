#https://leetcode.com/problems/find-all-duplicates-in-an-array/

#Solução IDE
nums = [4,3,2,7,8,2,3,1]
def dupli(nums):
    duplicado = []
    unicos = []
    for i in nums:
        if i not in unicos:
            unicos.append(i)
        else:
            duplicado.append(i)
    print (duplicado)
    return duplicado
dupli(nums)
#--------------------- solução leetcode

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupli = set()
        unicos = set()
        for i in nums:
            if i not in unicos:
                unicos.add(i)
            else:
                dupli.add(i)
        return dupli