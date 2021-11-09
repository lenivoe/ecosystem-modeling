from PyQt5 import QtWidgets
from mainForm import MainForm

import sys

app = QtWidgets.QApplication([])
application = MainForm()
application.show()
 
sys.exit(app.exec())