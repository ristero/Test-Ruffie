# напиши тут код третього екрана програми
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from second_win import*
from instr import*


class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.setApear()
        self.initUI()
        self.show()
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            if self.index <15 and self.index >= 11:
                return txt_res2
            if self.index < 11 and self.index >= 6:
                return txt_res3
            if self.index < 6 and self.index >= 0.5:
                return txt_res4
            if self.index < 0.4:
                return txt_res5
        if self.exp.age <= 14 and self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res1
            if self.index <16.4 and self.index >= 12.5:
                return txt_res2
            if self.index < 12.4 and self.index >= 7.5:
                return txt_res3
            if self.index < 7.4 and self.index >= 2:
                return txt_res4
            if self.index < 1.9:
                return txt_res5
        if self.exp.age <= 12 and self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            if self.index <17.9 and self.index >= 14:
                return txt_res2
            if self.index < 13.9 and self.index >= 9:
                return txt_res3
            if self.index < 8.9 and self.index >= 3.5:
                return txt_res4
            if self.index < 3.4:
                return txt_res5
        if self.exp.age <= 10 and self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            if self.index <19.4 and self.index >= 15.5:
                return txt_res2
            if self.index < 15.4 and self.index >= 10.5:
                return txt_res3
            if self.index < 10.4 and self.index >= 5:
                return txt_res4
            if self.index < 4.9:
                return txt_res5
        if self.exp.age <= 8 and self.exp.age >= 7:
            if self.index >= 18:
                return txt_res1
            if self.index <20.9 and self.index >= 17:
                return txt_res2
            if self.index < 16.9 and self.index >= 12:
                return txt_res3
            if self.index < 11.9 and self.index >= 6.5:
                return txt_res4
            if self.index < 6.4:
                return txt_res5
    def setApear(self):
        self.setWindowTitle(txt_title)
        self.resize(b,h)
    def initUI(self):
        self.widgets=[]
        self.test_results2 = QLabel(txt_workheart+self.results())
        self.widgets.append(self.test_results2)
        self.test_results1 = QLabel(txt_index+str(self.index))
        self.widgets.append(self.test_results1)
        self.v_line = QVBoxLayout()
        self.addWidgets()
        self.setLayout(self.v_line)

    def addWidgets(self):
        for i in self.widgets:
            self.v_line.addWidget(i,alignment=Qt.AlignCenter)
