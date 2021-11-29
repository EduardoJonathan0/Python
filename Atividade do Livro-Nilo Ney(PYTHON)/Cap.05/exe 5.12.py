deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal:"))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print("Saldo do mês %d é de R$%5.2f." % (mes, saldo))
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo - deposito:.8.2f}%8.2f.")
