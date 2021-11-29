ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
number = int(input('Insira um numero de 0 à 10: '))
if number <= 10:
    print(f'Você digitou: {ext[number]}')
