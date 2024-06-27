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

codigodecifradolista= []

print("Welcome to Basigma")
linha()
linha()

vezes=int(input("Quantos caracteres o codigo tem? "))
linha()

vezes=vezes+1

for i in range(1, vezes):
  codigo=input(f'Digite o {i}° código ? ')
  codigo=codigo.lower()
  linha()
  
  if codigo in Dicionario:
    codigodecifradolista.append(Dicionario[codigo])
  
  else:
    print('-Código não encontrado')
    linha()
  
codigodecifrado="".join(codigodecifradolista)
codigodecifrado2 = codigodecifrado.replace('200018',' 2018')
print("O codigo decifrado foi:", codigodecifrado2)
linha()

print("Obrigado por usar o Programa!")
print("deselvovido Por: BrunoHads")
