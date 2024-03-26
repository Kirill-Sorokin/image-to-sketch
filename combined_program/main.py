# python3 -m install PyQt5 if necessary (in terminal)
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from ImgDDLabel import ImgDDLabel
from sketcher import Sketcher, webcam

class ImageToSketch:
    def __init__(self):
        self.img = None
        self.sketch = None
        self.main()

    def main(self):
        try:
            app = QtWidgets.QApplication(sys.argv)
            self.ui = uic.loadUi("window.ui")
            self.original = ImgDDLabel()
            self.ui.layout2.addWidget(self.original)
            self.ui.convertBtn.clicked.connect(self.convert)
            self.ui.camBtn.clicked.connect(webcam)
            self.ui.show()
            app.exec_()
        except Exception as ex:
            print(ex)
        
    def convert(self):
        try:
            print("converting to sketch now...")
            self.img = self.original.imagefile
            if self.img:
                Sketcher(self.img)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Completed Conversion")
                msg.setWindowTitle("Information")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Error in Sketching\nPlease select any image to Sketch.")
                msg.setWindowTitle("Error Occurred")
                msg.exec_()
        except Exception as ex:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Error)
            msg.setText("Incomplete Conversion")
            msg.setInformativeText(str(ex))
            msg.setWindowTitle("Error")
            msg.exec_()
            print(ex)

if __name__ == "__main__":
    import sys
    ImageToSketch()
