total = 0
preco = 0
cod = int(input("Qual seu codigo: "))
while cod > 0:
    if cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1
    elif cod == 3:
        preco = 4
    else:
        print("Codigo invalido")
    continue
Qntd = float(input("Qual a quantidade do produto: "))
total = Qntd * preco
cod = int(input("Qual o codigo: "))
print("total= R$% 2f" % total)
