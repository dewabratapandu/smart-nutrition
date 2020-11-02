import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UIPage1 import UIPage1
from UIPage2 import UIPage2
from UIPage3 import UIPage3
from UIPage4 import UIPage4
from UIPage5 import UIPage5
from UIPage6 import UIPage6
import misc
from crop_traybox import cropTraybox
from hitung_sisa import estimation, error_cal
from testing import testing

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.beratA = ''; self.beratB = ''; self.beratC = ''; self.beratD = ''
        self.sisaA = ''; self.sisaB = ''; self.sisaC = ''; self.sisaD = ''
        self.A = ''; self.B = ''; self.C = ''; self.D = ''
        self.imBefore = ''; self.imAfter = ''
        self.estimasiSisa = []; self.errorEstimasi = []
        self.page_1 = UIPage1()
        self.page_2 = UIPage2()
        self.page_3 = UIPage3()
        self.page_4 = UIPage4()
        self.page_5 = UIPage5()
        self.page_6 = UIPage6()
        self.Page1()

    def Page1(self):
        self.page_1.setupUI(self)
        self.page_1.Button.clicked.connect(self.Page2)
        self.show()
    
    def Page2(self):
        self.page_2.setupUI(self)
        self.page_2.backButton.clicked.connect(self.Page1)
        self.page_2.nextButton.clicked.connect(self.Page3)
        self.show()

    def Page3(self):
        self.imBefore = self.page_2.imagePath
        self.croppedImg = cropTraybox(self.imBefore)
        self.A = testing(self.croppedImg[0])
        self.B = testing(self.croppedImg[1])
        self.C = testing(self.croppedImg[2])
        self.D = testing(self.croppedImg[3])

        self.page_3.setupUI(self)
        self.page_3.backButton.clicked.connect(self.Page2)
        self.page_3.nextButton.clicked.connect(self.Page4)
        self.show()

    def Page4(self):
        self.imAfter = self.page_3.imagePath
        self.page_4.setupUI(self)
        self.page_4.setValue(self.A, self.B, self.C, self.D)
        self.page_4.backButton.clicked.connect(self.Page3)
        self.page_4.nextButton.clicked.connect(self.Page5)
        self.show()

    def hitung_sisa(self, file_before, file_after, weight_bef, weight_sisa):
        list_estimation = estimation(file_before, file_after, weight_bef)
        self.estimasiSisa = list_estimation
        self.errorEstimasi = error_cal(weight_sisa,list_estimation)

    def Page5(self):
        self.page_5.setupUI(self)
        self.page_5.setValue(self.A, self.B, self.C, self.D)

        self.beratA = self.page_4.lineedit1_bef.text()
        self.beratB = self.page_4.lineedit2_bef.text()
        self.beratC = self.page_4.lineedit3_bef.text()
        self.beratD = self.page_4.lineedit4_bef.text()
        self.sisaA = self.page_4.lineedit1_aft.text()
        self.sisaB = self.page_4.lineedit2_aft.text()
        self.sisaC = self.page_4.lineedit3_aft.text()
        self.sisaD = self.page_4.lineedit4_aft.text()

        weight_bef = [int(self.beratA), int(self.beratB), int(self.beratC), int(self.beratD)]
        weight_sisa =[int(self.sisaA), int(self.sisaB), int(self.sisaC), int(self.sisaD)]
        self.hitung_sisa(self.imBefore, self.imAfter, weight_bef, weight_sisa)

        self.page_5.lineedit1a.setText(self.sisaA)
        self.page_5.lineedit2a.setText(self.sisaB)
        self.page_5.lineedit3a.setText(self.sisaC)
        self.page_5.lineedit4a.setText(self.sisaD)
        self.page_5.lineedit1b.setText(str(self.estimasiSisa[0]))
        self.page_5.lineedit2b.setText(str(self.estimasiSisa[1]))
        self.page_5.lineedit3b.setText(str(self.estimasiSisa[2]))
        self.page_5.lineedit4b.setText(str(self.estimasiSisa[3]))
        self.page_5.lineedit1c.setText(str(self.errorEstimasi[0]))
        self.page_5.lineedit2c.setText(str(self.errorEstimasi[1]))
        self.page_5.lineedit3c.setText(str(self.errorEstimasi[2]))
        self.page_5.lineedit4c.setText(str(self.errorEstimasi[3]))

        self.page_5.backButton.clicked.connect(self.Page4)
        self.page_5.nextButton.clicked.connect(self.Page6a)
        self.show()

    def Page6a(self):
        self.page_6.setJudul(self.A, self.sisaA)
        self.page_6.setupUI(self)
        self.page_6.setNutrisi(self.A, self.sisaA)
        self.page_6.backButton.clicked.connect(self.Page5)
        self.page_6.nextButton.clicked.connect(self.Page6b)
        self.show()

    def Page6b(self):
        self.page_6.setJudul(self.B, self.sisaB)
        self.page_6.setupUI(self)
        self.page_6.setNutrisi(self.B, self.sisaB)
        self.page_6.backButton.clicked.connect(self.Page6a)
        self.page_6.nextButton.clicked.connect(self.Page6c)
        self.show()

    def Page6c(self):
        self.page_6.setJudul(self.C, self.sisaC)
        self.page_6.setupUI(self)
        self.page_6.setNutrisi(self.C, self.sisaC)
        self.page_6.backButton.clicked.connect(self.Page6b)
        self.page_6.nextButton.clicked.connect(self.Page6d)
        self.show()

    def Page6d(self):
        self.page_6.setJudul(self.D, self.sisaD)
        self.page_6.setupUI(self)
        self.page_6.setNutrisi(self.D, self.sisaD)
        self.page_6.backButton.clicked.connect(self.Page6c)
        self.page_6.nextButton.clicked.connect(self.close)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())