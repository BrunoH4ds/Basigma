def linha():
  print("-"*30)
  
Dicionario = {
  '6' : 'f',
  '5': 'e',
  '50':'l',
  '1': 'i',
  '26': 'z',
  'mm': '2000',
  'r':'18'
}
print("Welcome to Basigma")
linha()
linha()

codigo = input("digite o codigo: ")
codigo2=codigo.lower()
codigodecodificado = ""
linha()

i = 0

while i < len(codigo):
  if codigo2[i:i+2] in Dicionario:
    codigodecodificado += Dicionario[codigo2[i:i+2]]
    i += 2
    
  elif codigo2[i] in Dicionario:
    codigodecodificado += Dicionario[codigo2[i]]
    i += 1
  
  else:
    print("-Código não encontrado.")
    linha()
    break

codigodecodificado = codigodecodificado.replace("200018", " 2018")

print("Codigo decodificado:", codigodecodificado)
linha()
print("Obrigado por usar o Programa!")
print("deselvovido Por: BrunoHads")
