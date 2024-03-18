from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Botão para Exibir Imagem')
        self.setGeometry(100, 100, 400, 300)

        # Criando um botão
        self.btn_show_image = QPushButton('Mostrar Imagem', self)
        self.btn_show_image.setGeometry(150, 50, 100, 30)

        # Conectando o sinal clicked do botão à função showImage
        self.btn_show_image.clicked.connect(self.showImage)

        # Criando um QLabel para exibir a imagem
        self.lbl_image = QLabel(self)
        self.lbl_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Criando um layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.btn_show_image)
        layout.addWidget(self.lbl_image)

        # # Criando um widget central para a janela principal
        # central_widget = QWidget()
        # central_widget.setLayout(layout)
        # self.setCentralWidget(central_widget)

    def showImage(self):
        # Carregando a imagem
        pixmap = QPixmap('icon_pdf.png')  # Substitua 'imagem.png' pelo caminho da sua imagem
        self.lbl_image.setPixmap(pixmap)
        self.lbl_image.setScaledContents(True)  # Redimensionar a imagem para o tamanho do QLabel

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
