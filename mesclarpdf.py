import PyPDF2 #Biblioteca que permite manipular pdfs
import os #Biblioteca que permite manipular arquivos de computador, ler arquivos de uma pasta etc

merger = PyPDF2.PdfMerger() #Cria uma variavel para a função de Mesclar PDF

lista_arquivos = os.listdir("arquivos") #Cria uma lista de todos os arquivos que estão na pasta arquivos
lista_arquivos.sort() #Ordena os arquivos
print(lista_arquivos)   

for arquivo in lista_arquivos: #Percorre todos os arquivos da lista arquivos
    if ".pdf" in arquivo: #Verifica se o arquivo é um PDF
        merger.append(f"arquivos/{arquivo}") 
    
merger.write('PDF Final.pdf') #Escreve um novo PDF mesclando todos os outros.