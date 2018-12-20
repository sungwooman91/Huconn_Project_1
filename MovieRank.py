import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class Form(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("UI/ui_text1.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_1st(self):
        pixmap = QPixmap('image/drugking.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)

    @pyqtSlot()
    def slot_2nd(self):
        pixmap = QPixmap('image/aquaman.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)

    @pyqtSlot()
    def slot_3rd(self):
        pixmap = QPixmap('image/swingkids.jpg')
        pixmap_resized = pixmap.scaled(480, 240, Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_resized)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = Form()
    MyForm.show()
    app.exec_()