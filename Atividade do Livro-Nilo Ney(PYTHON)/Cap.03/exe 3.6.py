materia1 = int(input("Qual a primeira nota do aluno: "))
materia2 = int(input("Qual a Segunda nota do aluno: "))
materia3 = int(input("Qual a Terceira nota do aluno: "))
result = int(materia1 + materia2 + materia3 / 2)
if result > 7:
    print("Aprovado")
elif result <= 7:
    print("Reprovado")
