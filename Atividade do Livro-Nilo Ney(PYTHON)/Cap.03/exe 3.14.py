carro_km = int(input('Quantos quilometros foram pecorridos pelo carro? '))
carro_dias = int(input('Quantos dias o carro foi alugado?'))
preco = int(60)
km = int(0.15)
pagamento = carro_km * carro_dias + preco
print(f'O total a pagar é de: {pagamento}')
