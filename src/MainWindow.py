# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDial, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import src.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 795)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	border-radius: 15px;\n"
"	background-color: rgba(31, 31, 31, 120);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headFrame = QFrame(self.centralwidget)
        self.headFrame.setObjectName(u"headFrame")
        self.headFrame.setFrameShape(QFrame.StyledPanel)
        self.headFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftHeadFrame = QFrame(self.headFrame)
        self.leftHeadFrame.setObjectName(u"leftHeadFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftHeadFrame.sizePolicy().hasHeightForWidth())
        self.leftHeadFrame.setSizePolicy(sizePolicy)
        self.leftHeadFrame.setFrameShape(QFrame.StyledPanel)
        self.leftHeadFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftHeadFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 4, 0, 4)
        self.headLabel = QLabel(self.leftHeadFrame)
        self.headLabel.setObjectName(u"headLabel")
        font = QFont()
        font.setFamilies([u"Xeron"])
        font.setPointSize(48)
        self.headLabel.setFont(font)

        self.verticalLayout.addWidget(self.headLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.versionLabel = QLabel(self.leftHeadFrame)
        self.versionLabel.setObjectName(u"versionLabel")
        font1 = QFont()
        font1.setFamilies([u"Xeron"])
        font1.setPointSize(11)
        self.versionLabel.setFont(font1)
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.versionLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.leftHeadFrame)

        self.miniMenuFrame = QFrame(self.headFrame)
        self.miniMenuFrame.setObjectName(u"miniMenuFrame")
        self.miniMenuFrame.setStyleSheet(u"QButton{\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.miniMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.miniMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.miniMenuFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.miniBtnMinimode = QPushButton(self.miniMenuFrame)
        self.miniBtnMinimode.setObjectName(u"miniBtnMinimode")
        self.miniBtnMinimode.setMinimumSize(QSize(30, 30))
        self.miniBtnMinimode.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icons/basic_download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniBtnMinimode.setIcon(icon)

        self.horizontalLayout.addWidget(self.miniBtnMinimode, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.miniBtnMinimize = QPushButton(self.miniMenuFrame)
        self.miniBtnMinimize.setObjectName(u"miniBtnMinimize")
        self.miniBtnMinimize.setEnabled(True)
        self.miniBtnMinimize.setMinimumSize(QSize(30, 30))
        self.miniBtnMinimize.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/basic_display.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniBtnMinimize.setIcon(icon1)

        self.horizontalLayout.addWidget(self.miniBtnMinimize, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.miniBtnExit = QPushButton(self.miniMenuFrame)
        self.miniBtnExit.setObjectName(u"miniBtnExit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.miniBtnExit.sizePolicy().hasHeightForWidth())
        self.miniBtnExit.setSizePolicy(sizePolicy1)
        self.miniBtnExit.setMinimumSize(QSize(30, 30))
        self.miniBtnExit.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/basic_ban.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniBtnExit.setIcon(icon2)

        self.horizontalLayout.addWidget(self.miniBtnExit, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.miniMenuFrame)


        self.verticalLayout_2.addWidget(self.headFrame)

        self.midFrame = QFrame(self.centralwidget)
        self.midFrame.setObjectName(u"midFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.midFrame.sizePolicy().hasHeightForWidth())
        self.midFrame.setSizePolicy(sizePolicy2)
        self.midFrame.setFrameShape(QFrame.StyledPanel)
        self.midFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.midFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.midFrame)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.leftFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.multiBtn = QPushButton(self.frame_6)
        self.multiBtn.setObjectName(u"multiBtn")
        self.multiBtn.setEnabled(True)
        self.multiBtn.setMinimumSize(QSize(110, 0))
        self.multiBtn.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")

        self.verticalLayout_9.addWidget(self.multiBtn, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.optionFrame = QFrame(self.frame)
        self.optionFrame.setObjectName(u"optionFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.optionFrame.sizePolicy().hasHeightForWidth())
        self.optionFrame.setSizePolicy(sizePolicy3)
        self.optionFrame.setMinimumSize(QSize(250, 0))
        self.optionFrame.setMaximumSize(QSize(250, 16777215))
        self.optionFrame.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.optionFrame.setFrameShape(QFrame.StyledPanel)
        self.optionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.optionFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.speakBtn = QPushButton(self.optionFrame)
        self.speakBtn.setObjectName(u"speakBtn")
        self.speakBtn.setMinimumSize(QSize(110, 0))

        self.verticalLayout_7.addWidget(self.speakBtn, 0, Qt.AlignHCenter)

        self.saveBtn = QPushButton(self.optionFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(110, 0))

        self.verticalLayout_7.addWidget(self.saveBtn, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.optionFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.filenameEdit = QLineEdit(self.frame_7)
        self.filenameEdit.setObjectName(u"filenameEdit")
        self.filenameEdit.setMinimumSize(QSize(190, 0))
        self.filenameEdit.setMaximumSize(QSize(190, 16777215))
        self.filenameEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.filenameEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.optionFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_8)

        self.formatComboBox = QComboBox(self.frame_12)
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.verticalLayout_17.addWidget(self.formatComboBox, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_8 = QFrame(self.optionFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.uploadTxtBtn = QPushButton(self.frame_8)
        self.uploadTxtBtn.setObjectName(u"uploadTxtBtn")
        self.uploadTxtBtn.setMinimumSize(QSize(110, 0))
        self.uploadTxtBtn.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_10.addWidget(self.uploadTxtBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.optionFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.currentSavepathLabel = QLabel(self.frame_3)
        self.currentSavepathLabel.setObjectName(u"currentSavepathLabel")
        self.currentSavepathLabel.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Terminator Two\";\n"
"	color: rgb(0, 167, 250);\n"
"}")
        self.currentSavepathLabel.setAlignment(Qt.AlignCenter)
        self.currentSavepathLabel.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.currentSavepathLabel)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.changeSavepathBtn = QPushButton(self.frame_14)
        self.changeSavepathBtn.setObjectName(u"changeSavepathBtn")
        self.changeSavepathBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_4.addWidget(self.changeSavepathBtn)

        self.openPathBtn = QPushButton(self.frame_14)
        self.openPathBtn.setObjectName(u"openPathBtn")

        self.horizontalLayout_4.addWidget(self.openPathBtn)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_7.addWidget(self.frame_3, 0, Qt.AlignVCenter)

        self.frame_4 = QFrame(self.optionFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 4, 0, 4)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.selectVoiceBox = QComboBox(self.frame_4)
        self.selectVoiceBox.setObjectName(u"selectVoiceBox")

        self.verticalLayout_11.addWidget(self.selectVoiceBox)

        self.playDemoBtn = QPushButton(self.frame_4)
        self.playDemoBtn.setObjectName(u"playDemoBtn")
        self.playDemoBtn.setMinimumSize(QSize(110, 0))

        self.verticalLayout_11.addWidget(self.playDemoBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_13 = QFrame(self.optionFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.valumeLabel = QLabel(self.frame_2)
        self.valumeLabel.setObjectName(u"valumeLabel")
        self.valumeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.valumeLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.valumeEdit = QLineEdit(self.frame_2)
        self.valumeEdit.setObjectName(u"valumeEdit")
        self.valumeEdit.setMaximumSize(QSize(60, 16777215))
        self.valumeEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.valumeEdit, 0, Qt.AlignHCenter)

        self.volumeDial = QDial(self.frame_2)
        self.volumeDial.setObjectName(u"volumeDial")
        self.volumeDial.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.volumeDial, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_13)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.rateLabel = QLabel(self.frame_5)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.rateLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rateEdit = QLineEdit(self.frame_5)
        self.rateEdit.setObjectName(u"rateEdit")
        self.rateEdit.setMaximumSize(QSize(60, 16777215))
        self.rateEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.rateEdit, 0, Qt.AlignHCenter)

        self.rateDial = QDial(self.frame_5)
        self.rateDial.setObjectName(u"rateDial")
        self.rateDial.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.rateDial, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.frame_5)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.helpBtn = QPushButton(self.frame_19)
        self.helpBtn.setObjectName(u"helpBtn")

        self.horizontalLayout_11.addWidget(self.helpBtn)

        self.resetOptionBtn = QPushButton(self.frame_19)
        self.resetOptionBtn.setObjectName(u"resetOptionBtn")
        self.resetOptionBtn.setMinimumSize(QSize(110, 0))
        self.resetOptionBtn.setMaximumSize(QSize(110, 16777215))
        self.resetOptionBtn.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.resetOptionBtn)


        self.verticalLayout_18.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_6.addWidget(self.optionFrame)


        self.horizontalLayout_6.addWidget(self.frame, 0, Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.midFrame)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.rightFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_19 = QVBoxLayout(self.helpPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_16 = QFrame(self.helpPage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_20.addWidget(self.label_10)

        self.helpTextLabel = QLabel(self.frame_16)
        self.helpTextLabel.setObjectName(u"helpTextLabel")
        sizePolicy2.setHeightForWidth(self.helpTextLabel.sizePolicy().hasHeightForWidth())
        self.helpTextLabel.setSizePolicy(sizePolicy2)
        self.helpTextLabel.setStyleSheet(u"	font: 14pt \"Terminator Two\";\n"
"color: white;")
        self.helpTextLabel.setAlignment(Qt.AlignCenter)
        self.helpTextLabel.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.helpTextLabel)

        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_11)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.githubBtn = QPushButton(self.frame_18)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_10.addWidget(self.githubBtn, 0, Qt.AlignHCenter)

        self.ytBtn = QPushButton(self.frame_18)
        self.ytBtn.setObjectName(u"ytBtn")
        self.ytBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_10.addWidget(self.ytBtn, 0, Qt.AlignHCenter)

        self.thmBtn = QPushButton(self.frame_18)
        self.thmBtn.setObjectName(u"thmBtn")
        self.thmBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_10.addWidget(self.thmBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_18, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.helpBackBtn = QPushButton(self.frame_17)
        self.helpBackBtn.setObjectName(u"helpBackBtn")
        self.helpBackBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_9.addWidget(self.helpBackBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_17)


        self.verticalLayout_19.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.helpPage)
        self.singleKovertPage = QWidget()
        self.singleKovertPage.setObjectName(u"singleKovertPage")
        self.verticalLayout_5 = QVBoxLayout(self.singleKovertPage)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.inputFrame = QFrame(self.singleKovertPage)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inputFrame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.inputFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")

        self.verticalLayout_3.addWidget(self.label)

        self.convertTextEdit = QPlainTextEdit(self.inputFrame)
        self.convertTextEdit.setObjectName(u"convertTextEdit")

        self.verticalLayout_3.addWidget(self.convertTextEdit)


        self.verticalLayout_5.addWidget(self.inputFrame)

        self.stackedWidget.addWidget(self.singleKovertPage)
        self.multiKonvertPage = QWidget()
        self.multiKonvertPage.setObjectName(u"multiKonvertPage")
        self.multiKonvertPage.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: 1px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.verticalLayout_16 = QVBoxLayout(self.multiKonvertPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.multiKonvertPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: 1px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_7.setText(u"Mehrere Datein Hochladen")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_7)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.saveMultiBtn = QPushButton(self.frame_15)
        self.saveMultiBtn.setObjectName(u"saveMultiBtn")
        self.saveMultiBtn.setMinimumSize(QSize(110, 0))
        self.saveMultiBtn.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_8.addWidget(self.saveMultiBtn)

        self.multiUploadBtn = QPushButton(self.frame_15)
        self.multiUploadBtn.setObjectName(u"multiUploadBtn")
        self.multiUploadBtn.setMinimumSize(QSize(110, 0))
        self.multiUploadBtn.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_8.addWidget(self.multiUploadBtn)

        self.eraseUploadBtn = QPushButton(self.frame_15)
        self.eraseUploadBtn.setObjectName(u"eraseUploadBtn")
        self.eraseUploadBtn.setMinimumSize(QSize(110, 0))
        self.eraseUploadBtn.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_8.addWidget(self.eraseUploadBtn)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.kovertProgressbar = QProgressBar(self.frame_11)
        self.kovertProgressbar.setObjectName(u"kovertProgressbar")
        self.kovertProgressbar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid red;\n"
"    border-radius: 5px;\n"
"	background-color: rgb(97, 97, 97);\n"
"	text-align: center;\n"
"	color: white;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"}")
        self.kovertProgressbar.setValue(24)

        self.verticalLayout_15.addWidget(self.kovertProgressbar)

        self.filelistView = QListWidget(self.frame_11)
        self.filelistView.setObjectName(u"filelistView")

        self.verticalLayout_15.addWidget(self.filelistView)


        self.verticalLayout_13.addWidget(self.frame_11)


        self.verticalLayout_14.addWidget(self.frame_10)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_20 = QFrame(self.multiKonvertPage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_9)

        self.dataTableWidget = QTableWidget(self.frame_20)
        if (self.dataTableWidget.columnCount() < 3):
            self.dataTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font2 = QFont()
        font2.setKerning(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.dataTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.dataTableWidget.setAlternatingRowColors(True)
        self.dataTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dataTableWidget.setTextElideMode(Qt.ElideMiddle)
        self.dataTableWidget.setWordWrap(True)
        self.dataTableWidget.setColumnCount(3)
        self.dataTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.dataTableWidget.horizontalHeader().setMinimumSectionSize(57)
        self.dataTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_21.addWidget(self.dataTableWidget)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.clearOutputBtn = QPushButton(self.frame_21)
        self.clearOutputBtn.setObjectName(u"clearOutputBtn")
        self.clearOutputBtn.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_12.addWidget(self.clearOutputBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_21)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.multiKonvertPage)
        self.eqPage = QWidget()
        self.eqPage.setObjectName(u"eqPage")
        self.verticalLayout_28 = QVBoxLayout(self.eqPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_22 = QFrame(self.eqPage)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_12)


        self.verticalLayout_28.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.eqPage)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.savedListWidget = QListWidget(self.frame_23)
        self.savedListWidget.setObjectName(u"savedListWidget")

        self.horizontalLayout_13.addWidget(self.savedListWidget)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_24)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.saveEqBtn = QPushButton(self.frame_24)
        self.saveEqBtn.setObjectName(u"saveEqBtn")

        self.verticalLayout_22.addWidget(self.saveEqBtn)

        self.deleteEqBtn = QPushButton(self.frame_24)
        self.deleteEqBtn.setObjectName(u"deleteEqBtn")

        self.verticalLayout_22.addWidget(self.deleteEqBtn)

        self.copyBtn = QPushButton(self.frame_24)
        self.copyBtn.setObjectName(u"copyBtn")

        self.verticalLayout_22.addWidget(self.copyBtn)

        self.eqBtn = QPushButton(self.frame_24)
        self.eqBtn.setObjectName(u"eqBtn")
        self.eqBtn.setMinimumSize(QSize(110, 0))
        self.eqBtn.setStyleSheet(u" QPushButton {\n"
"		background-color:none;\n"
"                border: .5px solid #ff3333;\n"
"				\n"
"	color: rgb(255, 0, 0);\n"
"			padding:3 15;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              		background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 1 #C0392B,                              \n"
"		stop: 0 #E74C3C );\n"
"color:white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    	stop: 0 #C0392B,                              \n"
"		stop: 1 #E74C3C );\n"
"	color:white;            \n"
"}\n"
" QPushButton:disabled {\n"
"        background-color: none;\n"
"        border-color: #aaaaaa;\n"
"        color: #666666;\n"
"    }")

        self.verticalLayout_22.addWidget(self.eqBtn)


        self.horizontalLayout_13.addWidget(self.frame_24, 0, Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.eqPage)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_27)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSlider = QSlider(self.frame_27)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_23.addWidget(self.verticalSlider, 0, Qt.AlignHCenter)

        self.lcdNumber = QLCDNumber(self.frame_27)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_23.addWidget(self.lcdNumber)


        self.horizontalLayout_14.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_28)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSlider_2 = QSlider(self.frame_28)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_24.addWidget(self.verticalSlider_2, 0, Qt.AlignHCenter)

        self.lcdNumber_2 = QLCDNumber(self.frame_28)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.verticalLayout_24.addWidget(self.lcdNumber_2)


        self.horizontalLayout_14.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_29)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSlider_3 = QSlider(self.frame_29)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.verticalLayout_25.addWidget(self.verticalSlider_3, 0, Qt.AlignHCenter)

        self.lcdNumber_3 = QLCDNumber(self.frame_29)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.verticalLayout_25.addWidget(self.lcdNumber_3)


        self.horizontalLayout_14.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSlider_4 = QSlider(self.frame_30)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.verticalLayout_26.addWidget(self.verticalSlider_4, 0, Qt.AlignHCenter)

        self.lcdNumber_4 = QLCDNumber(self.frame_30)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")

        self.verticalLayout_26.addWidget(self.lcdNumber_4)


        self.horizontalLayout_14.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_26)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_31)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSlider_5 = QSlider(self.frame_31)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.verticalLayout_27.addWidget(self.verticalSlider_5, 0, Qt.AlignHCenter)

        self.lcdNumber_5 = QLCDNumber(self.frame_31)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")

        self.verticalLayout_27.addWidget(self.lcdNumber_5)


        self.horizontalLayout_14.addWidget(self.frame_31)


        self.verticalLayout_28.addWidget(self.frame_26)

        self.frame_32 = QFrame(self.eqPage)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.eqEffectBox = QComboBox(self.frame_32)
        self.eqEffectBox.setObjectName(u"eqEffectBox")

        self.horizontalLayout_15.addWidget(self.eqEffectBox)

        self.playEqBtn = QPushButton(self.frame_32)
        self.playEqBtn.setObjectName(u"playEqBtn")

        self.horizontalLayout_15.addWidget(self.playEqBtn)


        self.verticalLayout_28.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.eqPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.rightFrame)


        self.verticalLayout_2.addWidget(self.midFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.headLabel.setText(QCoreApplication.translate("MainWindow", u"Speaker ", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.4", None))
        self.miniBtnMinimode.setText("")
        self.miniBtnMinimize.setText("")
        self.miniBtnExit.setText("")
        self.multiBtn.setText(QCoreApplication.translate("MainWindow", u"Multi-Konvertieren", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Optionen", None))
        self.speakBtn.setText(QCoreApplication.translate("MainWindow", u"Sprechen", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Datei Name", None))
        self.filenameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Datei Format", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Textdatei laden", None))
        self.uploadTxtBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speicherpfad", None))
        self.currentSavepathLabel.setText(QCoreApplication.translate("MainWindow", u"current path", None))
        self.changeSavepathBtn.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.openPathBtn.setText(QCoreApplication.translate("MainWindow", u"\u00d6ffnen", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stimme", None))
        self.playDemoBtn.setText(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.valumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.rateLabel.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.resetOptionBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.helpTextLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">- Geben Sie den Text ein, den Sie in eine Audio-Datei umwandeln m\u00f6chten.</span></p><p><span style=\" font-size:12pt;\">- Passen Sie die Sprechgeschwindigkeit und Lautst\u00e4rke nach Bedarf an.</span></p><p><span style=\" font-size:12pt;\">- W\u00e4hlen Sie das gew\u00fcnschte Audioformat aus der Dropdown-Liste aus.</span></p><p><span style=\" font-size:12pt;\">- Klicken Sie auf die Schaltfl\u00e4che &quot;Sprechen&quot; oder &quot;Speichern&quot;, um den Text in Sprache umzuwandeln und anzuh\u00f6ren oder zu speichern.</span></p><p><span style=\" font-size:12pt;\">- Um zur Mehrfachkonvertierung zu wechseln, klicken Sie auf die Schaltfl\u00e4che &quot;Multi-Konvertieren&quot;/&quot;Single-Konvertieren&quot;</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.githubBtn.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.ytBtn.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.thmBtn.setText(QCoreApplication.translate("MainWindow", u"TryHackMe", None))
        self.helpBackBtn.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fcck", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text zum Konvertieren:", None))
        self.saveMultiBtn.setText(QCoreApplication.translate("MainWindow", u"Konvertieren", None))
        self.multiUploadBtn.setText(QCoreApplication.translate("MainWindow", u"Hinzuf\u00fcgen", None))
        self.eraseUploadBtn.setText(QCoreApplication.translate("MainWindow", u"Entfernen", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Datein im Speicherpfad", None))
        ___qtablewidgetitem = self.dataTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.dataTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Typ", None));
        ___qtablewidgetitem2 = self.dataTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gr\u00f6\u00dfe", None));
        self.clearOutputBtn.setText(QCoreApplication.translate("MainWindow", u"Bereinigen", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.saveEqBtn.setText(QCoreApplication.translate("MainWindow", u"Laden", None))
        self.deleteEqBtn.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.copyBtn.setText(QCoreApplication.translate("MainWindow", u"Kopieren", None))
        self.eqBtn.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.playEqBtn.setText(QCoreApplication.translate("MainWindow", u"Abspielen", None))
    # retranslateUi

