from PyQt5.QtWidgets import QDialog
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap

from monitor.area2_page import A2_Dialog

import cv2 as cv

# ai.haha import DistortEffect
from monitor.video2 import Video2
import sys


# 主页面
class Area2Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = A2_Dialog()
        self.ui.setupUi(self)
        self.label = self.ui.label # 修改为实际的 QLabel 控件名称

        # 加载图片
        image_path = './data/area2_bg.png'  # 替换为正确的图片路径
        image_pixmap = QPixmap(image_path)
        if image_pixmap.isNull():  # 检查图片是否成功加载
            print("Failed to load the image.")
        else:
            # 设置 QLabel 的 QPixmap
            self.label.setPixmap(image_pixmap)

        self.th5 = Video2('./data/mask2.mp4')
        # 绑定信号与槽函数
        self.th5.send.connect(self.showimg)
        self.th5.start()

        self.th6 = Video2('./data/mask3.mp4')
        # 绑定信号与槽函数
        self.th6.send.connect(self.showimg)
        self.th6.start()

    def showimg(self, h, w, c, b, th_id, num, num1):
        # OpenCV的图片  --->QImage--->像素图---> 缩放---> QT lable显示
        # h,w,c = self.img.shape
        # img_bytes = self.img.tobytes()

        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 5:
            # 自动缩放
            width = self.ui.label1_13.width()
            height = self.ui.label1_13.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label1_13.setPixmap(scale_pix)
            self.ui.label1_14.setText(str(num))
            self.ui.label_9.setText(str(num1))


        if th_id == 6:
            # 自动缩放
            width = self.ui.label1_15.width()
            height = self.ui.label1_15.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label1_15.setPixmap(scale_pix)
            self.ui.label1_16.setText(str(num))
            self.ui.label_10.setText(str(num1))


    # def closeEvent(self, event):
    #     # 停止线程
    #     if hasattr(self, 'th5') and self.th5.isRunning():
    #         self.th5.stop()
    #     if hasattr(self, 'th6') and self.th6.isRunning():
    #         self.th6.stop()
    #     super().closeEvent(event)  # 调用父类的 closeEvent 方法

    def gomain(self):

        self.th5.stop()  # 调用停止视频播放的方法
        self.th5.wait()  # 等待线程结束
        self.th6.stop()  # 调用停止视频播放的方法
        self.th6.wait()  # 等待线程结束
        from monitor.main_frame import MainDialog
        mian_dialog = MainDialog()

        mian_dialog.show()
        self.close()





