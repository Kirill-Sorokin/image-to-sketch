from PyQt5 import QtCore, QtWidgets, QtGui, uic

class ImgDDLabel(QtWidgets.QLabel):
    def __init(self, lineedit = None):
        super().__init()
        self.setAcceptDrops(True)
        self.lineedit = lineedit
        self.imagefile = None
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText("Drag the Image here")
        self.setStyleSheet('''background-color: rgb(255, 255, 255): 
                           color: rgb(39, 86, 115);
                           border-radius:10px;
                           font: 75 9pt "MS Shell Dlg 2";''')
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            image_path = event.mimeData().urls()[0].toLocalFile()
            self.imagefile = image_path
            self.set_image()
            self.set_image(image_path)
            event.accept()
        else:
            event.ignore()

    def mouseDoubleClickEvent(self, event):
        print("Mouse Double Click Event Triggered")
        try:
            fname = QtWidgets.QFileDialog.getopenFileName(self, 'Select Image to Sketch',
                                                          '.',"Image Files (*.png *.bmp *.jpg)")
            if fname:
                self.imagefile = fname[0]
                self.set_image(self.imagefile)
        except Exception as ex:print(ex)

    def set_image(self, image_path):
        try:
            image_path = QtGui.QPixmap(image_path)
            image_path = image_path.scaled(QtCore.QSize(self.width(),
                                                        self.height()),
                                                        QtCore.Qt.KeepAspectRatio,
                                                        QtCore.Qt.SmoothTransformation)
            self.setPixmap(image_path)
        except Exception as ex:print(ex)

__name__ == "__main__":
import sys
print('running')
try:
    app = QtWidgets.QApplication(sys.argv)
    ui = uic.loadUi('window.ui')
    imgddlabel = ImgDDLabel()
    ui.l1.addWidget(imgddlabel)
    ui.show()
    app.exec_()
except Exception as ex:print(ex)
print('running finished')





                           