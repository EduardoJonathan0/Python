n = int(input('Digite somente numeros primos: '))
c = p = 0
while c < n:
    if p % 2 != 0 and p != 1 and p != 0:
        print(f'Primo: {p}')
        c += 1
    elif p == 2:
        print(f'Primo: {p}')
        c += 1
    p += 1
