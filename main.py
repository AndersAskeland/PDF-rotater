##################################################################################
##                                                                              ##
## Title: PDF rotater                                                            ##
##                                                                              ##
## What: Main file (currently).                                      ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QSize

# UI files
from UI.ui_mainwindow import Ui_MainWindow


##################################################################
## 2 - SETTING AND CONSTANTS                                    ##
##################################################################




##################################################################
## 3 - Main                                                    ##
##################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load generated UI files
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title
        self.setWindowTitle("PDF rotater")

        # Set window size
        window_size = QSize(1100, 720)
        self.resize(window_size)
        self.setMinimumSize(window_size)



##################################################################
## 4 - Run                                                    ##
##################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Show GUI window
    window = MainWindow()
    window.show()


    sys.exit(app.exec_())       
