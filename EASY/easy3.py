#https://leetcode.com/problems/defanging-an-ip-address/

#solução leetcode
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")