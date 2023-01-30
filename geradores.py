"""substituindo um for que travaria a memoria
por um gerador, que reproduz a mesma coisa quase que
sem consumir memoria"""
def a():
    n = 0
    while True:
        n+=1
        yield n

for i in a():
    print(i)

#yield from argumento é uma boa também!