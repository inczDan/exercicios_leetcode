#https://leetcode.com/problems/maximum-gap/
nums = [1,1,1,5,5,5]

def gap(nums):
    duplicado = []
    unicos = []
    nums = sorted(nums)
    if len(nums)<2:
        return 0
    else:    
        for i in nums:
            if i not in unicos:
                unicos.append(i)
            else:
                duplicado.append(i)
        maxi = max(unicos)
        copia = unicos
        copia.remove(max(copia))
        second_max = max(copia)
        result = maxi - second_max
        print(result)
        return result
gap(nums)
            
#0-------------------------
def maximumGap(nums):
    if len(nums)<2:
        return 0
    nums=sorted(nums)
    max=0
    for i in range(len(nums)-1):
        if abs(nums[i]-nums[i+1])>max:
            max=abs(nums[i]-nums[i+1])
    return max
maximumGap(nums)