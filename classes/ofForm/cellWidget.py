from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CellWidget(QWidget):
    expandable = pyqtSignal(int, int)
    clicked = pyqtSignal()
    ohno = pyqtSignal()

    def __init__(self, x, y, partition, h = None, cell = None):
        super(CellWidget, self).__init__()

        W_MAX_SIZE = 100

        self.setFixedSize(QSize(W_MAX_SIZE / partition, W_MAX_SIZE / partition))
        self.setAutoFillBackground(True)

        self.qcolorsOfPlant = [
            QColor(38, 96, 31), QColor(55, 111, 36),
            QColor(64, 128, 42), QColor(81, 148, 50),
            QColor(143, 220, 78), QColor(112, 187, 61),
            QColor(127, 204, 69), QColor(140, 220, 76),
            QColor(158, 236, 88), QColor(180, 248, 107),
            QColor(194, 253, 124), QColor(209, 254, 143),
            QColor(249, 254, 158) ]
        self.QcolorNone = QColor(211, 153, 95)

        self.p = self.palette()
        self.color = self._getColor(h)
        self.p.setColor(self.backgroundRole(), self.color)
        self.setPalette(self.p)

        self.x = x
        self.y = y

        self.cell = cell

    def _getColor(self, h = None) :
            if h is not None :
                from ..plant import LiveObjOnMap
                maxH = LiveObjOnMap.MAX_HEIGHT
                h /= maxH
                i = int((h * len(self.qcolorsOfPlant)) // 1)
                # Подстраховка на случай максимально высокого растения
                if i >= len(self.qcolorsOfPlant) : i = len(self.qcolorsOfPlant) - 1
                return self.qcolorsOfPlant[i]
            else :
                return self.QcolorNone
    
    def checkColor(self, h = None) :
        newColor = self._getColor(h)
        if newColor is not self.color :
            self.color = newColor
            self.p.setColor(self.backgroundRole(), self.color)
            self.setPalette(self.p)  


    # def reset(self):
    #     self.is_start = False
    #     self.is_mine = False
    #     self.adjacent_n = 0

    #     self.is_revealed = False
    #     self.is_flagged = False

    #     self.update()

    # def paintEvent(self, event):
    #     p = QPainter(self)
    #     p.setRenderHint(QPainter.Antialiasing)

    #     r = event.rect()

    #     if self.is_revealed:
    #         color = self.palette().color(QPalette.Background)
    #         outer, inner = color, color
    #     else:
    #         outer, inner = Qt.gray, Qt.lightGray

    #     p.fillRect(r, QBrush(inner))
    #     pen = QPen(outer)
    #     pen.setWidth(1)
    #     p.setPen(pen)
    #     p.drawRect(r)

    #     if self.is_revealed:
    #         if self.is_start:
    #             p.drawPixmap(r, QPixmap(IMG_START))

    #         elif self.is_mine:
    #             p.drawPixmap(r, QPixmap(IMG_BOMB))

    #         elif self.adjacent_n > 0:
    #             pen = QPen(NUM_COLORS[self.adjacent_n])
    #             p.setPen(pen)
    #             f = p.font()
    #             f.setBold(True)
    #             p.setFont(f)
    #             p.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.adjacent_n))

    #     elif self.is_flagged:
    #         p.drawPixmap(r, QPixmap(IMG_FLAG))

    # def flag(self):
    #     self.is_flagged = True
    #     self.update()

    #     self.clicked.emit()

    # def reveal(self):
    #     self.is_revealed = True
    #     self.update()

    # def click(self):
    #     if not self.is_revealed:
    #         self.reveal()
    #         if self.adjacent_n == 0:
    #             self.expandable.emit(self.x, self.y)

    #     self.clicked.emit()

    # def mouseReleaseEvent(self, e):

    #     if (e.button() == Qt.RightButton and not self.is_revealed):
    #         self.flag()

    #     elif (e.button() == Qt.LeftButton):
    #         self.click()

    #         if self.is_mine:
    #             self.ohno.emit()
