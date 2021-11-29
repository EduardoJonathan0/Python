choose = input("1)Digite 1 para Somar\n2)Digite 2 para Subtrair\n3)Digite 3 para Multiplicar\n4)Digite 4 para Dividir\n")

num0 = int(input("Insira o primeiro número: "))
num1 = int(input("Insira o segundo número: "))
result1 = num0 + num1
result2 = num0 - num1
result3 = num0 * num1
result4 = num0 / num1

if choose == '1':
    print(f'O resultado de {num0} + {num1} é = {result1}')
elif choose == '2':
    print(f'O resultado de {num0} - {num1} é = {result2}')
elif choose == '3':
    print(f'O resultado de {num0} * {num1} é = {result3}')
elif choose == '4':
    print(f'O resultado de {num0} / {num1} é = {result4}')
