#DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#화면을 로딩
form_clas = uic.loadUiType("DemoForm.ui")[0]
#윈도우 (폼) 클래스 정의
class DemoForm(QDialog, form_clas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모")
#직접 이 모듈을 실행한 경우 체크
if __name__== "__main__":
    app = QApplication(sys.argv)
    DemoForm=DemoForm()
    DemoForm.show()
    app.exec()

