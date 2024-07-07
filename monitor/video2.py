from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal

from ai.mask import smokmask_detect
from ai.people import people_detect


# 重写父类run（）方法：线程执行内容
# Thread的实例对象.strat() run()就会自动执行
class Video2(QThread):
    # 使用信号与槽函数向外传递数据
    #   信号发送者   video
    #   信号类型    自定义信号类型（）
    #   信号接受者   线程所在dialog
    #   槽函数     （接受者类：公能方法）

    # 信号定义方法
    send = pyqtSignal(int, int, int, bytes, int, int, int)  # emit

    def __init__(self, video_id):
        super().__init__()
        # 准备工作
        self.th_id = 0
        self.running = True

        if video_id == './data/mask2.mp4':
            self.th_id = 5
        if video_id == './data/mask3.mp4':
            self.th_id = 6
        self.dev = cv.VideoCapture(video_id)
        # self.dev = cv.VideoCapture(0,cv.CAP_DSHOW)

        self.dev.open(video_id)

    def run(self):
        # 耗时操作
        i = 0
        ret, frame = self.dev.read()
        num, num1 = smokmask_detect(frame)
        while not self.isInterruptionRequested():
            try:
                if not self.running:
                    # 如果 running 为 False，退出循环
                    break
                ret, frame = self.dev.read()
                i = i + 1
                if i % 10 == 0:
                    print('检测')
                    num, num1 = smokmask_detect(frame)
                if not ret:
                    print('no')
                    break
                h, w, c = frame.shape
                img_bytes = frame.tobytes()
                self.send.emit(h, w, c, img_bytes, self.th_id, num, num1)
            # us
                QThread.usleep(1000000)
            except Exception as e:
                print("Error in thread:", e)


    def stop(self):
        self.requestInterruption()
        self.dev.release()  # 释放视频捕获设备
        self.quit()  # 退出线程
        self.wait()  # 等待线程结束


