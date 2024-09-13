#Apresentar os valores
respostas = [7.5,8.0,6.5,3.0,4.4,9.8]

#Função regular para calcular média

def media_regular(respostas):
    total = sum(respostas) #Para somar todos os valores  da lista
    media = total / len(respostas) #O Len é para contar a quantiadde de elementos que há na lista
    return media

#Arredondar respostas
arrendondar_media = lambda media: round(media,2) # O round vai fazer com que o  valor seja arredondado para duas casas decimais. A função lambda  é uma função anônima, ou seja, não tem nome.

#calcular media
media = media_regular(respostas)
media_arredondada = arrendondar_media(media)

#Verificar aprovação
situacao = "Aprovado" if media >= 7 else "Reprovado"

print("Respostas das pessoas:", respostas)
print("Média das notas:", media_arredondada)
print("As pessoas estão:", situacao)