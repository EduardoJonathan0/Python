div = float(input("Qual o valor de sua divida: "))
juros = float(input("E seu juros mensal: ")) / 100
valor_mensal = float(input("E o seu valor mensal: "))
total = 0
parcelas = 0
jurot = 0
while total <= div:
    total = total + valor_mensal
    parcelas += 1
    jurot = parcelas + juros
    print(total)
    print(juros * valor_mensal)
    print(parcelas)
