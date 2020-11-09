from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QColor

import pyqtgraph as pg
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Load the UI Page
        uic.loadUi('teeeeest.ui', self)
        self.pushButton.clicked.connect(self.show_plot)

    def show_plot(self):
        ############################################ this code draws in the specified location without any problem:
        # self.graphics_View_widget.clear()
        # pg.setConfigOption('background', 'k')
        # h=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # self.graphics_View_widget.plot(h, t, pen=(0,0,255))

        ############################################ this code draws a new window (instead of specified location in qt designer)
        self.graphics_View_widget.clear()
        h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        xDict = dict(enumerate(t))
        xValue = list(xDict.keys())
        self.graphics_View_widget = pg.GraphicsWindow()
        bottomAxis = pg.AxisItem(orientation='bottom')
        pp = self.graphics_View_widget.addPlot(axisItems={'bottom': bottomAxis}, name='h')
        xtickts = [xDict.items()]
        bottomAxis.setTicks(xtickts)
        pp.plot(xValue, h)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())