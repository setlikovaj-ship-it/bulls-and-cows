import random


DIGITS_COUNT = 4


def uvodni_text():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)


def vygeneruj_cislo():
    cisla = list("0123456789")
    random.shuffle(cisla)

    if cisla[0] == "0":
        for i in range(1, len(cisla)):
            if cisla[i] != "0":
                cisla[0], cisla[i] = cisla[i], cisla[0]
                break

    return "".join(cisla[:DIGITS_COUNT])


def validuj_vstup(vstup):
    if not vstup.isdigit():
        print("Invalid input: not a number.")
        return False

    if len(vstup) != DIGITS_COUNT:
        print("Invalid input: wrong length.")
        return False

    if vstup[0] == "0":
        print("Invalid input: number starts with zero.")
        return False

    if len(set(vstup)) != DIGITS_COUNT:
        print("Invalid input: duplicate digits.")
        return False

    return True


def spocitej_bulls_cows(tajne, tip):
    bulls = 0
    cows = 0

    for i in range(DIGITS_COUNT):
        if tip[i] == tajne[i]:
            bulls += 1
        elif tip[i] in tajne:
            cows += 1

    return bulls, cows


def vypis_vysledek(bulls, cows):
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_text}, {cows} {cow_text}")


def hra():
    uvodni_text()
    tajne_cislo = vygeneruj_cislo()
    pokusy = 0

    while True:
        tip = input("Enter a number: ")
        print("-" * 47)

        if not validuj_vstup(tip):
            continue

        pokusy += 1
        bulls, cows = spocitej_bulls_cows(tajne_cislo, tip)
        vypis_vysledek(bulls, cows)
        print("-" * 47)

        if bulls == DIGITS_COUNT:
            print("Correct, you've guessed the right number")
            print(f"in {pokusy} guesses!")
            print("-" * 47)
            print("That's amazing!")
            break


if __name__ == "__main__":
    hra()

