numeros = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
busca = int(input('Digite o número desejado: '))
inicio = 0
fim = len(numeros) - 1
encontrado = False
while inicio <= fim:
 meio = (inicio + fim) // 2
 if numeros[meio] == busca:
  print(f'Número encontrado no índice {meio}')
  encontrado = True
  break
 elif numeros[meio] < busca:
  inicio = meio + 1
 else:
  fim = meio - 1
if not encontrado:
 print('Número não encontrado.')
