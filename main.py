from PyQt4 import QtGui
import sys
import view #from generated file

class SynthApp(QtGui.QMainWindow, view.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    form = SynthApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
