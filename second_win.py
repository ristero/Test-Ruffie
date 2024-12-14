from PyQt5.QtCore import Qt, QTimer,QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel,QWidget, QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from instr import*
from final_win import FinalWin

class Experiment():
    pass
    def __init__(self,age_1,test_1,test_2,test_3):
        self.age = age_1
        self.t1 = test_1
        self.t2 = test_2
        self.t3 = test_3
class SecondWin(QWidget):
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
        self.widgets = []
        self.name = QLabel("Name")
        self.widgets.append(self.name)
        self.lineedit1 = QLineEdit("Name")
        self.widgets.append(self.lineedit1)

        self.text1 = QLabel("Alter:")
        self.widgets.append(self.text1)
        self.age = QLineEdit("0")
        self.widgets.append(self.age)

        self.text2 = QLabel('Legen Sie sich auf den Rücken und messen Sie 15 Sekunden lang Ihren Puls. Klicken Sie auf die Schaltfläche „Ersten Test starten“, um den Timer zu starten. Tragen Sie das Ergebnis in das entsprechende Feld ein.')
        self.widgets.append(self.text2)
        self.pbtn1 = QPushButton("Den ersten Test starten")
        self.widgets.append(self.pbtn1)
        self.t1 = QLineEdit("0")
        self.widgets.append(self.t1)

        self.text3= QLabel('Führen Sie 30 Kniebeugen in 45 Sekunden durch. Drücken Sie dazu die Taste „Start Squat“, um den Squat Counter zu starten.')
        self.widgets.append(self.text3)
        self.pbtn2 = QPushButton("Beginnen Sie mit Kniebeugen")
        self.widgets.append(self.pbtn2)

        self.text4 = QLabel("Legen Sie sich auf den Rücken und messen Sie den Puls in den ersten 15 Sekunden der Minute, dann in den letzten 15 Sekunden der Minute, ohne die Pulsation zu messen. Tragen Sie die Ergebnisse in die entsprechenden Felder ein.")
        self.widgets.append(self.text4)
        self.pbtn3 = QPushButton("Den Abschlusstest starten")
        self.widgets.append(self.pbtn3)

        self.t2 = QLineEdit("0")
        self.widgets.append(self.t2)
        self.t3 = QLineEdit("0")
        self.widgets.append(self.t3)

        self.pbtn4 = QPushButton("Ergebnisse einreichen")
        self.v_line1 = QVBoxLayout()
        self.v_line2 = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.addWidgets()
        self.v_line1.addWidget(self.pbtn4,alignment=Qt.AlignCenter)

        self.text_timer = QLabel("00:00:15")
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.v_line2.addWidget(self.text_timer,alignment= Qt.AlignCenter)

        self.v_lines = [self.v_line1,self.v_line2]
        self.addLines()
        self.setLayout(self.h_line)

    def addWidgets(self):
        for i in self.widgets:
            self.v_line1.addWidget(i, alignment=Qt.AlignLeft)
    def addLines(self):
        for i in self.v_lines:
            self.h_line.addLayout(i)

    def connects(self):
        self.pbtn1.clicked.connect(self.timer_test1)
        self.pbtn2.clicked.connect(self.timer_test2)
        self.pbtn3.clicked.connect(self.timer_test3)
        self.pbtn4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.age.text()), self.t1.text(),self.t2.text(),self.t3.text())
        self.fw= FinalWin(self.exp)

    def timer_test1(self):
        global time1
        time1 = QTime(0,0,15)
        self.timer= QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time1
        time1 = time1.addSecs(-1)
        self.text_timer.setText(time1.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time1.toString("hh,mm,ss") == "00,00,00":
            self.timer.stop()

    def timer_test2(self):
        global time2
        time2 = QTime(0,0,30)
        self.timer= QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time2
        time2 = time2.addSecs(-1)
        self.text_timer.setText(time2.toString("hh:mm:ss")[6:])
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time2.toString("hh,mm,ss") == "00,00,00":
            self.timer.stop()
    
    def timer_test3(self):
        global time3
        time3 = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time3
        time3 = time3.addSecs(-1)
        self.text_timer.setText(time3.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36,QFont.Bold))
        if int(time3.toString("hh:mm:ss")[6:8]) >= 45:#and int(time3.toString("hh:mm:ss")[6:8]) <= 15
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif time3.toString("hh:mm:ss") <= "00,00,15":
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
            
        if time3.toString("hh:mm:ss") == "00,00,00":
            self.timer.stop()
