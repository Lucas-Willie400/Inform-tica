#Questão 1:
# def saudacao(nome):
#     return(f"Oi {nome}, seja bem-vindo(a)")
# print(saudacao("Luna"))

# Questão 2:
# def numero(a):
#     if a % 2 == 0:
#         return("número par")
#     else:
#         return("número ímpar")
# print(numero(int(input("digite um número: "))))

# Questão 3:
# def comparar(a,b):
#     if a>b:
#         return(f"{a} é maior")
#     elif b>a:
#         return(f"{b} é maior")
#     elif a==b:
#         return(f"{a} é igual a {b}")
# print(comparar(int(input("digite um número: ")), int(input("digite outro número: "))))

#Questão 4:
# n = int(input("Digite um número: "))
# for i in range(1, 11):
#     print(n*i)

# Questão 5
# n =10
# while n >=1:
#     n-=1
#     if n ==0:
#         print(0)
#         print("Explosão.")
#     else:
#         print(n)

#Questão 6:
# def media (notas):
#     for i in notas

#Questão 7:
# def fatorial(n):
#     resultado = 1
#     contador = n
#     while contador >= 1:
#         resultado *= contador
#         contador -= 1
#     return resultado
# numero = 5
# print(f"O fatorial de {numero} é {fatorial(numero)}")

#Questão 8:


# Questão 9:
# import random

# numero = random.randint(1, 20)
# numero_digitado = int(input("digite um número: "))
# if numero == numero_digitado:
#     print("você acertou!")
# elif numero > numero_digitado:
#     print("o número é maior")
# else:
#     print("o número é menor")
# print(numero)

#Questão 10:
# n =int(input("Digite um número"))
# pares_soma = 0
# for i in range(1,n):
#     if i%2 == 0:
#         pares_soma += i
# print(pares_soma)

#Questão 11:
def calculadora(a,b,operacao):
    if operacao =="+":
        return(a +b)
    elif operacao =="-":
        return(a - b)
    elif operacao =="*":
        return(a  * b)
    elif operacao =="/":
        return(a / b)
    elif b ==0:
        return("Erro, não dá pra dividir por zero")
print(calculadora(4,2,"+"))
print(calculadora(4,2,"-"))
print(calculadora(4,2,"*"))
print(calculadora(4,2,"/"))
