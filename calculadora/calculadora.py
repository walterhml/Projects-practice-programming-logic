import math

def calculadora(opr, n1, n2):
    if opr == '+':
        return n1 + n2
    elif opr == '-':
        return n1 - n2
    elif opr == '*':
        return n1 * n2
    elif opr == '/':
        if n2 == 0:
            return "Error, divisão por zero"
        else:
            return n1 / n2
        
    else:
        return "operação invalida!"
    
    
print('Calculadora Simples - Desafio Simples:')
print('Operação disponiveis: +, -, *, /')

opr = input('Digite a operação que dejesa fazer: ')
n1 = (float(input('Digite o primeiro numero: ')))
n2 = (float(input('Digite o segundo numero: ')))

result = calculadora(opr, n1, n2)
print('Resultado: ', result)


