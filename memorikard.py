from  PyQt5.QtCore import Qt
from PyQt5.QtWidget import (
    QAppication, QWidget, QTableWidget,
    QListWidget, QFormLayout, QLineEdit,
    QPushButton, QSpinBox, QLabel, QRadioButton, QButtonGroup, QGroupBox, QHBoxayout, QVBoxLayout)
from memo_kart import *

lb_question = QListView()
widget_ans= QWidget
widget.ans(layout_form)
btn_add= QPushButton('new question')
btn_bel= QPushButton('del que')
btn_start=QPushButton('Початок тексту')

qst_col= QVBoxLayout()
qst_col.addWidget(list_question)
qst_col.addWidget(btn_add)

ans_col = QVBoxLayout()
ans_col.addWidget(widget_ans)
ans_col.addWidget(btn_del)

btn_line= QHBoxLayout()
btn_line.addLayout(qst_col) 
btn_line.addLayout(ans_col) 

test_line= QHBoxLayout()
test_line.addStretch(1)
test_line.addWidget(btn_start, stretch= 2)
test_line.addStretch(1)

layout_screen= QVBoxLayout(btn_line)
layout_screen.addLayout(test_line)