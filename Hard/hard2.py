#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

#solução IDE
nums1 = [1,3] 
nums2 = [2,5,4]
nums1+=nums2
nums1.sort()
tam = len(nums1)
if tam%2==1:
    print(nums1[((tam-1)//2)])
else:
    print((nums1[tam//2-1]+nums1[tam//2])/2)

#------------Solução leetcode

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            nums1+=nums2
            nums1.sort()
            tam = len(nums1)
            if tam%2==1:
                return(nums1[((tam-1)//2)])
            else:
                return((nums1[tam//2-1]+nums1[tam//2])/2)
