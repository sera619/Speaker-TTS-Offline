import sys,os
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QThreadPool
from src.MainWindow import Ui_MainWindow
from worker import Worker
from settings import SETTINGS
import pyttsx3
import webbrowser

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'creativeDudes.speakertts.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

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
        self.lastPage = 1

        self.threadpool = QThreadPool()
        self.stackedWidget.setCurrentIndex(1)
        #print("Worker started with maximum %d threads" % self.threadpool.maxThreadCount())
    

    def generateTestFiles(self):
        texts = ["test1", "test2", "test3", "test4"]
        for t in texts:
            with open('test/'+ t + '.txt', "w") as f:
                f.write(t)
       
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

        self.miniBtnMinimize.setDisabled(True)
        #self.miniBtnMinimize.clicked.connect(self.generateTestFiles)
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
        self.helpBtn.clicked.connect(self.showHelp)
        self.helpBackBtn.clicked.connect(self.backFromHelp)
        self.githubBtn.clicked.connect(self.openGithub)
        self.ytBtn.clicked.connect(self.openYoutube)
        self.thmBtn.clicked.connect(self.openTHM)

    def runMultiKonvert(self):
        worker = Worker(self.mulipleConvert)
        self.threadpool.start(worker)
    
    def runPlayDemo(self):
        worker = Worker(self.playDemo)
        self.threadpool.start(worker)
    
    def runSaveAudio(self):
        worker = Worker(self.saveAudioClicked)
        self.threadpool.start(worker)
    
    def runSpeakText(self):
        worker = Worker(self.speakTextClicked)
        self.threadpool.start(worker)

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
        self.lastPage = self.stackedWidget.currentIndex()

    def showNotification(self, title, text):
        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.addButton("OK", QtWidgets.QMessageBox.AcceptRole)
        msgBox.setWindowIcon(QtGui.QIcon(os.path.join(basedir,'audio-cassette.ico')))
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
        filters = '*.txt'
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', '', options=options, filter=filters)
        if filePath:
            with open(filePath, "r") as f:
                text = f.read()
                self.convertTextEdit.setPlainText(text)

    def speakTextClicked(self):
        if self.convertTextEdit.toPlainText() != "":
            self.engine.say(self.convertTextEdit.toPlainText())
            self.engine.runAndWait()
        else:
            self.showNotification("Fehler", "Bitte gebe einen Text zum konvertieren ein!")
            
    def saveAudioClicked(self):
        if self.convertTextEdit != "":
            if self.filenameEdit.text() != "":
                filename = self.filenameEdit.text()
                self.engine.save_to_file(self.convertTextEdit.toPlainText(), SETTINGS['savepath']+filename+self.formatComboBox.currentText())
                self.engine.runAndWait()
                self.convertTextEdit.clear()
                self.filenameEdit.clear()
                self.showNotification("Abgeschlossen", "Text wurde erfolgreich konvertiert!")
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
        if len(self.filelistView.children()) > 0:
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
    
    def showHelp(self):
        self.lastPage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentWidget(self.helpPage)
    
    def backFromHelp(self):
        self.stackedWidget.setCurrentIndex(self.lastPage)

    def openGithub(self):
        webbrowser.open(SETTINGS['github'])
    
    def openYoutube(self):
        webbrowser.open(SETTINGS['youtube'])
    
    def openTHM(self):
        webbrowser.open(SETTINGS['thm'])

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir,'audio-cassette.ico')))
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon(os.path.join(basedir,'audio-cassette.ico')))
    window.show()
    app.exec()



if __name__ == "__main__":
    main()