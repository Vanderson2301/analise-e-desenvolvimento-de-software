#Coleta de Dados
print(f"O peso é em 'kg'")
peso = float(input("Quanto você pesa? "))
print(f"A altura é em 'm'")
altura = float(input("Qual sua altura?: "))

#Calculo
imc = (peso/altura**2)

#Resultado IMC

if imc <= 16.9:
 print("Você está muito abaixo do peso")
elif imc <= 18.4:
 print("Você está abaixo do peso") 
elif imc <= 24.9:
  print("Você está com o peso normal")
elif imc <= 29.9:
  print("Você está acima do peso")
elif imc <= 34.9:
  print("Você está em Obesidade de grau I")
elif imc <= 39.9:
   print("Você está em Obesidade de grau II")
else:
 print("Você está em Obesidade de grau III")