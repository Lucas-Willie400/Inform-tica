# 1=soma
# 2=subtração
# 3=multiplicação
# 4=divisão

from operacoes import*
import emoji
while True:
    print("Quer realizar uma operação? ")
    ope=int(input("Digite um número para escolher a operação: "))
    x=int(input("Agora, digite um número da conta: "))
    y=int(input("Digite o outro número: "))

    if ope==0:
        break
    elif ope==1:
        print(soma(x,y))
        print(emoji.emojize(':thumbs_up:'))

    elif ope==2:
        print(sub(x,y))
        print(emoji.emojize(':thumbs_up:'))

    elif ope==3:
        print(multi(x,y))
        print(emoji.emojize(':thumbs_up:'))

    elif ope==4:
        print(div(x,y))
        print(emoji.emojize(':thumbs_up:'))


