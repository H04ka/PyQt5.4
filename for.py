from PyQt5 import QtWidgets
import ks, ks1

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ks.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.perehod)

    def perehod(self):
        vt.show()

class VtoroeWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ks1.Ui_Vtor()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.perehod2)

    def perehod2(self):
        a = float(self.ui.lineEdit.text())
        window.ui.label.setText(str(a+(a*0.15)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = VtoroeWindow()
    window.show()
    sys.exit(app.exec_())
