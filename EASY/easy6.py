#https://leetcode.com/problems/palindrome-number/description/

#solução IDE
def palio(x:int):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


#0-------------------Solução Leetcode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False