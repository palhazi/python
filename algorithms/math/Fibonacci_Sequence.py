# Fibonacci Sequence

if __name__ == '__main__':
    f = [0, 1]
    index1=0
    index2=1
    fibonacci_len = 18 # Lenght of Fibonacci Sequence
    for n in range(fibonacci_len):
        val = f[index1+n]+f[index2+n]
        f.append(val)
    f.pop(0)
    print (f)

""""
A Fibonacci-sorozat egy olyan számsorozat, amelyet az olasz matematikus, 
Leonardo Fibonacci alkotott meg a 13. században. Ez a sorozat úgy alakul, hogy minden szám az előző kettő összege. 
A sorozat az alábbi módon kezdődik:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Ahol az első két szám 0 és 1. Az azt követő számokat úgy kapjuk, hogy mindig hozzáadjuk az előző két számot. 
Például, 0+1=1, 1+1=2, 1+2=3, 2+3=5, és így tovább.

A Fibonacci-sorozatnak számos alkalmazása van a matematikában és a természettudományokban, 
beleértve a számítógépes algoritmusokat, a grafikát és a biológiai modellalkotást. 
Ezen kívül megjelenik a művészetben és az építészetben is, ahol gyakran kapcsolatba hozzák az aranymetszéssel."""