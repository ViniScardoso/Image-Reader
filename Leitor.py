from tkinter import Button, filedialog
from PIL import Image
import time
from pytesseract import pytesseract
import tkinter as tk

# Define path to tessaract.exe
path_to_tesseract = r'D:\Arquivos de Programas\Tesseract\tesseract.exe'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract


def extrairTexto():
	arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=(
		 ("jpg files", "*.jpg"),("png files", "*.png"),("all files", "*.*")))

	img = Image.open(arquivo)

	text = pytesseract.image_to_string(img)

	try:
		with open('TextoDaImagem.txt', 'w', encoding='utf-8') as archive:
			archive.write(text)

		texto_resultado["text"] = "Sucesso, verifique o arquivo TextoDaImagem.txt na sua pasta de trabalho"
	
	except:
		texto_resultado["text"] = "Erro ao salvar o arquivo" 
		
		

window = tk.Tk()

window.title("Leitor de Imagens")

texto_titulo = tk.Label(window, text="Leitor de Imagens", font=("Calibri", 15))
texto_titulo.grid(column=1, row=0)

texto_orientacao = tk.Label(
	window, text="Selecione o arquivo de imagem desejado", font=("Calibri", 12))
texto_orientacao.grid(column=1, row=2)

botao = Button(window, text="Selecionar arquivo", command=extrairTexto)
botao.grid(column=1, row=4)

texto_resultado = tk.Label(window, text="", font=("Calibri", 12))
texto_resultado.grid(column=1, row=6)

window.mainloop()
