def ducci_sequence(*ns):
    while True:
        yield ns
        ns = tuple(abs(ns[i - 1] - ns[i]) for i in range(len(ns)))

def ducci(*ns):
    known = set()
    for ns in ducci_sequence(*ns):
        print(ns)
        if ns in known or set(ns) == {0}:
            break
        known.add(ns)
    return len(known) + 1

print(ducci(0, 653, 1854, 4063), "steps")

"""
A Ducci-sorozat egy számteoretikai sorozat, amelyet egy négytagú számhalmazból generálnak, mindegyik számot kivonva a következő számból, ciklikusan. 
Az eljárást ismételjük a kapott négy számra, és így tovább. A Ducci-sorozatok nevét a matematikus Enrico Ducci-ról kapták.

A Ducci-sorozatok kiszámítására általánosan a következő algoritmust alkalmazzuk:

Kezdjünk egy (n1, n2, n3, n4) négytagú számsorral.
A következő sorozatot a |n1 - n2|, |n2 - n3|, |n3 - n4|, |n4 - n1| kifejezésekkel kapjuk.
Ismételjük a fenti lépést a kapott sorozattal.
Például, ha a kezdeti sorozat (0, 6, 9, 7), akkor a következő Ducci-sorozat (|0-6|, |6-9|, |9-7|, |7-0|), azaz (6, 3, 2, 7).

A Ducci-sorozatok vizsgálata során a matematikusok azt találták, hogy minden 4-tagnak véges számú lépés után elérkezik a (0, 0, 0, 0) sorozathoz, 
bármilyen kezdeti értékkel indítanak. A lépések száma és a sorozatok dinamikája azonban nagyon különböző lehet."""