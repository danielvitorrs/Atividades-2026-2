numeros = [8, 3, 5, 1, 9, 2]
n = len(numeros)
for i in range(n - 1):
 for j in range(n - 1 - i):
  if numeros[j] > numeros[j + 1]:
   numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print('Lista ordenada:', numeros)