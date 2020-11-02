from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from misc import Title, addButton, addLabel, addLineEdit, BottomLayout

class UIPage4():
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Smart Nutrition Box")
        
        self.widget = QWidget(MainWindow)
        mainLayout = QVBoxLayout()

        self.title = Title()
        mainLayout.addWidget(self.title)
        
        self.groupBox = QGroupBox("Masukkan Berat Sisa untuk Setiap Jenis Makanan")
        self.groupBox.setFont(QFont('SansSerif', 18))
        gridLayout = QGridLayout()
        # Baris Pertama
        self.text0 = addLabel("Jenis Makanan", 18)
        gridLayout.addWidget(self.text0, 0,0)
        self.text0 = addLabel("Berat Awal", 18)
        gridLayout.addWidget(self.text0, 0,1)
        self.text0 = addLabel("Berat Sisa", 18)
        gridLayout.addWidget(self.text0, 0,3)
        # Baris A
        self.text1 = addLabel("A", 18)
        gridLayout.addWidget(self.text1, 1,0)
        self.lineedit1_bef = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit1_bef, 1,1)
        self.text1gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text1gr, 1,2)
        self.lineedit1_aft = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit1_aft, 1,3)
        self.text1gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text1gr, 1,4)
        # Baris B
        self.text2 = addLabel("B", 18)
        gridLayout.addWidget(self.text2, 2,0)
        self.lineedit2_bef = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit2_bef, 2,1)
        self.text2gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text2gr, 2,2)
        self.lineedit2_aft = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit2_aft, 2,3)
        self.text2gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text2gr, 2,4)
        # Baris C
        self.text3 = addLabel("C", 18)
        gridLayout.addWidget(self.text3, 3,0)
        self.lineedit3_bef = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit3_bef, 3,1)
        self.text3gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text3gr, 3,2)
        self.lineedit3_aft = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit3_aft, 3,3)
        self.text3gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text3gr, 3,4)
        # Baris D
        self.text4 = addLabel("A", 18)
        gridLayout.addWidget(self.text4, 4,0)
        self.lineedit4_bef = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit4_bef, 4,1)
        self.text4gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text4gr, 4,2)
        self.lineedit4_aft = addLineEdit(18, 100)
        gridLayout.addWidget(self.lineedit4_aft, 4,3)
        self.text4gr = addLabel("gram", 18)
        gridLayout.addWidget(self.text4gr, 4,4)

        self.groupBox.setLayout(gridLayout)
        mainLayout.addWidget(self.groupBox)

        BottomLayout(self)
        self.nextButton.setEnabled(False)
        mainLayout.addLayout(self.bottomLayout)

        self.lineedit1_bef.textChanged.connect(self.enableNextButton)
        self.lineedit2_bef.textChanged.connect(self.enableNextButton)
        self.lineedit3_bef.textChanged.connect(self.enableNextButton)
        self.lineedit4_bef.textChanged.connect(self.enableNextButton)
        self.lineedit1_aft.textChanged.connect(self.enableNextButton)
        self.lineedit2_aft.textChanged.connect(self.enableNextButton)
        self.lineedit3_aft.textChanged.connect(self.enableNextButton)
        self.lineedit4_aft.textChanged.connect(self.enableNextButton)

        self.widget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.widget)

    def enableNextButton(self):
        cond1 = len(self.lineedit1_bef.text())
        cond2 = len(self.lineedit2_bef.text())
        cond3 = len(self.lineedit3_bef.text())
        cond4 = len(self.lineedit4_bef.text())
        cond5 = len(self.lineedit1_aft.text())
        cond6 = len(self.lineedit2_aft.text())
        cond7 = len(self.lineedit3_aft.text())
        cond8 = len(self.lineedit4_aft.text())
        if(cond1>0 and cond2>0 and cond3>0 and cond4>0 and cond5>0 and cond6>0 and cond7>0 and cond8>0):
            self.nextButton.setEnabled(True)

    def setValue(self, A, B, C, D):
        self.text1.setText(A)
        self.text2.setText(B)
        self.text3.setText(C)
        self.text4.setText(D)