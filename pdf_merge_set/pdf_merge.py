import os
import sys
import shutil
import PyPDF2
from shutil import copyfile
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog

#FUNÇÕES DO BOTÃO MERGE
def pdf_merge():

    # merge dos arquivos na pasta "./arquivos"
    merger = PyPDF2.PdfMerger()
    arquivos = os.listdir("./arquivos")
    arquivos.sort()
    print(arquivos)

   #abre os arquivos dentro da pasta arquivo read only para fazer um apend
    for arquivo in arquivos:
        if arquivo.endswith(".pdf"):
            with open(os.path.join("./arquivos", arquivo), "rb") as arquivo_pdf:
                merger.append(arquivo_pdf)

    merger.write("PDF Final.pdf")
    salvar_arquivo()
    mostrar_alerta_merge()
    limpar_pasta_arquivos()
    print("Merge concluído")

def limpar_pasta_arquivos():

    arquivos = os.listdir("./arquivos")
    # Limpar a pasta 'arquivos'
    if os.path.exists('./arquivos'):
        for f in arquivos:
            try:
                os.remove(os.path.join("./arquivos", f))
            except:
                print("Erro ao deletar")

    # Abrir o PDF Final read only e remover da pasta
    pdf_final = "PDF Final.pdf"

    try:
        with open(pdf_final, "rb"):
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

    # Verifica se a pasta "arquivos" existe e a cria se não existir
    diretorio_arquivos = "arquivos"
    if not os.path.exists(diretorio_arquivos):
        os.makedirs(diretorio_arquivos)

    arquivo_carregado, _ = QFileDialog.getOpenFileNames(None, 'Selecionar Arquivos PDF', '', 'Arquivos PDF (*.pdf);;Todos os Arquivos (*)')

    if not arquivo_carregado:
        print("Nenhum arquivo selecionado.")
        return
    
    for caminho_arquivo in arquivo_carregado:
        nome_arquivo = os.path.basename(caminho_arquivo)
        destination_path = os.path.join('arquivos', nome_arquivo)
        copyfile(caminho_arquivo, destination_path)
        print(f'Arquivo "{nome_arquivo}" salvo em "./arquivos".')

    pixmap = QPixmap('pdf_merge_set/icon_pdf.png')  # Substitua 'imagem.png' pelo caminho da sua imagem
    lbl_image.setPixmap(pixmap)
    lbl_image.setScaledContents(True)  # Redimensionar a imagem para o tamanho do QLabel

    # Verifica se a imagem pdf está visível
    if lbl_image.isHidden():
        lbl_image.show()   # Mostra a imagem
    else:
        lbl_image.hide()  # Esconde a imagem
  
    # Verifica se a imagem da logo está visível
    if lbl_imagetitulo.isVisible():
        lbl_imagetitulo.hide()  # Esconde a imagem
    else:
        lbl_imagetitulo.show()  # Mostra a imagem

    QTimer.singleShot(2000, mostrar_lbl_alerta_carregado)

def mostrar_lbl_alerta_carregado():
    #puxa a lista de arquivos ordenada
    arquivos = os.listdir("./arquivos")
    arquivos.sort()
    texto = ' | '.join(arquivos)

    #mostra a lista de arquivos que o usuario carregou pra ele mesmo verificar
    lbl_alerta_carregado.setText("Arquivos: {}".format(texto))
    lbl_alerta_carregado.adjustSize()
    print(lbl_alerta_carregado)

    texto = lbl_alerta_carregado.text()
    max_length = 30
    print(texto)

    if len(texto) > max_length:
        texto_truncado = texto[:max_length] + "..."
        lbl_alerta_carregado.setText(texto_truncado)

# --------------------------------------- Estrutura do executável --------------------------------------------------
app = QApplication(sys.argv)

#set da janela
janela = QWidget()
janela.resize(300, 330)
janela.setWindowTitle("PDF Merge")

#set icon da barra de titulo
icon = QIcon("pdf_merge_set/logobarratitulo.png")
janela.setWindowIcon(icon)
                     
#set do título
lbl_imagetitulo = QLabel(janela, objectName="titulo")
logo = QPixmap("pdf_merge_set/logo.png")
lbl_imagetitulo.setPixmap(logo)
lbl_imagetitulo.move(0, 50)
lbl_imagetitulo.setScaledContents(True)


#set do botão de carregar arquivo
carregar_arquivoButton = QPushButton("Carregar Arquivo", janela, objectName="buttons")
carregar_arquivoButton.setGeometry(20, 210, 120, 50)
carregar_arquivoButton.clicked.connect(carregar_arquivo)

#set da imagem pdf
lbl_image = QLabel(janela, objectName="lbl_image")
lbl_image.move(0, 50)
lbl_image.hide()

#set do alerta_merge de arquivos carregados
lbl_alerta_carregado = QLabel(janela, objectName="lbl_alerta_carregado")
lbl_alerta_carregado.move(0, 170)

#set do botão de merge arquivo
merge_arquivoButton = QPushButton("Juntar PDF", janela, objectName="buttons")
merge_arquivoButton.setGeometry(160, 210, 120, 50)
merge_arquivoButton.clicked.connect(pdf_merge)

#set do alerta_merge de merge concluído
alerta_merge = QLabel(janela, objectName="lbl_alerta_merge")
alerta_merge.move(0, 270)

#aplicação de estilos no executável
with open("pdf_merge_set/styles.css", "r") as file:
    app.setStyleSheet(file.read())

janela.show()
app.exec()