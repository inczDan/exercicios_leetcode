#https://leetcode.com/problems/palindrome-number/description/
def palio(x:int):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


#0-------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False