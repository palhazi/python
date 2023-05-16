def is_armstrong(n):
    # Konvertáljuk a számot stringgé, hogy megtudjuk, hány jegye van
    str_n = str(n)
    num_digits = len(str_n)

    # Számoljuk össze a számjegyek num_digits hatványait
    sum = 0
    for digit in str_n:
        sum += int(digit) ** num_digits

    # Ha a szám egyenlő a számjegyek hatványaival, akkor az Armstrong-szám
    return sum == n

# Listázzuk ki az összes Armstrong-számot 0 és 1000 között
for i in range(100000001):
    if is_armstrong(i):
        print(i)

"""
Egy pozitív egész számot Armstrong-számnak (vagy narcissisztikus számnak) nevezünk, ha a számjegyeinek számára emelt hatványok összege megegyezik a számmal.

Például a 3 jegyű Armstrong-számok:

153, mert 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
370, mert 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
371, mert 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
407, mert 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407
Ezt az összefüggést kiterjeszthetjük a több jegyű számokra is. Az n jegyű Armstrong-számokra érvényes, hogy a számjegyeinek n-edik hatványainak összege megegyezik a számmal.

Például a 4 jegyű Armstrong-számok:

1634, mert 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
A legkisebb Armstrong-szám 0, és nincs felső határ."""