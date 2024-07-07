from PyQt5.QtGui import QImage, QPixmap
from monitor.login_page import L_Dialog
from monitor.main_frame import MainDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QMessageBox

from PyQt5 import QtWidgets, QtGui, QtCore


'#page 是 Ui_,E_dialog,frame是EnterDialog'


import cv2 as cv

# ai.haha import DistortEffect
from monitor.video import Video
import sys
# 主页面
class LoginDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)

        self.pixmap = QtGui.QPixmap("./data/login_bg.png")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        #self.resizeEvent = self.on_resize
        self.ui = L_Dialog()
        self.ui.setupUi(self)



    def showimg(self, h, w, c, b, th_id):
        #OpenCV的图片  --->QImage--->像素图---> 缩放---> QT lable显示
        #h,w,c = self.img.shape
        #img_bytes = self.img.tobytes()

        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)



    def showLogin(self):
        self.md = LoginDialog()
        self.md.show()


    def gomain(self):
        # 获取账号和密码输入
        account = self.ui.textEdit.toPlainText()  # 假设账号输入框对象名为 textEdit
        password = self.ui.textEdit_2.toPlainText()  # 假设密码输入框对象名为 textEdit_2

        # 设置正确的账号和密码
        correct_account = "manager"
        correct_password = "123456"

        # 验证账号和密码
        if account == correct_account and password == correct_password:
            self.enterframe = MainDialog()
            self.enterframe.show()
            self.close()
        else:
            # 显示账号或密码错误的消息框
            QMessageBox.warning(self, "登录错误", "账号或密码错误，请重试！")


    def gofirst(self):
        from monitor.first_frame import FirstDialog
        #self.firstframe = FirstDialog()
        #self.monitorframe.show()
        #FirstDialog.show_dialog()
        #self.close()
        first_dialog = FirstDialog()
        first_dialog.show()
        self.close()


