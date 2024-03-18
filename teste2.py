import PyPDF2
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
import shutil
from shutil import copyfile
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

# FUNÇÕES DO BOTÃO MERGE
def pdf_merge():

    # merge dos arquivos na pasta "arquivos"

    merger = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir("arquivos")
    lista_arquivos.sort()
    print(lista_arquivos)

   #abre os arquivos dentro da pasta arquivo read only para fazer um apend

    for arquivo in lista_arquivos:
        if arquivo.endswith(".pdf"):
            with open(os.path.join("arquivos", arquivo), "rb") as arquivo_pdf:
                merger.append(arquivo_pdf)

    merger.write("PDF Final.pdf")

    salvar_arquivo()

    mostrar_alerta_merge()

    print("Merge concluído")

    # Limpar a pasta 'arquivos'
    if os.path.exists('arquivos'):
        for f in lista_arquivos:
            try:
                os.remove(os.path.join("arquivos", f))
                # print(os.path.join(current_directory, os.path.join("arquivos", f)))
                # os.remove(os.path.join(current_directory,  os.path.join("arquivos", f)))
            except:
                print("Erro ao deletar")

    # Abrir o PDF Final read only e remover da pasta
    pdf_final = "PDF Final.pdf"

    try:
        with open(pdf_final, "rb") as exclusão_pdf_final:
            pass
        os.remove(pdf_final)
        print(f"Arquivo PDF excluído com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo PDF não foi encontrado.")
    except:
        print(f"Ocorreu um erro ao excluir o arquivo PDF.")
    
def mostrar_alerta_merge():

    alerta_merge.setText("Merge Concluído")
    alerta_merge.adjustSize()

def salvar_arquivo():
     
    salvar_arquivo, _ = QFileDialog.getSaveFileName(directory='PDF Final.pdf', filter= 'Arquivos PDF (*.pdf);;Todos os Arquivos (*)')

    if salvar_arquivo:
       # Caminho do arquivo PDF original
        caminho_arquivo = 'PDF Final.pdf'

        try:
            # Copiar o arquivo PDF original para o destino selecionado pelo usuário
            shutil.copyfile(caminho_arquivo, salvar_arquivo)
            print("Cópia do PDF salva com sucesso em:", salvar_arquivo)
        except Exception as e:
            print("Erro ao salvar a cópia do PDF:", e)

#FUNÇÕES DO BOTÃO CARREGAR ARQUIVO
def carregar_arquivo():
    arquivo_carregado, _ = QFileDialog.getOpenFileNames(None, 'Selecionar Arquivos PDF', '', 'Arquivos PDF (*.pdf);;Todos os Arquivos (*)')

    if not arquivo_carregado:
        print("Nenhum arquivo selecionado.")
        return
    
    for caminho_arquivo in arquivo_carregado:
        nome_arquivo = os.path.basename(caminho_arquivo)
        destination_path = os.path.join('arquivos', nome_arquivo)
        copyfile(caminho_arquivo, destination_path)
        print(f'Arquivo "{nome_arquivo}" salvo em "arquivos".')

    pixmap = QPixmap('icon_pdf.png')  # Substitua 'imagem.png' pelo caminho da sua imagem
    lbl_image.setPixmap(pixmap)
    lbl_image.setScaledContents(True)  # Redimensionar a imagem para o tamanho do QLabel

    mostrar_alerta_carregado()

def mostrar_alerta_carregado():
    #puxa a lista de arquivos ordenada
    lista_arquivos = os.listdir("arquivos")
    lista_arquivos.sort()

    #mostra a lista de arquivos que o usuario carregou pra ele mesmo verificar
    alerta_carregado.setText("Arquivos carregados: {}".format(lista_arquivos))
    alerta_carregado.adjustSize()
    print(lista_arquivos)

# --------------------------------------- Estrutura do executável --------------------------------------------------
app = QApplication(sys.argv)

#set da janela
janela = QWidget()
janela.resize(300, 300)

#set do título
titulo = QLabel(janela)
titulo.move(120, 50)
titulo.setText("PDF Merge")

#set do botão de carregar arquivo
carregar_arquivoButton = QPushButton("Carregar Arquivo", janela)
carregar_arquivoButton.setGeometry(20, 210, 120, 50)
carregar_arquivoButton.clicked.connect(carregar_arquivo)

#set da imagem pdf
lbl_image = QLabel(janela)
lbl_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
lbl_image.setGeometry(120,110,50,50)

#set do alerta_merge de arquivos carregados
alerta_carregado = QLabel(janela)
alerta_carregado.setGeometry(75, 170, 300, 300)
alerta_carregado.setAlignment(Qt.AlignmentFlag.AlignCenter)

#set do botão de merge arquivo
merge_arquivoButton = QPushButton("Juntar PDF", janela)
merge_arquivoButton.setGeometry(160, 210, 120, 50)
merge_arquivoButton.clicked.connect(pdf_merge)

#set do alerta_merge de merge concluído
alerta_merge = QLabel(janela)
alerta_merge.move(105, 270)

janela.show()
app.exec()