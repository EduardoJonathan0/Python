while True:
    print("Menu\n1 - Adição\n2 - Substração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    print("_"*40)
    opcao = int(input("Escolha uma opção do menu: "))
    if opcao == 5:
        break
    elif 1 <= opcao <= 5:
        print("_"*30)
        number = int(input("Qual tabuada deseja realizar: "))
        print("_"*30)
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f'{number} + {x} = {number + x}')
            elif opcao == 2:
                print(f'{number} - {x} = {number +- x}')
            elif opcao == 3:
                print(f'{number} * {x} = {number * x}')
            elif opcao == 4:
                print(f'{number} / {x} = {number / x}')
            x = x + 1
        else:
            print("Opção inválida")
