from random import randint

los = randint(1,10)
odp = -1
i = 0

print("Zgadnij liczbę z przedziału 1-10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Niestety, wylosowana liczba jest mniejsza od twojej")
    elif odp < los:
        print("Niestety, wylosowana liczba jest większa od twojej")

print("Brawo, zgadłeś!")
print("Ilość prób: ",i)
