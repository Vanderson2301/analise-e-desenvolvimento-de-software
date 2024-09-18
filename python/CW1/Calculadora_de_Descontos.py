valor = print = float(input("Qual o valor da compra? "))
desconto = print = float(input("Qual o valor do desconto? "))

def desconto_correto(desconto):
    if desconto < 1:
        print ("Desconto inválido")
    elif desconto > 100:
        print  ("Desconto inválido")
    else:
        return desconto



print ("O valor da compra foi", valor)
print ("O desconto foi de ", desconto)
print ("O valor final da compra foi", )