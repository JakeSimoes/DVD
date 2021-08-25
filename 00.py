import sys
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from threading import Thread
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
import random

speed = 0.1
started = False

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(240,122),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

        self.setAttribute(
            QtCore.Qt.WA_TranslucentBackground
        )
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('../dvd.png')
        label.setPixmap(pixmap.scaled(240,122))
        label.resize(240,122)
        self.show()

    def Worker(QObject):
        global speed
        bounds = [app.primaryScreen().size().width() - 240,
                  app.primaryScreen().size().height() - 122]
        try:
            while True:
                mywindow.move(mywindow.pos().x() + 1,
                              mywindow.pos().y() + 1)
                if mywindow.pos().x() > bounds[0] or mywindow.pos().y() > \
                        bounds[1]:
                    print("break!")
                    break
                time.sleep(speed)
        except Exception as e:
            print(e)


    def mousePressEvent(self, event):

        global speed
        try:
            global started
            if not started:
                started = True
                print("bleh")
                self.thread = QThread()
                # Step 3: Create a worker object
                self.worker = self.Worker()
                # Step 4: Move worker to the thread
                self.worker.moveToThread(self.thread)
                self.thread.start()
            else:
                print(speed)
                speed += 0.05
        except Exception as e:
            print(e)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()

