############################################
#CREANDO UN MARCO DE INTERFAZ 
############################################
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

############################################
class Ventana(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setWindowTitle("Ventana prueba")
        self.setGeometry(100,100,500,500)
        self.show()
        
############################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())
    
    
    