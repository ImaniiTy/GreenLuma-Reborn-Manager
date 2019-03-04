import sys
from PyQt5.QtWidgets import QApplication
from Qt.gui import Ui_MainWindow
from Qt.logic import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())