# Recebe um número e operador.
# Mostra o resultado.
# elif = elseif c#
# Operadores - +, -, *, /.

print('Digite um valor:')
valor1 = int(input())

print('Digite um operador:')
operador = input()

print('Digite um segundo valor:')
valor2 =  int(input())

if operador == '+':
    resultado = valor1 + valor2
    print(resultado)
elif operador == '-':
    resultado = valor1 - valor2
    print(resultado)
elif operador == '*':
    resultado = valor1 * valor2
    print(resultado)
elif operador == '/':
    resultado = valor1 / valor2
    print(resultado)
else: print('Operador invalido')