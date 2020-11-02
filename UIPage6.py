from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from misc import Title, addButton, addLabel, addLineEdit, BottomLayout
from hitung_nutrisi import *

class UIPage6():
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Smart Nutrition Box")
        
        self.widget = QWidget(MainWindow)
        mainLayout = QVBoxLayout()

        self.title = Title()
        mainLayout.addWidget(self.title)
        
        self.groupBox = QGroupBox("Jenis Makanan: "+ self.jenis + "; Berat Sisa: "+ self.berat+" gram")
        self.groupBox.setFont(QFont('SansSerif', 18))
        self.groupBox.setAlignment(Qt.AlignHCenter)
        gridLayout = QGridLayout()
        # Baris A
        self.text1 = addLabel("Kalori", 18)
        gridLayout.addWidget(self.text1, 0,0)
        self.lineedit1 = addLineEdit(18, 150)
        gridLayout.addWidget(self.lineedit1, 0,1)
        self.text1 = addLabel("kkal", 18)
        gridLayout.addWidget(self.text1, 0,2)
        # Baris B
        self.text2 = addLabel("Karbohidrat", 18)
        gridLayout.addWidget(self.text2, 1,0)
        self.lineedit2 = addLineEdit(18, 150)
        gridLayout.addWidget(self.lineedit2, 1,1)
        self.text2 = addLabel("gram", 18)
        gridLayout.addWidget(self.text2, 1,2)
        # Baris C
        self.text3 = addLabel("Protein", 18)
        gridLayout.addWidget(self.text3, 2,0)
        self.lineedit3 = addLineEdit(18, 150)
        gridLayout.addWidget(self.lineedit3, 2,1)
        self.text3 = addLabel("gram", 18)
        gridLayout.addWidget(self.text3, 2,2)
        # Baris D
        self.text4 = addLabel("Lemak", 18)
        gridLayout.addWidget(self.text4, 3,0)
        self.lineedit4 = addLineEdit(18, 150)
        gridLayout.addWidget(self.lineedit4, 3,1)
        self.text4 = addLabel("gram", 18)
        gridLayout.addWidget(self.text4, 3,2)

        self.groupBox.setLayout(gridLayout)
        mainLayout.addWidget(self.groupBox)

        BottomLayout(self)
        mainLayout.addLayout(self.bottomLayout)

        self.widget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.widget)
        
    def setJudul(self, jenis, berat):
        self.jenis = jenis
        self.berat = berat

    def setNutrisi(self, jenis, sisa):
        self.lineedit1.setText(str(Kalori(jenis, sisa)))
        self.lineedit2.setText(str(Karbohidrat(jenis, sisa)))
        self.lineedit3.setText(str(Protein(jenis, sisa)))
        self.lineedit4.setText(str(Lemak(jenis, sisa)))