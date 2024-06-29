from tkinter import *
def descriptografar():
  Dicionario = {
    ' ' : ' ',
    '6' : 'F',
    '5': 'e',
    '50':'l',
    '1': 'i',
    '26': 'z',
    'mm': '2000',
    'r':'18'
  }

  codigo = codigo1.get().lower()
  codigodecodificado = ""

  i = 0

  while i < len(codigo):
      if codigo[i:i+2] in Dicionario:
        codigodecodificado += Dicionario[codigo[i:i+2]]
        i += 2
    
      elif codigo[i] in Dicionario:
        codigodecodificado += Dicionario[codigo[i]]
        i += 1
      else:
         break

  codigodecodificado = codigodecodificado.replace("200018", "2018")

  resultados_janela.config(text=f"Resultado: {codigodecodificado}")
  

janela = Tk()
janela.title("Basigma")
janela.geometry("1000x200+300+150")
janela.resizable(False,False)
janela.iconbitmap("")
janela["bg"]= 'gray'

texto= Label(
 janela,
 text="Bem-vindo a Basigma",
 font=("arial", 18),
 bg= 'gray',
 fg= 'white'
)
texto.place(
 x=325,
 y=25,
 width=345,
 height=30
)

texto= Label(
 janela,
 text="Digite o Codigo Criptografado:",
 font=("arial", 18), 
 bg= 'gray',
 fg= 'white'
)
texto.place(
  x=5,
  y=80,
  width=335,
  height=28,
)

codigo1= Entry(
  janela,
  font=("arial", 18),
  bd=0 
)
codigo1.place(
  x=345,
  y=80,
  width=350,
  height=28
)

botao= Button(
  janela,
  text="Inicie a Descriptografia",
  command= descriptografar,
  font=("arial", 18),
  bg= 'gray',
  fg= 'white',
  bd= 0.5,
  highlightthickness= 0
)
botao.place(
  x=710,
  y=80,
  width=275,
  height=28
)

resultados_janela= Label(
  janela,
  text="Aguardando Descriptografia... ",
  font=("arial", 18),
  bg= 'gray',
  fg= 'white',
  relief= 'flat'
)
resultados_janela.place(
  x=345,
  y=125,
  width=345,
  height=50
)

janela.mainloop()
