from PyQt5.QtWidgets import QDialog
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap

from monitor.area1_page import A1_Dialog
from monitor.area2_frame import Area2Dialog
import cv2 as cv

# ai.haha import DistortEffect
from monitor.video1 import Video1
import sys


# 主页面
class Area1Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = A1_Dialog()
        self.ui.setupUi(self)
        self.label = self.ui.label_3  # 修改为实际的 QLabel 控件名称

        # 加载图片
        image_path = './data/area1_bg.png'  # 替换为正确的图片路径
        image_pixmap = QPixmap(image_path)
        if image_pixmap.isNull():  # 检查图片是否成功加载
            print("Failed to load the image.")
        else:
            # 设置 QLabel 的 QPixmap
            self.label.setPixmap(image_pixmap)

        self.th3 = Video1('./data/smoking.mp4')
        # 绑定信号与槽函数
        self.th3.send.connect(self.showimg)
        self.th3.start()

        self.th4 = Video1('./data/mask.mp4')
        # 绑定信号与槽函数
        self.th4.send.connect(self.showimg)
        self.th4.start()

    def showimg(self, h, w, c, b, th_id, num, num1):
        # OpenCV的图片  --->QImage--->像素图---> 缩放---> QT lable显示
        # h,w,c = self.img.shape
        # img_bytes = self.img.tobytes()

        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 3:
            # 自动缩放
            width = self.ui.label1_1.width()
            height = self.ui.label1_1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label1_1.setPixmap(scale_pix)
            self.ui.label1_4.setText(str(num))
            self.ui.label_4.setText(str(num1))


        if th_id == 4:
            # 自动缩放
            width = self.ui.label1_3.width()
            height = self.ui.label1_3.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label1_3.setPixmap(scale_pix)
            self.ui.label1_5.setText(str(num))
            self.ui.label_5.setText(str(num1))

    def showarea1(self):
        self.md = Area1Dialog()
        self.md.show()

    # def closeEvent(self, event):
    #     # 停止线程
    #     if hasattr(self, 'th3') and self.th3.isRunning():
    #         self.th3.stop()
    #     if hasattr(self, 'th4') and self.th4.isRunning():
    #         self.th4.stop()
    #     super().closeEvent(event)  # 调用父类的 closeEvent 方法

    def gomain(self):

        self.th3.stop()  # 调用停止视频播放的方法
        self.th3.wait()  # 等待线程结束
        self.th4.stop()  # 调用停止视频播放的方法
        self.th4.wait()  # 等待线程结束
        from monitor.main_frame import MainDialog
        mian_dialog = MainDialog()

        mian_dialog.show()
        self.close()






