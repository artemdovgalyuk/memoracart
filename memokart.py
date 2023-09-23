from  PyQt5.QtCore import Qt
from PyQt5.QtWidget import (
    QAppication, QWidget, QTableWidget,
    QListWidget, QFormLayout, QLineEdit,
    QPushButton, QSpinBox, QLabel, QRadioButton, QButtonGroup, QGroupBox, QHBoxayout, QVBoxLayout)
app= QAppication([])
btn_Menu = QPushButton('Меню')
btn_Pause= QPushButton('Відпочинок')
box_Minutes= QSpinBox()
box_Minutes.setValue(30)
btn_Answer= QPushButton('Віповісти')
lb_Question = QLabel('Як перекласти слово')
radio_Group= QGroupBox('Вар вітповідей')
rbtn_1= QRadioButton('Yellow')
rbtn_2= QRadioButton('Apple')
rbtn_3= QRadioButton('Green')
rbtn_4= QRadioButton('Red')
ans_Group_Box= QGroupBox('Result test')
lb_Result= QLabel('') #в цьому місці в нас визначається правильно або неправильно
lb_Correct= QLabel('') #3
layout_Ans1= QHBoxLayout()
layout_Ans3= QVBoxLayout()
layout_Ans2= QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1= QHBoxLayout()
layout_line2= QVBoxLayout()
layout_line3= QVBoxLayout()
layout_line4= QVBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Relax)
layout_line1.addWidget(btn_Minutes)
layout_line1.addWidget(QLabel('minutes'))

layout_line2.addWidget(lb_Question, alignment= (Qt.AlignHCentre | Qt.AlignVCentre))
layout_line3.addWidget(radio_Group)
layout_line3.addWidget(ans_Group_Box)

layout_line4.addWidget(btn_Answer, alignment= (Qt.AlignHCentre | Qt.AlignVCentre))

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=6)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)




def show_result():
    radio_Group.hide()
    ans_Group_Box.show()
    btn_Answer.setText("Далі")
def show_question():
    radio_Group.show()
    ans_Group_Box.hide()
    btn_Answer.setText('Відповісти')
    radio_Answer.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_Answer.setExclusive(True)









