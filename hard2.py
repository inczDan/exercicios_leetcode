#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
nums1 = [1,3] 
nums2 = [2,5,4]
nums1+=nums2
nums1.sort()
tam = len(nums1)
if tam%2==1:
    print(nums1[((tam-1)//2)])
else:
    print((nums1[tam//2-1]+nums1[tam//2])/2)
