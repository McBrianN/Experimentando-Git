############################################
#CREANDO UN MARCO DE INTERFAZ 
############################################
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QPixmap

############################################
class Ventana(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        self.setStyleSheet("background-color: #000000;")
    
    def inicializar_ui(self):
        self.setWindowTitle("Aprendiendo GIT - Window")
        self.setGeometry(100,100,500,500)
        self.contenido()
        self.adjustSize()
        self.show()
    
    def contenido(self):
        titulo = QLabel("EL DIABLOOOOOOO")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont("Times New Roman", 25))
        titulo.setStyleSheet("color: orange;")
        
        #imagen
        imagen = QLabel()
        pixmap = QPixmap("git.jpg")
        imagen.setPixmap(pixmap)
        imagen.setBaseSize(QSize(200,200))
        imagen.setScaledContents(True)
        imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        imagen.setStyleSheet("border: 2px solid purple;")    

        
        boton = QPushButton("SALIR")
        boton.setStyleSheet("background-color: grey; color: black; bold: true;")
        boton.setFont(QFont("Times New Roman", 25))
        boton.setFixedSize(100,50)
        
        
        #Agregamos el layout del texto y la imagen.
        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(imagen)
        layout.addWidget(boton,alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
     
############################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())
    
    
    