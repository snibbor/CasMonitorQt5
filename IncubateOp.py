# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IncubateOperation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class IncubateOp(QtWidgets.QStackedWidget):
    def __init__(self, typeParamWid = False):
        QtWidgets.QStackedWidget().__init__()
        # Form.setObjectName("Form")
        # Form.resize(700, 700)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        # Form.setSizePolicy(sizePolicy)
        # Form.setMinimumSize(QtCore.QSize(0, 30))
        
        
        #Make a stacked widget that has a label side and parameter side
        # self.formwidget = QtWidgets.QWidget(Form)
        
        # self.stack = QtWidgets.QStackedWidget(Form)
        
        self.stack = QtWidgets.QStackedWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName("stack")
        
        
        #Front side of widget
        #0
        self.labelWidget = QtWidgets.QWidget()
        self.labelWidget.resize(110,50)
        self.frontLabel = QtWidgets.QLabel(self.labelWidget)
        self.frontLabel.setGeometry(QtCore.QRect(10, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frontLabel.setFont(font)
        self.frontLabel.setObjectName("frontLabel")
        self.frontLabel.setText("Incubate")
        self.stack.addWidget(self.labelWidget)
        
        #Main parameter widget
        #1
        # self.paramWidget = QtWidgets.QWidget(Form)
        self.paramWidget = QtWidgets.QWidget()
        self.paramWidget.resize(590, 32)
        self.stack.addWidget(self.paramWidget)
        
        #Specify widget type to display
        self.switchWidget(typeParamWid)
        
        # self.topFrame = QtWidgets.QFrame(Form)
        self.topFrame = QtWidgets.QFrame(self.paramWidget)
        # self.paramWidget.addWidget(self.topFrame)
        self.topFrame.setGeometry(QtCore.QRect(0, 0, 590, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setMinimumSize(QtCore.QSize(590, 32))
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        
        self.incButton = QtWidgets.QToolButton(self.topFrame, checked = False, checkable = True)
        self.incButton.setText("Incubation")
        self.incButton.setGeometry(QtCore.QRect(0, 0, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.incButton.setFont(font)
        self.incButton.setStyleSheet("border: None\n" "")
        self.incButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.incButton.setAutoRaise(False)
        self.incButton.setArrowType(QtCore.Qt.RightArrow)
        self.incButton.setObjectName("incButton")
        
        self.dispTimeLab = QtWidgets.QLabel(self.topFrame)
        self.dispTimeLab.setGeometry(QtCore.QRect(430, 0, 101, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dispTimeLab.setFont(font)
        self.dispTimeLab.setObjectName("dispTimeLab")
        self.dispTimeLab.setText("(hh:mm:ss)")
        
        self.removeButton = QtWidgets.QPushButton(self.topFrame)
        self.removeButton.setEnabled(True)
        self.removeButton.setGeometry(QtCore.QRect(550, 0, 32, 32))
        self.removeButton.setStyleSheet("border: None")
        self.removeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon)
        self.removeButton.setIconSize(QtCore.QSize(10, 10))
        self.removeButton.setObjectName("removeButton")
        
        
        # self.botFrame = QtWidgets.QFrame(Form)
        self.botFrame = QtWidgets.QFrame(self.paramWidget)
        # self.paramWidget.addWidget(self.botFrame)
        self.botFrame.setGeometry(QtCore.QRect(0, 32, 590, 52))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botFrame.sizePolicy().hasHeightForWidth())
        self.botFrame.setSizePolicy(sizePolicy)
        self.botFrame.setMinimumSize(QtCore.QSize(590, 52))
        self.botFrame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.botFrame.setObjectName("botFrame")
        # self.botFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.botFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        #Initial state is with the parameters hidden?
        self.botFrame.hide()
        
        self.tempLab = QtWidgets.QLabel(self.botFrame)
        self.tempLab.setGeometry(QtCore.QRect(20, 5, 140, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLab.setFont(font)
        self.tempLab.setObjectName("tempLab")
        self.tempLab.setText("Temperature (°C):")
        
        self.tempEdit = QtWidgets.QLineEdit(self.botFrame)
        self.tempEdit.setGeometry(QtCore.QRect(20, 25, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempEdit.setFont(font)
        self.tempEdit.setObjectName("tempEdit")
        self.tempEdit.setInputMask("999")
        
        self.timeLab = QtWidgets.QLabel(self.botFrame)
        self.timeLab.setGeometry(QtCore.QRect(190, 5, 140, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeLab.setFont(font)
        self.timeLab.setObjectName("timeLab")
        self.timeLab.setText("Time (hh:mm:ss):")
        
        self.timeEdit = QtWidgets.QLineEdit(self.botFrame)
        self.timeEdit.setGeometry(QtCore.QRect(190, 25, 120, 20))
        self.timeEdit.setInputMethodHints(QtCore.Qt.ImhTime)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setInputMask("99:99:99")
        self.timeEdit.setText("::")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEdit.setFont(font)
        
        self.shakBox = QtWidgets.QCheckBox(self.botFrame)
        self.shakBox.setGeometry(QtCore.QRect(370, 10, 91, 23))
        # self.shakBox.setStyleSheet("""
        # QWidget {
        #     border: 2px solid black;
        #     }
        # """)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shakBox.setFont(font)
        self.shakBox.setIconSize(QtCore.QSize(16, 16))
        self.shakBox.setTristate(False)
        self.shakBox.setObjectName("shakBox")
        self.shakBox.setText("Shaking")
        
        
        self.incButton.clicked.connect(lambda: self.onClick())
        self.removeButton.clicked.connect(self.paramWidget.hide)
        # print(self.incButton.isChecked())

        
    @QtCore.pyqtSlot()
    def onClick(self):
        
        checked = self.incButton.isChecked()
        # print(checked)
        if checked:    
            self.botFrame.show()
            self.paramWidget.resize(590,82)
            self.stack.resize(590,82)            
            # Form.resize(590,92)
            self.incButton.setArrowType(QtCore.Qt.DownArrow)
        else:
            self.botFrame.hide()
            self.paramWidget.resize(590,32)
            self.stack.resize(590,32)
            # Form.resize(590,32)
            self.incButton.setArrowType(QtCore.Qt.RightArrow)
            
    def switchWidget(self, typeParamWidget):
        if typeParamWidget:
            self.stack.resize(590,32)
            self.stack.setCurrentIndex(1)
        else:
            self.stack.resize(110,50)
            self.stack.setCurrentIndex(0)
    
    def dropEvent(self, event):
        
        
        
        
        

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     IncOp = IncubateOp(MainWindow)
#     # IncOp.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
    
# if __name__ == '__main__':
#     main()
        
        
        
        
        
        
       

