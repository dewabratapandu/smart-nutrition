from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from misc import Title, addButton, addLabel, addLineEdit, BottomLayout

class UIPage5():
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Smart Nutrition Box")
        
        self.widget = QWidget(MainWindow)
        mainLayout = QVBoxLayout()

        self.title = Title()
        mainLayout.addWidget(self.title)
        
        self.groupBox = QGroupBox("Prediksi Berat Sisa Makanan")
        self.groupBox.setFont(QFont('SansSerif', 18))
        self.groupBox.setAlignment(Qt.AlignHCenter)
        gridLayout = QGridLayout()
        self.text0a = addLabel("Berat Asli (gr)", 15)
        self.text0b = addLabel("Berat Prediksi (gr)", 15)
        self.text0c = addLabel("Berat Error (%)", 15)
        gridLayout.addWidget(self.text0a, 0,1)
        gridLayout.addWidget(self.text0b, 0,2)
        gridLayout.addWidget(self.text0c, 0,3)
        # Baris A
        self.text1 = addLabel("A", 18)
        gridLayout.addWidget(self.text1, 1,0)
        self.lineedit1a = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit1a, 1,1)
        self.lineedit1b = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit1b, 1,2)
        self.lineedit1c = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit1c, 1,3)
        # Baris B
        self.text2 = addLabel("B", 18)
        gridLayout.addWidget(self.text2, 2,0)
        self.lineedit2a = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit2a, 2,1)
        self.lineedit2b = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit2b, 2,2)
        self.lineedit2c = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit2c, 2,3)
        # Baris C
        self.text3 = addLabel("C", 18)
        gridLayout.addWidget(self.text3, 3,0)
        self.lineedit3a = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit3a, 3,1)
        self.lineedit3b = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit3b, 3,2)
        self.lineedit3c = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit3c, 3,3)
        # Baris D
        self.text4 = addLabel("D", 18)
        gridLayout.addWidget(self.text4, 4,0)
        self.lineedit4a = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit4a, 4,1)
        self.lineedit4b = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit4b, 4,2)
        self.lineedit4c = addLineEdit(18, 180)
        gridLayout.addWidget(self.lineedit4c, 4,3)

        self.groupBox.setLayout(gridLayout)
        mainLayout.addWidget(self.groupBox)

        BottomLayout(self)
        mainLayout.addLayout(self.bottomLayout)

        self.widget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.widget)

    def setValue(self, A, B, C, D):
        self.text1.setText(A)
        self.text2.setText(B)
        self.text3.setText(C)
        self.text4.setText(D)