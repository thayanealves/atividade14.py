# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

n1= float(input("digite a nota 1"))
n2= float(input("digite a nota 2"))
n3= float(input("digite a nota 3"))

#calcule a média
media = (n1+n2+n3)/3
print (f"amédia é {media}")

#aprovacao
if media >=7:
    print ("aprovado")
elif 5<= media <7:
    print ("recuperação")
elif media <5:
    print("reprovado")