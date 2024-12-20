from PyQt5 import QtWidgets, QtCore
import time
import osn_proga
import Zastavka



class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Zastavka.Ui_Form()
        self.ui.setupUi(self)

class zad(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = osn_proga.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.doAction)


    def doAction(self):
        a = 0
        while a < 100:
            a += 5
            time.sleep(0.10)
            self.ui.progressBar.setValue(a)
            self.u
        else:
            zas.close()
            window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowFlag(QtCore.Qt.Drawer)
    zas = zad()
    zas.setWindowFlag(QtCore.Qt.SplashScreen)
    zas.show()
    sys.exit(app.exec_())