from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QPen, QPolygon, QBrush
from PyQt5.QtCore import Qt, QTimer, QPoint

from state.Factory import blank_state, random_state
from state.LifeState import LifeState


class LifeWindow(QMainWindow):

    tick_time: int = 200

    def __init__(self, state: LifeState):
        super().__init__()

        self.state = state
        self.title = 'GoL'
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 700

        self.timer = QTimer()
        self.tick = 0
        self.init_window()
        self.timer.timeout.connect(self.on_tick)
        self.timer.start(self.tick_time)

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def on_tick(self):
        self.timer.stop()
        self.tick += 1
        self.state = self.state.evolve()
        self.repaint()
        self.timer.start(self.tick_time)

    def paintEvent(self, e):
        self.paint_game_box()
        # self.paint_track()
        # self.paint_start_arrow()
        # self.paint_cars()
        # self.paint_text()

    def paint_game_box(self):
        live = QBrush(Qt.green, Qt.DiagCrossPattern)
        dead = QBrush(Qt.red, Qt.DiagCrossPattern)
        gap = 500 / self.state.size()
        painter = QPainter(self)
        for x in range(self.state.size()):
            for y in range(self.state.size()):
                val = self.state.value(x, y)
                painter.fillRect(49 + gap * x, 49 + gap * y, gap, gap, live if val == 1 else dead)

        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.drawRect(48, 48, 502, 502)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        for i in range(1, self.state.size()):
            painter.drawLine(48, 48 + gap * i, 550, 48 + gap * i)
            painter.drawLine(48 + gap * i, 48, 48 + gap * i, 550)

    @staticmethod
    def new(state: LifeState):
        app = QApplication([])
        window = LifeWindow(state if state is not None else random_state(25, 0.5))
        app.exec_()
