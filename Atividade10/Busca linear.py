numeros = [10, 25, 8, 40, 15, 30, 7, 50, 12, 20]
busca = int(input('Digite o número que deseja buscar: '))
encontrado = False
for i in range(len(numeros)):
 if numeros[i] == busca:
  print(f'Número encontrado no índice {i}')
 encontrado = True
 break
if not encontrado:
 print('Número não encontrado.')
