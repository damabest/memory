from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

#the question ask and what questions there are
class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
        
question_list = [Question('How many people are there in the world?', '8bil', '6bil', '7bil', '2bil'),
                        Question('What type of tree does an acron come from?', 'Oak', 'Pine', 'Spruce', 'Birch'),
                        Question('What is the capital city of France?', 'Paris', 'Madrid', 'Berlin', 'Rome'),
                        Question('Which planet is known as the "Red Planet"?', 'Mars', 'Venus', 'Earth', 'Saturn'),
                        Question('In which year did the Titanic sink?', '1912', '1914', '1918', '1922'),
                        Question('What is the largest mammal in the world?', 'Blue Whale', 'Elephant', 'Spider', 'Giraffe'),
                        Question('Which element has the chemical symbol "H"?', 'Hydrogen', 'Helium', 'Iron', 'Mercury'),
                        Question('Who wrote "Romeo and Juliet"?', 'Shakespeare', 'Your Dad', 'Mark Twain', 'Charles Dickens'),
                        Question('What is the largest ocean on Earth?', 'Pacific', 'Atlantic', 'Indian', 'Southern'),
                        Question('What is the currency of Japan?', 'Yen', 'Yuan', 'Wuan', 'Won'),
                        Question('Which year did Kazakhstan gain independence?', '1991', '1990', '1981', '1891')]

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')
btn_answer = QPushButton('Answer')
lb_Question = QLabel('Which nationality does not exist?')

RadioGroupBox = QGroupBox('Varients of answers')

#buttons and what they do and their question
Varients = QLabel('Varients of answers')
btn1 = QRadioButton('Indians')
btn2 = QRadioButton('Pakistani')
btn3 = QRadioButton('Smurfs')
btn4 = QRadioButton('American')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

#layout and what it is supposed to look like
layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans1.addWidget(btn1)
layout_ans1.addWidget(btn2)
layout_ans2.addWidget(btn3)
layout_ans2.addWidget(btn4)

layout_ans3.addLayout(layout_ans1)
layout_ans3.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_ans3)

#where the questions are layed out
AnsGroupBox = QGroupBox('results')
lb_Result = QLabel('Right/Not Right')
lb_Correct = QLabel('Correct Answer')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

#layout and where they are supposed to go
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

#where it is positioned e.g. left, right or center
layout_line1.addWidget(lb_Question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_answer, stretch=3)
RadioGroupBox.hide()

#the layout and how it is supposed to look like
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

#whether or not the answer is correct or not
def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_answer.setText('Next Question')

#question and showing the first question
def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_answer.setText('Varients of answers')
        RadioGroup.setExclusive(False)
        btn1.setChecked(False)
        btn2.setChecked(False)
        btn3.setChecked(False)
        btn4.setChecked(False)
        RadioGroup.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]

#asking statement and asking the questions in def show_question
def ask(q):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()

#correct answer and if it is show the results
def show_correct(res):
        lb_Result.setText(res)
        show_result()

#if right answer and checking it
def check_answer():
        if answers[0].isChecked():
                show_correct('Its True!')
                mw.score += 1
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct('Incorrect!')
        print(f'Statistics\nNumber of Questions: {mw.total}\nCorrect Answers: {mw.score}')
        print(f'Rating: {mw.score/mw.total*100}%')
#going onto the next question and showing if it was correct or not
def next_question():
        mw.total += 1
        print(f'Statistics\nOnly Answers: {mw.total}\nCorrect Answers: {mw.score}')
        cur_question = randint(0, len(question_list) - 1)
        q = question_list[cur_question]
        ask(q)

#after the answer is answered, this will check whether or not it is correct and if so do onto the next question
def click_OK():
        if btn_answer.text() == 'Varients of answers':
                check_answer()
        else:
                next_question()


mw.total = 0
mw.score = 0
next_question()
btn_answer.clicked.connect(click_OK)
mw.setLayout(layout_card)
mw.show()
app.exec()

