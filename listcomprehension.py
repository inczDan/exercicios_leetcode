#aqui era um treino pra refatorar

with open('file.txt', 'r') as t:
    text = t.read()
# def func(text):
#     """Retornar dict
#     dict[char] = quantidade em que char aparece em text"""
#     chars = []
#     quantidade = []
#     for c in text:
#         if not c in chars:
#             chars.append(c)
#             quantidade.append(1)
#         else:
#             indice = chars.index(c)
#             quantidade[indice]+=1
#     d = {}
#     for i in range(len(chars)):
#         d[chars[i]] = quantidade[i]
#     return d
# print(func(text))

#fazendo com listcomprehension
# def func2(text):
#     chars = list({ c for c in text })
#     quantidade = [ text.count(i) for i in text ]
#     d = {}
#     for i in range(len(chars)):
#         d[chars[i]] = quantidade[i]
#     return d
# print(func2(text))

#melhorando um pouco mais, a parte do dict
def func3(text):
    chars = list({c for c in text})
    quantidade = [(i, text.count(i)) for i in text]
    return dict(quantidade)
print(func3(text))
#se nao convertermos p dict, isso irá retornar um 'dict' falso
#falso pq é de tuplas na real.

#matando mais ainda o codigo, ta maluco!
def func4(text):
    return dict([(i,text.count(i)) for i in set(text)])
print(func4(text))
"""Convertemos o texto diretamente pra set,
ai nao precisamos mais do indice"""

# dict comprehension, que loucura!
def func5(text):
    return {i: text.count(i) for i in set(text)}
print(func5(text))

#também poderiamos importar o counter do collections
from collections import Counter
def func6(text):
    return Counter(text)
    