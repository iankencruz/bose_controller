import sys
import random 


from PySide6 import QtCore, QtWidgets, QtGui
from libsoundtouch import device, soundtouch_device


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Bose Controller")
        
        self.device = soundtouch_device('10.1.1.21')  # Manual configuration
        # self.device.select_source_aux()
        self.volume = self.device.volume()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.power_on_btnn = QtWidgets.QPushButton("Power On")
        self.power_off_bttn = QtWidgets.QPushButton("Power Off")




        self.vol_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.vol_slider.setGeometry(10, 60, 280, 30)
        self.vol_slider.setValue(self.volume.actual)
        self.vol_slider.valueChanged[int].connect(self.changeValue)

        
        self.text = QtWidgets.QLabel(str(self.volume.actual),
                                     alignment=QtCore.Qt.AlignCenter)
        self.text.setFont(QtGui.QFont('Poppins', 20))

        self.layout_top = QtWidgets.QHBoxLayout(self)
        self.layout_top.addWidget(self.text)
        self.layout_top.addWidget(self.power_on_btnn)
        self.layout_top.addWidget(self.power_off_bttn)




        self.layout_bot = QtWidgets.QHBoxLayout(self)

        self.layout_bot.addWidget(self.vol_slider)


        self.layout_top.setAlignment(QtCore.Qt.AlignTop)
        self.layout_bot.setAlignment(QtCore.Qt.AlignTop)


        self.power_on_btnn.clicked.connect(self.powerOn)
        self.power_off_bttn.clicked.connect(self.powerOff)

    @QtCore.Slot()
    def powerOn(self):
        self.device.power_on()

    @QtCore.Slot()
    def powerOff(self):
        self.device.power_off()


    def changeValue(self, value):

        self.volume = self.device.volume()
        self.device.set_volume(self.vol_slider.value())
        self.text.setText(str(self.vol_slider.value()))




if __name__ == "__main__":
    # app = QtWidgets.QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    

    widget = MyWidget()
    widget.resize(300, 100)
    widget.show()

    sys.exit(app.exec())