"""Collatz sequence.

@author: Pablo Trinidad <github.com/pablotrinidad>
"""


def collatz(n):
    """Sequence generation."""
    l = []
    while n > 1:
        l.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    l.append(n)
    return l

n = int(input("Enter an integer n to compute the Collatz sequence: "))
print(collatz(n))

"""
A Collatz-sorozat (más néven 3n+1 tétel, Collatz probléma, Ulam tétel, 
Kakukktojás tétel, Hasse algoritmus, Thwaites tétel) egy számteoretikai algoritmus, 
amelyet Lothar Collatz német matematikus javasolt 1937-ben.

A Collatz-sorozat a következő módon generálódik:
Kezdd bármely pozitív egész számmal.
Ha a szám páros, oszd el kettővel.
Ha a szám páratlan, szorozd meg hárommal, majd adj hozzá egyet.
Ismételd meg a 2. és 3. lépéseket a kapott számmal.
A sorozat véget ér, ha a szám eléri az 1-et.
Például, ha a kezdeti szám 6, akkor a Collatz-sorozat a következő: 6, 3, 10, 5, 16, 8, 4, 2, 1.

A Collatz-tétel azt állítja, hogy bármely pozitív egész számból kiindulva a fenti lépések 
végül mindig az 1-hez vezetnek. Habár a tételnek számos számítógépes tesztje igazolta az igazságát, 
matematikailag még nem sikerült bizonyítani vagy cáfolni, tehát a Collatz probléma továbbra 
is nyitott kérdés a matematikában."""
