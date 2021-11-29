valor_da_casa = int(input('Qual valor da casa que deseja a comprar: '))
salario = int(input('Qual seu salario: '))
qntd_de_anos = int(input('Quantos anos a pagar: '))
meses = qntd_de_anos * 12
valor_da_prestacao = valor_da_casa / meses
if valor_da_prestacao > salario * 0.3:
    print("Desculpe você não pode obter o emprestimo da casa")
else:
    print(f'O valor da prestação: R${valor_da_prestacao:.2f} está OK.')
