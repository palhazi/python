def generate_lucky_number_sequence(end):
    
    #create a list of all odd numbers up to the final number
    sequence = [*range(1, end+1, 2)]

    #remove every xth number from the list where x = the nth element of the sequence
    n = 1
    while len(sequence) > sequence[n]:
        number_to_delete = sequence[n]
        del sequence[number_to_delete-1::number_to_delete]
        n = n + 1

    return sequence

print(generate_lucky_number_sequence(int(input("Please enter the upper bound of the lucky number sequence: "))))

"""""
Ez a Python program a szerencsés számok sorozatát generálja. 
A szerencsés számok egy számteoretikai szekvencia, amelyet az alábbi algoritmus generál:

1. Kezdünk az 1-től kezdődő páratlan számok sorozatával.
2. Az első szám (ami mindig 1) a "szerencsés".
3. Töröljük minden n-edik számot a listából, ahol n a legutóbbi "szerencsés" szám.
4. Az első töröletlen szám a következő "szerencsés" szám.
5. Ismételjük a 3-4. lépést, amíg el nem érjük a lista végét.

A fenti Python kódban a 'generate_lucky_number_sequence' függvény előállítja 
a szerencsés számok sorozatát az 1-től a megadott számig. 
A végén a függvény visszaadja a szerencsés számok listáját.

Például, ha 20-at adunk meg bemenetként, a program a következő szerencsés számokat adja vissza:

[1, 3, 7, 9, 13, 15, 19]"""""