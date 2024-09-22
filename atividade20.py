# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.

soma = 0
for numero in range (2, 101, 2):
    soma += numero 
print("a soma de todos os números pares de 1 a 100 é:", soma)