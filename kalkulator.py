from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(450,350)
        self.setStyleSheet("font-size:25px;color:green")
        self.setWindowTitle("Kalkulator")


        self.lbl = QLabel(self)
        self.lbl.move(30, 30)
        

        self.bir = QPushButton("1", self)
        self.bir.move(20, 100)
        self.bir.clicked.connect(lambda: self.screen(self.bir.text()))
        
        self.ikki = QPushButton("2", self)
        self.ikki.move(120, 100)
        self.ikki.clicked.connect(lambda: self.screen(self.ikki.text()))

        self.uch = QPushButton("3", self)
        self.uch.move(220,100)
        self.uch.clicked.connect(lambda: self.screen(self.uch.text()))
        
        self.minus = QPushButton("-", self)
        self.minus.move(320,100)
        self.minus.clicked.connect(lambda: self.screen(self.minus.text()))
        
        self.tort = QPushButton("4", self)
        self.tort.move(20, 140)
        self.tort.clicked.connect(lambda: self.screen(self.tort.text()))

        self.besh = QPushButton("5", self)
        self.besh.move(120, 140)
        self.besh.clicked.connect(lambda: self.screen(self.besh.text()))

        self.olti = QPushButton("6", self)
        self.olti.move(220,140)
        self.olti.clicked.connect(lambda: self.screen(self.olti.text()))
        
        self.koptirish = QPushButton("*", self)
        self.koptirish.move(320,140)
        self.koptirish.clicked.connect(lambda: self.screen(self.koptirish.text()))
        
        self.yetti = QPushButton("7", self)
        self.yetti.move(20, 180)
        self.yetti.clicked.connect(lambda: self.screen(self.yetti.text()))

        self.sakkiz = QPushButton("8", self)
        self.sakkiz.move(120, 180)
        self.sakkiz.clicked.connect(lambda: self.screen(self.sakkiz.text()))

        self.toqqiz = QPushButton("9", self)
        self.toqqiz.move(220,180)
        self.toqqiz.clicked.connect(lambda: self.screen(self.toqqiz.text()))
        
        self.bolish = QPushButton("/", self)
        self.bolish.move(320,180)
        self.bolish.clicked.connect(lambda: self.screen(self.bolish.text()))
        
        self.nuqta = QPushButton(".", self)
        self.nuqta.move(20, 220)
        self.nuqta.clicked.connect(lambda: self.screen(self.nuqta.text()))

        self.nol = QPushButton("0", self)
        self.nol.move(120, 220)
        self.nol.clicked.connect(lambda: self.screen(self.nol.text()))
        
        self.plus = QPushButton("+", self)
        self.plus.move(220, 220)
        self.plus.clicked.connect(lambda: self.screen(self.plus.text()))
        
        self.tenglash = QPushButton("=", self)
        self.tenglash.move(320, 220)
        self.tenglash.clicked.connect(self.hisoblash)
        
        self.clear = QPushButton("Clear", self)
        self.clear.move(20,260)
        self.clear.clicked.connect(self.Clear)
        self.clear.setStyleSheet("color:blue")
        
        
    def screen(self, obj):
        if obj == "*" or obj == '/' or obj == '+':
            if self.lbl.text():
                self.lbl.setStyleSheet("color:black")
                soz = self.lbl.text() + obj
                self.lbl.setText(f"{soz}")
                self.lbl.adjustSize()
        else:
            self.lbl.setStyleSheet("color:black")
            soz = self.lbl.text() + obj
            self.lbl.setText(f"{soz}")
            self.lbl.adjustSize()
    
    def hisoblash(self):
        if self.lbl.text():
            self.lbl.setText(f"{eval(self.lbl.text())}")
            self.lbl.adjustSize()

    def Clear(self):
            self.lbl.clear()

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
