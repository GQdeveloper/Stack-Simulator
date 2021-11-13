# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:13:48 2020

@author: drefg
"""


import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, 
                             QLineEdit, QLabel,  QTextBrowser,
                             QGridLayout, QDialog)

class Form(QDialog):
        
    def __init__(self):
        super(Form, self).__init__()        
        self.title = 'Stack simulator'  
        self.setGeometry(500, 300, 400, 300)

        self.stack = []         
        
        grid = QGridLayout()
        self.setLayout(grid)       
        
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(380, 40)       
       
        #Text Browser
        self.browser = QTextBrowser()
        self.browser.resize(200, 300)
        
        #buttons
        self.pushButton = QPushButton('Push', self)        
        self.popButton = QPushButton('Pop', self)        
        self.clearButton = QPushButton('Clear stack', self)
        
        #Labels
        self.label1 = QLabel("size: 0", self)
        self.label1.setStyleSheet("background-color: white")
        self.label1.resize(380,40)    
        
        self.label2 = QLabel("Preform an action", self)
        self.label2.setStyleSheet("background-color: white")
        self.label2.resize(380,40)        
       
        #adding widgets into the grid
        grid.addWidget(self.lineEdit,0,0,1,5)
        grid.addWidget(self.browser,1,0,4,2)
        grid.addWidget(self.pushButton,1,3,1,1) 
        grid.addWidget(self.popButton,2,3,1,1)
        grid.addWidget(self.clearButton,3,3,1,1)
        grid.addWidget(self.label1,5,0,1,5)
        grid.addWidget(self.label2,6,0,1,5)
       
        
        # connecting buttons
        self.pushButton.clicked.connect(self.on_push)
        self.popButton.clicked.connect(self.on_pop)
        self.clearButton.clicked.connect(self.on_clear)
        self.show()
        
        
    
    def on_push(self):        
       
        try:
            textboxInput = self.lineEdit.text()
            if not textboxInput:
                raise ValueError('empty field')
            self.browser.clear()
            self.stack.append(textboxInput) 
            self.label1.setText("Size: {} ".format(len(self.stack)))
            self.label2.setText("Message: {} has been pushed into the stack".format(textboxInput))
            for i in reversed(self.stack):
                self.browser.append(i)
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        except ValueError as e:
            self.label2.setText("Message: {} ,please enter a value to push into the stack".format(e))                 
        
    
    def on_pop(self):
        if len(self.stack) == 0:
            self.label2.setText("Message: Stack is empty, there is nothing to pop")
            return
        self.browser.clear()        
        self.label2.setText("Message: {} has been poped from the stack".format(self.stack.pop()))
        self.label1.setText("Size: {} ".format(len(self.stack)))
        for i in reversed(self.stack):
            self.browser.append(i)
        self.lineEdit.clear()
        
    def on_clear(self):
        self.browser.clear()
        self.stack.clear()        
        self.label2.setText("The stack has been emptied")
        self.label1.setText("Size: {} ".format(len(self.stack)))        
        self.lineEdit.clear()
        
        
        

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
