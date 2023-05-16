from math import sqrt

"""
this function calculate euler totien function
"""
def eulerTotienFunction(n):
	if n == 1:
		return 1
	result = 1
	temp = n
	for i in range(2,int(sqrt(n))+10):
		if (temp % i == 0):
			j = 0
			while(temp % i == 0):
				j += 1
				temp //= i
			result = result * (i**(j-1)) * (i-1)
	if temp == n:
		return n-1
	return result


"""""
Euler totient (φ) függvénye egy aritmetikai függvény, amely megszámolja a pozitív egészeket, 
amelyek relatíve prímek egy n számmal, és kisebbek n-nél. Két szám relatíve prím, ha a legnagyobb közös osztójuk 1.

Például φ(9) = 6, mert a 9-nél kisebb pozitív egészek közül a 1, 2, 4, 5, 7 és 8 relatíve prím a 9-cel.

Euler totient függvényének néhány fontos tulajdonsága:

- Ha p prímszám, akkor φ(p) = p-1, mert egy prímszám minden kisebb pozitív egész számmal relatíve prím.
- Ha n = p*q, ahol p és q különböző prímszámok, akkor φ(n) = (p-1)*(q-1).
- Euler totient függvénye additív: ha n és m relatíve prímek, akkor φ(nm) = φ(n)*φ(m).

Euler totient függvényét sok helyen alkalmazzák a számelméletben, különösen a csoportelméletben és a kriptográfiában. """""


