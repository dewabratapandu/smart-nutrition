from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def Title():
    title = QLabel('Smart Nutrion Box')
    font = QFont('SansSerif', 27); font.setUnderline(True)
    title.setFont(font)
    title.setAlignment(Qt.AlignHCenter)
    return title

def addLabel(text, fontsize=20):
    label = QLabel(text)
    label.setFont(QFont('SansSerif', fontsize))
    return label

def addButton(text, fontsize=20):
    button = QPushButton(text)
    button.setFont(QFont('SansSerif', fontsize))
    button.setFixedWidth(300)
    return button

def addLineEdit(fontsize=20, width=50):
    lineedit = QLineEdit()
    lineedit.setFont(QFont('SansSerif', fontsize))
    lineedit.setFixedWidth(width)
    return lineedit

def BottomLayout(self):
    self.bottomLayout = QHBoxLayout()
    self.backButton = addButton("Kembali")
    self.bottomLayout.addWidget(self.backButton)
    self.nextButton = addButton("Lanjut")
    self.bottomLayout.addWidget(self.nextButton)