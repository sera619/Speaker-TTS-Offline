import sys,os
from PySide6 import QtWidgets, QtCore, QtGui
from src.MainWindow import Ui_MainWindow
from settings import SETTINGS
import pyttsx3


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle(SETTINGS['title'])
        self.versionLabel.setText(f"Version {SETTINGS['version']} 2023 by {SETTINGS['author']}")
        self.engine = pyttsx3.init()
        self.volume = self.engine.getProperty('volume')
        self.rate = self.engine.getProperty('rate')
        self.valumeEdit.setValidator(QtGui.QDoubleValidator(0.1, 1.0, 2))
        self.rateEdit.setValidator(QtGui.QDoubleValidator(10, 500, 2))
        self.formatList = [".mp3", ".wav", '.ogg', '.aac', '.flac']
        self.currentSavepathLabel.setText(os.getcwd()+SETTINGS["savepath"])
        self.convertTextEdit.setPlaceholderText("Bitte gebe hier deinen Text ein den du in eine Audioausgabe umwandeln möchtest...")
        self.setupFileSystem(os.getcwd()+SETTINGS["savepath"])
        self.setupButtons()
        self.setupDials()
        self.resetOptions()
        self.fileKovertList = []
        
    def setupDials(self):
        self.rateDial.setMaximum(500)
        self.rateDial.setMinimum(0)
        self.rateDial.setValue(self.rate)
        self.rateDial.valueChanged.connect(self.changeRate)
        self.volumeDial.setMaximum(10)
        self.volumeDial.setMinimum(0)
        self.volumeDial.setValue(self.volume)
        self.volumeDial.valueChanged.connect(self.changeVolume)
        
    def setupButtons(self):
        self.changeSavepathBtn.clicked.connect(self.chooseFolderClicked)
        self.uploadTxtBtn.clicked.connect(self.uploadTextClicked)
        self.miniBtnExit.clicked.connect(sys.exit)
        self.speakBtn.clicked.connect(self.speakTextClicked)
        self.saveBtn.clicked.connect(self.saveAudioClicked)
        self.miniBtnMinimode.clicked.connect(self.showMinimized)
        voices = self.engine.getProperty('voices')
        voicelist = []
        for i in voices:
            voicelist.append(i.name)
        self.selectVoiceBox.addItems(voicelist)
        self.selectVoiceBox.currentTextChanged.connect(self.changeVoice)
        self.multiBtn.clicked.connect(self.switchButtonClick)
        self.multiUploadBtn.clicked.connect(self.uploadMultiEvent)
        self.eraseUploadBtn.clicked.connect(self.removeEntry)
        self.saveMultiBtn.clicked.connect(self.mulipleConvert)
        for i in self.formatList:
            self.formatComboBox.addItem(i)
        self.kovertProgressbar.setValue(0)
        self.kovertProgressbar.setVisible(False)
        self.resetOptionBtn.clicked.connect(self.resetOptions)
        self.openPathBtn.clicked.connect(self.openSavePath)
        self.playDemoBtn.clicked.connect(self.playDemo)

    def setupFileSystem(self, path):
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)
    
    def openSavePath(self):
        path = self.currentSavepathLabel.text()
        os.system(f'explorer.exe "{path}"')

    def switchButtonClick(self):
        if self.stackedWidget.currentWidget() == self.singleKovertPage:
            self.stackedWidget.setCurrentWidget(self.multiKonvertPage)
            self.multiBtn.setText("Single-Konvertieren")
            self.saveBtn.setEnabled(False)
            self.uploadTxtBtn.setEnabled(False)
            self.speakBtn.setEnabled(False)
            
        elif self.stackedWidget.currentWidget() == self.multiKonvertPage:
            self.saveBtn.setEnabled(True)
            self.speakBtn.setEnabled(True)
            self.uploadTxtBtn.setEnabled(True)
            self.stackedWidget.setCurrentWidget(self.singleKovertPage)
            self.fileKovertList.clear()
            self.multiBtn.setText("Multi-Konvertieren")

    def showNotification(self, title, text):
        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.addButton("OK", QtWidgets.QMessageBox.AcceptRole)
        msgBox.exec()

    def chooseFolderClicked(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', '', options=options)
        if folder_path:
            self.currentSavepathLabel.setText(f'{folder_path}')
            
    def uploadTextClicked(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', '', options=options)
        if filePath:
            with open(filePath, "r") as f:
                text = f.read()
                self.convertTextEdit.setPlainText(text)

    def speakTextClicked(self):
        if self.convertTextEdit != "":
            self.engine.say(self.convertTextEdit.toPlainText())
            self.engine.runAndWait()
        else:
            self.showNotification("Fehler", "Bitte gebe einen Text zum konvertieren ein!")
            
    def saveAudioClicked(self):
        if self.convertTextEdit != "":
            if self.filenameEdit.text() != "":
                filename = self.filenameEdit.text()
                print(filename)
                self.engine.save_to_file(self.convertTextEdit.toPlainText(), SETTINGS['savepath']+filename+self.formatComboBox.currentText())
                self.engine.runAndWait()
                self.convertTextEdit.clear()
                self.showNotification("Information", "Text wurde erfolgreich konvertiert!")
            else:
                self.showNotification("Fehler", "Bitte gebe einen Dateinamen ein!")               
        else:
            self.showNotification("Fehler", "Bitte gebe einen Text zum konvertieren ein!")

    def changeRate(self, value):
        self.rate = value
        self.rateEdit.setText(f"{self.rate}")
        self.engine.setProperty('rate', self.rate)

    def changeVolume(self, value):
        self.volume = value /10
        self.engine.setProperty('volume', self.volume)
        self.valumeEdit.setText(f"{self.volume}")

    def changeVoice(self, value):
        print(value)
        voices = self.engine.getProperty('voices')
        for i in voices:
            if i.name == value:
                self.engine.setProperty('voice', i.id)
                break
    
    def uploadMultiEvent(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_paths, _ = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select files', '', options=options)

        if file_paths:
            for file_path in file_paths:
                item = QtWidgets.QListWidgetItem(file_path)
                self.filelistView.addItem(item)
                self.fileKovertList.append(file_path)
    
    def removeEntry(self):
        itemToRemove = self.filelistView.currentItem()
        if itemToRemove:
            self.fileKovertList.remove(itemToRemove.text())
            self.filelistView.takeItem(self.filelistView.row(itemToRemove))

    def mulipleConvert(self):
        if len(self.fileKovertList) < 0:
            if self.filenameEdit.text() != "":
                count = 0
                self.kovertProgressbar.setMaximum(len(self.fileKovertList))
                self.kovertProgressbar.setValue(0)
                self.kovertProgressbar.setVisible(True)
                for file in self.fileKovertList:
                    count += 1
                    self.kovertProgressbar.setValue(count)
                    with open(file, 'r') as f:
                        text = f.read()
                        filename = self.filenameEdit.text() + f"-{count}"+ self.formatComboBox.currentText()
                        self.engine.save_to_file(text, SETTINGS['savepath']+filename)
                        self.engine.runAndWait()
                    
                self.fileKovertList.clear()
                self.filelistView.clear()
                self.filenameEdit.setText("")
                self.showNotification("Abgeschlossen", f"Es wurden {count} Datei(n) konvertiert!")
                self.kovertProgressbar.setVisible(False)
            else:
                self.showNotification("Fehler", "Bitte gebe einen gewünschten Dateinamen ein.")
        else:
            self.showNotification("Fehler", "Es konnte keine Textdatei zum konvertieren gefunden werden.")

    def playDemo(self):
        self.engine.say(SETTINGS['testText'])
        self.engine.runAndWait()

    def resetOptions(self):
        self.changeVolume(10)
        self.volumeDial.setValue(10)
        self.rateDial.setValue(175)
        self.changeRate(175)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__":
    main()