import sys
import random 
from PySide6 import QtCore, QtWidgets, QtGui
from libsoundtouch import device, soundtouch_device



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.device = soundtouch_device('10.1.1.21')  # Manual configuration
        # self.device.select_source_aux()
        self.volume = self.device.volume()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button_plus = QtWidgets.QPushButton("+")
        self.button_minus = QtWidgets.QPushButton("-")
        self.text = QtWidgets.QLabel(str(self.volume.actual),
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_plus)
        self.layout.addWidget(self.button_minus)

        self.button_plus.clicked.connect(self.volumeUp)
        self.button_minus.clicked.connect(self.volumeDown)

    @QtCore.Slot()
    def volumeUp(self):
        self.volume = self.device.volume()
        curr_vol = self.volume.actual
        new_vol = curr_vol + 5 
        self.device.set_volume(new_vol)
        self.text.setText(str(self.volume.actual))

    @QtCore.Slot()
    def volumeDown(self):
        self.volume = self.device.volume()
        curr_vol = self.volume.actual
        new_vol = curr_vol - 5 
        self.device.set_volume(new_vol)
        self.text.setText(str(self.volume.actual))

    # def plusVol(self, a):
    #     curr_vol = self.device.volume()
    #     curr_vol += a
    #     self.device.set_volume(new_vol)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())