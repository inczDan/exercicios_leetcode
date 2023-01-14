#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
def maisDoces(doces, extras):
    bolso = 0
    lista = []
    for i in range(len(doces)):
        if doces[i] >= bolso:
            lista.append('True')
            bolso = doces[i]
        else:
            bolso = doces[i]
            lista.append('False')
    print(lista, i)
maisDoces([2,3,5,1,3], 3)

#----------------------------
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bolso = max(candies)
        lista = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= bolso: 
                lista.append(True)
            else:
                lista.append(False)
        return lista
