from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

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

  codigo = criptografado_Entry.get().lower()
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

  resultados_Textcase.insert(ttk.INSERT,codigodecodificado + "\n")
  

janela = ttk.Window()
janela.title("Basigma")
janela.geometry("1000x500+500+350")
janela.resizable(False,False)
style= Style(theme="solar")

texto= ttk.Frame(janela)
texto.pack(padx=10,pady=10,fill='both')
ttk.Label(texto, text= "Welcome to Basigma", font=('',18)).pack(padx=10,pady=10, fill='y')

criptografado= ttk.Frame(texto) 
criptografado.pack(padx=5,pady=5, fill='x')
criptografado_Label=ttk.Label(criptografado, text= "Digite o Texto Criptografado:",font=('',15)).pack(side=LEFT,padx=5,pady=5, fill='x')
criptografado_Entry= ttk.Entry(criptografado, font=("arial",12),)
criptografado_Entry.pack(padx=5,side=LEFT,fill="x", expand= True)
Descriptografia_buttom= ttk.Button(criptografado, text="Descriptografar",command=descriptografar, bootstyle=OUTLINE).pack(side=LEFT,padx=5)

resultados_janela= ttk.Frame(texto)
resultados_janela.pack(padx=10,fill='both')
resultados_Label=ttk.Label(resultados_janela,text="Texto Descriptografado:",font=("arial",15)).pack()
resultados_Textcase=ttk.Text(resultados_janela,font=("arial",12))
resultados_Textcase.pack(pady=10,fill='x')

janela.mainloop()
