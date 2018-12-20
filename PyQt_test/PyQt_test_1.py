import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)        ## QApplicaion instance create

## Label Create
# label = QLabel("Hello")
# label.show()

## Button Create
btn = QPushButton("Push Push Babe")
btn.show()

app.exec_()                         ## Event loop create
