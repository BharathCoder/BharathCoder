from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs)
    super(MainWindow,self).__init__(*args, **kwargs)

    self.setWindowTitle("Mozarella Ashbadger")




app=QApplication(sys.argv)
app.exec_()
