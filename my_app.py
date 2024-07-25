from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QVBoxLayout,QLabel 
from instr import*
from second_win import*


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(h,b)
    def initUI(self):
        self.text1 = QLabel(hello)
        self.text2 = QLabel(instraction)
        self.pbtn = QPushButton(pbtn_text)
        self.v_line = QVBoxLayout()
        self.widgets = [self.text1,self.text2,self.pbtn]
        self.add_widgets()
        self.setLayout(self.v_line)
    def add_widgets(self):
        for i in self.widgets:
            self.v_line.addWidget(i,alignment= Qt.AlignCenter)


    def connects(self):
        self.pbtn.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.nw = SecondWin()



app = QApplication([])
win = MainWin()
app.exec_()

