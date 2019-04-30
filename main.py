import sys, logging, traceback
from core import runUpdater
from PyQt5.QtWidgets import QApplication
from Qt.gui import Ui_MainWindow
from Qt.logic import MainWindow

# Logs errors on crash
def except_hook(type_, value, trace_back):
    logging.basicConfig(filename='crash.log',filemode="w",level=logging.DEBUG)
    logging.exception("".join(traceback.format_exception(type_, value, trace_back)))
    QApplication.quit()

sys.excepthook = except_hook
#-------------------

# Starts main loop
runUpdater()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
#-------------------