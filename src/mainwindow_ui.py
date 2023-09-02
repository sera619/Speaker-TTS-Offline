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
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 593)
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headLabel = QLabel(self.leftHeadFrame)
        self.headLabel.setObjectName(u"headLabel")
        font = QFont()
        font.setFamilies([u"Xeron"])
        font.setPointSize(48)
        self.headLabel.setFont(font)

        self.verticalLayout.addWidget(self.headLabel, 0, Qt.AlignHCenter|Qt.AlignTop)


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
        self.miniBtnMinimode.setMinimumSize(QSize(25, 25))
        self.miniBtnMinimode.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icons/basic_download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniBtnMinimode.setIcon(icon)

        self.horizontalLayout.addWidget(self.miniBtnMinimode, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.miniBtnMinimize = QPushButton(self.miniMenuFrame)
        self.miniBtnMinimize.setObjectName(u"miniBtnMinimize")
        self.miniBtnMinimize.setMinimumSize(QSize(25, 25))
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
        self.miniBtnExit.setMinimumSize(QSize(25, 25))
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
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignTop)


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
        self.optionFrame.setFrameShape(QFrame.StyledPanel)
        self.optionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.optionFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.speakBtn = QPushButton(self.optionFrame)
        self.speakBtn.setObjectName(u"speakBtn")

        self.verticalLayout_7.addWidget(self.speakBtn, 0, Qt.AlignHCenter)

        self.saveBtn = QPushButton(self.optionFrame)
        self.saveBtn.setObjectName(u"saveBtn")

        self.verticalLayout_7.addWidget(self.saveBtn, 0, Qt.AlignHCenter)

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

        self.changeSavepathBtn = QPushButton(self.frame_3)
        self.changeSavepathBtn.setObjectName(u"changeSavepathBtn")

        self.verticalLayout_8.addWidget(self.changeSavepathBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_3, 0, Qt.AlignVCenter)

        self.frame_4 = QFrame(self.optionFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.optionFrame)
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

        self.volumeDial = QDial(self.frame_2)
        self.volumeDial.setObjectName(u"volumeDial")
        self.volumeDial.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.volumeDial, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.optionFrame)
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

        self.rateDial = QDial(self.frame_5)
        self.rateDial.setObjectName(u"rateDial")
        self.rateDial.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.rateDial, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.optionFrame)


        self.horizontalLayout_6.addWidget(self.frame, 0, Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.midFrame)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.rightFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Terminator Two\";\n"
"	color: rgb(255, 0, 0)\n"
"}")

        self.verticalLayout_4.addWidget(self.label)

        self.inputFrame = QFrame(self.rightFrame)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inputFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.convertTextEdit = QPlainTextEdit(self.inputFrame)
        self.convertTextEdit.setObjectName(u"convertTextEdit")

        self.verticalLayout_3.addWidget(self.convertTextEdit)


        self.verticalLayout_4.addWidget(self.inputFrame)


        self.horizontalLayout_7.addWidget(self.rightFrame)


        self.verticalLayout_2.addWidget(self.midFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.headLabel.setText(QCoreApplication.translate("MainWindow", u"Speaker ", None))
        self.miniBtnMinimode.setText("")
        self.miniBtnMinimize.setText("")
        self.miniBtnExit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Optionen", None))
        self.speakBtn.setText(QCoreApplication.translate("MainWindow", u"Abspielen", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Textdatei laden", None))
        self.uploadTxtBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speicherpfad", None))
        self.currentSavepathLabel.setText(QCoreApplication.translate("MainWindow", u"current path", None))
        self.changeSavepathBtn.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stimme", None))
        self.valumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.rateLabel.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text zum Konvertieren:", None))
    # retranslateUi

