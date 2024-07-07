import sys
from PyQt5.QtWidgets import QApplication
from monitor.first_frame import FirstDialog
from monitor.enter_frame import EnterDialog
from monitor.area1_frame import Area1Dialog
from monitor.area2_frame import Area2Dialog
#from monitor.login_frame import LoginDialog

def main():
    app = QApplication(sys.argv)
    main_window = FirstDialog()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()