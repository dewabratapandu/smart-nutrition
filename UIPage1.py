from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from misc import Title, addButton, addLabel, addLineEdit, BottomLayout

class UIPage1():
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Smart Nutrition Box")

        self.widget = QWidget(MainWindow)
        mainLayout = QVBoxLayout()
        
        self.title = Title()
        mainLayout.addWidget(self.title)

        self.Button = QPushButton('Mulai Hitung\nNutrisi Makanan')
        self.Button.setFont(QFont('SansSerif', 20))
        self.Button.setFixedWidth(300)
        mainLayout.addWidget(self.Button, alignment=Qt.AlignCenter)
        
        self.widget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.widget)