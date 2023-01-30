#https://leetcode.com/problems/smallest-even-multiple/description/

#solução leetcode
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
     if  n %2 == 0:                 
         return n                                
     return n * 2
        