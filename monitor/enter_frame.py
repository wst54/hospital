from PyQt5.QtWidgets import QDialog
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from monitor.enter_page import E_Dialog
from monitor.area1_frame import Area1Dialog

import cv2 as cv

# ai.haha import DistortEffect
from monitor.video import Video
#from monitor.video1 import Video1
import sys
# 主页面
class EnterDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = E_Dialog()
        self.ui.setupUi(self)
        self.label = self.ui.label  # 修改为实际的 QLabel 控件名称

        # 加载图片
        image_path = './data/enter_bg.png'  # 替换为正确的图片路径
        image_pixmap = QPixmap(image_path)
        if image_pixmap.isNull():  # 检查图片是否成功加载
            print("Failed to load the image.")
        else:
            # 设置 QLabel 的 QPixmap
            self.label.setPixmap(image_pixmap)

        self.th1 = Video('./data/car1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

        self.th2 = Video('./data/car2.mp4')
        # 绑定信号与槽函数
        self.th2.send.connect(self.showimg)
        self.th2.start()


    def showimg(self, h, w, c, b, th_id, num, num1):
        #OpenCV的图片  --->QImage--->像素图---> 缩放---> QT lable显示
        #h,w,c = self.img.shape
        #img_bytes = self.img.tobytes()

        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)

        if th_id == 1:
            # 自动缩放
            width = self.ui.label1.width()
            height = self.ui.label1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label1.setPixmap(scale_pix)
            self.ui.label3.setText(str(num))
            self.ui.label5.setText(str(num1))
        if th_id == 2:
            # 自动缩放
            width = self.ui.label2.width()
            height = self.ui.label2.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label2.setPixmap(scale_pix)
            self.ui.label4.setText(str(num))
            self.ui.label6.setText(str(num1))



    def showenter(self):
        self.md = EnterDialog()
        self.md.show()


    def gomain(self):

        self.th1.stop()  # 调用停止视频播放的方法
        self.th1.wait()  # 等待线程结束
        self.th2.stop()  # 调用停止视频播放的方法
        self.th2.wait()  # 等待线程结束
        from monitor.main_frame import MainDialog
        mian_dialog = MainDialog()

        mian_dialog.show()
        self.close()



