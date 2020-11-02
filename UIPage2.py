from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from misc import Title, addButton, addLabel, addLineEdit, BottomLayout

class UIPage2():
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Smart Nutrition Box")
        
        self.widget = QWidget(MainWindow)
        self.mainLayout = QVBoxLayout()

        self.title = Title()
        self.mainLayout.addWidget(self.title)
        self.text1 = addLabel("Upload Gambar Makanan Sebelum Dimakan!\nContoh:", 18)
        self.mainLayout.addWidget(self.text1)
        
        self.labelImage = QLabel(self.widget)
        pixmap = QPixmap("tes1.jpg")
        pixmap = pixmap.scaled(350, 350, Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)
        self.mainLayout.addWidget(self.labelImage, alignment=Qt.AlignCenter)

        self.Button = QPushButton('Upload')
        self.Button.setFont(QFont('SansSerif', 20))
        self.Button.setFixedWidth(300)
        self.Button.clicked.connect(self.getImage)
        self.mainLayout.addWidget(self.Button, alignment=Qt.AlignCenter)

        BottomLayout(self)
        self.nextButton.setEnabled(False)
        self.mainLayout.addLayout(self.bottomLayout)

        self.widget.setLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.widget)

    def getImage(self, MainWindow):
        fname = QFileDialog.getOpenFileName(self.widget, 'Open file', 'home/pandu', "Image files (*.jpg *.gif)")
        self.imagePath = fname[0]
        pixmap = QPixmap(self.imagePath)
        pixmap = pixmap.scaled(350, 350, Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)
        
        self.text1.setText("Gambar Makanan Sebelum Dimakan Berhasil Diupload")

        self.nextButton.setEnabled(True)
        self.mainLayout.update()