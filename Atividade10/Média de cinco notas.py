soma = 0
for i in range(1, 6):
 nota = float(input(f'Digite a {i}ª nota: '))
 soma += nota
media = soma / 5
print(f'Média do aluno: {media:.2f}')
if media >= 7:
 print('Aluno aprovado')
else:
 print('Aluno reprovado')
