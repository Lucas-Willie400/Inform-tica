ListaNotas=[1,9,8,20]
media=sum(ListaNotas)/len(ListaNotas)
def calcular_media(ListaNotas):
    return media
print(calcular_media(ListaNotas))

def verificar_situacao(media):
    if media >=7:
        return("Aprovado")
    elif media ==5 or media<6.9:
        return("Recuperação")
    elif media <5:
        return("Reprovado")
print(verificar_situacao(media))