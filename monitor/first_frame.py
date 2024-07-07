from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.first_home import F_Dialog
from monitor.login_frame import LoginDialog

import cv2 as cv

import sys
# 主页面

class FirstDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)

        self.pixmap = QtGui.QPixmap("./data/first_bg.png")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                            transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize
        self.ui = F_Dialog()
        self.ui.setupUi(self)


    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def showFirst(self):
        self.md = FirstDialog()
        self.md.show()


    def show_dialog(self):
        fdialog = FirstDialog()  # 创建 FirstDialog 的实例
        fdialog.show()

    def gologin(self):
        self.monitorframe = LoginDialog()
        self.monitorframe.show()
        self.close()

if __name__ == "__main__":
    FirstDialog()

