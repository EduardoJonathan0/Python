consumo_de_kwh = int(input("Quanto consome de kwh: "))
tipo_de_instalacoes = input("Qual o tipo da instalaçao: (R, C , I): ")
if tipo_de_instalacoes == "R" or "r":
    if consumo_de_kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_de_instalacoes == "C" or "c":
    if consumo_de_kwh <= 1000:
        preco = 0.60
    else:
        preco = 0.55
elif tipo_de_instalacoes == "I" or "i":
    if consumo_de_kwh >= 5000:
        preco = 0.60
    else:
        preco = 0.55
else:
    preco = 0
    print("Erro! Instalação desconhecida")
preco_a_pagar = consumo_de_kwh * preco
print(f'A sua instalação é {tipo_de_instalacoes} e seu valor a pagar é de: {preco_a_pagar}')
