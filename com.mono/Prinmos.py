def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(n, "es divisor de ", num, " por lo tanto no es primo, tiene un divisor el puñetero")
            return False
    print("Es primo")
    return True

    es_primo(7)
