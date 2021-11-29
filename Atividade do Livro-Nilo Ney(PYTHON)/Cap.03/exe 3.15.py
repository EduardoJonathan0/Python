Qntd_cigarros = int(input("Quantidade de cigarros por dias: "))
anos_de_fumo = int(input("Quantidade de cigarros por ano: ")) #1 dia = 24 hrs
reduzindo_mnts = anos_de_fumo * 365 * Qntd_cigarros * 10  #10 minutos, 1 minuto equivale 60 segundo entao ele fuma 60 minutos
reduzindo_dias = reduzindo_mnts / (24 * 60)
print(f'A redução de tempo de vida da pessoa é de {reduzindo_dias:.2f}')
