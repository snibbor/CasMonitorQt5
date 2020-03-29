#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:25:42 2020

@author: jackr
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class SampMonitor(QtWidgets.QStackedWidget):
    def __init__(self, casNumber):
        QtWidgets.QStackedWidget.__init__(self)
        self.monWidget = QtWidgets.QStackedWidget()
        self.monWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monWidget.sizePolicy().hasHeightForWidth())
        self.monWidget.setSizePolicy(sizePolicy)
        self.monWidget.setAcceptDrops(False)
        self.monWidget.setObjectName("monWidget"+str(casNumber))
        
        #Page 1: active run with progress bar
        self.SxPage1 = QtWidgets.QWidget()
        self.SxPage1.setObjectName("S"+str(casNumber)+"Page1")
        self.gridLayout_xp1 = QtWidgets.QGridLayout(self.SxPage1)
        self.gridLayout_xp1.setObjectName("gridLayout_"+str(casNumber)+"p1")
        self.sampName = QtWidgets.QLabel(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampName.sizePolicy().hasHeightForWidth())
        self.sampName.setSizePolicy(sizePolicy)
        self.sampName.setAlignment(QtCore.Qt.AlignCenter)
        self.sampName.setObjectName("sampName_" + str(casNumber))
        self.sampName.setText("SampleName")
        self.gridLayout_xp1.addWidget(self.sampName, 1, 0, 1, 1)
        
        self.step = QtWidgets.QLabel(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step.sizePolicy().hasHeightForWidth())
        self.step.setSizePolicy(sizePolicy)
        self.step.setAlignment(QtCore.Qt.AlignCenter)
        self.step.setObjectName("step" + str(casNumber))
        self.step.setText("\"Wash (1/6)\"")
        self.gridLayout_xp1.addWidget(self.step, 7, 0, 1, 1)
        
        self.progressBar = QtWidgets.QProgressBar(self.SxPage1)
        self.progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 19)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar_" + str(casNumber))
        self.progressBar.setFormat("%p%")
        self.gridLayout_xp1.addWidget(self.progressBar, 9, 0, 1, 2)
        
        self.stopB = QtWidgets.QPushButton(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopB.sizePolicy().hasHeightForWidth())
        self.stopB.setSizePolicy(sizePolicy)
        self.stopB.setObjectName("stopB_" + str(casNumber))
        self.stopB.setText("Stop Run")
        self.gridLayout_xp1.addWidget(self.stopB, 10, 0, 1, 2)
        
        self.protName = QtWidgets.QLabel(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.protName.sizePolicy().hasHeightForWidth())
        self.protName.setSizePolicy(sizePolicy)
        self.protName.setAlignment(QtCore.Qt.AlignCenter)
        self.protName.setObjectName("protName_" + str(casNumber))
        self.protName.setText("ProtocolName")
        self.gridLayout_xp1.addWidget(self.protName, 1, 1, 1, 1)
        
        self.runDetB = QtWidgets.QPushButton(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runDetB.sizePolicy().hasHeightForWidth())
        self.runDetB.setSizePolicy(sizePolicy)
        self.runDetB.setAutoDefault(False)
        self.runDetB.setDefault(False)
        self.runDetB.setFlat(False)
        self.runDetB.setObjectName("runDetB_" + str(casNumber))
        self.runDetB.setText("Run Details")
        self.gridLayout_xp1.addWidget(self.runDetB, 2, 0, 1, 2)
        
        self.casN_x1 = QtWidgets.QLabel(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.casN_x1.sizePolicy().hasHeightForWidth())
        self.casN_x1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.casN_x1.setFont(font)
        self.casN_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.casN_x1.setObjectName("casN_"+str(casNumber)+"1")
        self.casN_x1.setText(str(casNumber))
        self.gridLayout_xp1.addWidget(self.casN_x1, 0, 0, 1, 2)
        
        self.time = QtWidgets.QLabel(self.SxPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time_" + str(casNumber))
        self.time.setText("HH:mm:ss")
        self.gridLayout_xp1.addWidget(self.time, 7, 1, 1, 1)
        self.monWidget.addWidget(self.SxPage1)
        
        #Page 2: cassette ready to start new run
        self.SxPage2 = QtWidgets.QWidget()
        self.SxPage2.setObjectName("S"+str(casNumber)+"Page2")
        self.gridLayout_xp2 = QtWidgets.QGridLayout(self.SxPage2)
        self.gridLayout_xp2.setObjectName("gridLayout_"+str(casNumber)+"p2")
        self.casN_x2 = QtWidgets.QLabel(self.SxPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.casN_x2.sizePolicy().hasHeightForWidth())
        self.casN_x2.setSizePolicy(sizePolicy)
        self.casN_x2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.casN_x2.setFont(font)
        self.casN_x2.setAlignment(QtCore.Qt.AlignCenter)
        self.casN_x2.setObjectName("casN_"+str(casNumber)+"2")
        self.casN_x2.setText(str(casNumber))
        self.gridLayout_xp2.addWidget(self.casN_x2, 0, 0, 1, 2)
        
        self.setupB = QtWidgets.QPushButton(self.SxPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setupB.sizePolicy().hasHeightForWidth())
        self.setupB.setSizePolicy(sizePolicy)
        self.setupB.setBaseSize(QtCore.QSize(0, 0))
        self.setupB.setObjectName("setupB_" + str(casNumber))
        self.setupB.setText("Setup Run")
        self.gridLayout_xp2.addWidget(self.setupB, 2, 0, 1, 1)
        
        self.runDefault = QtWidgets.QPushButton(self.SxPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runDefault.sizePolicy().hasHeightForWidth())
        self.runDefault.setSizePolicy(sizePolicy)
        self.runDefault.setSizeIncrement(QtCore.QSize(0, 0))
        self.runDefault.setBaseSize(QtCore.QSize(0, 0))
        self.runDefault.setObjectName("runDefault_" + str(casNumber))
        self.runDefault.setText("Run Default")
        self.gridLayout_xp2.addWidget(self.runDefault, 2, 1, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_xp2.addItem(spacerItem, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_xp2.addItem(spacerItem1, 3, 0, 1, 2)
        self.monWidget.addWidget(self.SxPage2)
        
        #Page 3: No cassette detected
        self.SxPage3 = QtWidgets.QWidget()
        self.SxPage3.setObjectName("S"+str(casNumber)+"Page3")
        self.gridLayout_xp3 = QtWidgets.QGridLayout(self.SxPage3)
        self.gridLayout_xp3.setObjectName("gridLayout_"+str(casNumber)+"p3")
        self.casN_x3 = QtWidgets.QLabel(self.SxPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.casN_x3.sizePolicy().hasHeightForWidth())
        self.casN_x3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.casN_x3.setFont(font)
        self.casN_x3.setAlignment(QtCore.Qt.AlignCenter)
        self.casN_x3.setObjectName("casN_"+str(casNumber)+"3")
        self.casN_x3.setText(str(casNumber))
        self.gridLayout_xp3.addWidget(self.casN_x3, 0, 0, 1, 1)
        
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_xp3.addItem(spacerItem2, 1, 0, 1, 1)
        
        self.noCas = QtWidgets.QLabel(self.SxPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noCas.sizePolicy().hasHeightForWidth())
        self.noCas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noCas.setFont(font)
        self.noCas.setAlignment(QtCore.Qt.AlignCenter)
        self.noCas.setObjectName("noCas_" + str(casNumber))
        self.noCas.setText("No cassette detected")
        self.gridLayout_xp3.addWidget(self.noCas, 2, 0, 1, 1)
        
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_xp3.addItem(spacerItem3, 3, 0, 1, 1)
        self.monWidget.addWidget(self.SxPage3)
        
        
    def setTime(self, tRun):
        self.time.setText(tRun)
        
        