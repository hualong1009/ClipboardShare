# -------------------------------------------------------------------
#   Author : HansenWang
#   Date : 2019/08/01
#   Description : Sharing clipboard in area network
#   Version : v1.0
#   history :
#       2019/08/01  v1.0
#       init
# -------------------------------------------------------------------


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from Clipboard_QT import Ui_MainWindow
import pyperclip, time, socket
from PyQt5.QtCore import QThread, pyqtSignal


class WorkThread(QThread):
    mySignal = pyqtSignal(list)
    def __init__(self, MainGui):
        super(WorkThread, self).__init__()
        self.MainGui = MainGui

    def run(self):
        while True:
            #if pyperclip.paste() != ""  and pyperclip.paste() not in self.MainGui.EditCopy:
            #    self.MainGui.EditCopy[1], self.MainGui.EditCopy[2] = self.MainGui.EditCopy[0], self.MainGui.EditCopy[1]
            #    self.MainGui.EditCopy[0] = pyperclip.paste()
            #    print(self.MainGui.EditCopy)
            self.mySignal.emit(self.MainGui.EditCopy)
            time.sleep(1)

class ShareThread(QThread):
    mySignal = pyqtSignal(list)
    def __init__(self, MainGui):
        super(ShareThread, self).__init__()
        self.MainGui = MainGui

    def run(self):
        shareClipboardData = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        shareClipboardData.bind(('', 9999))
        while True:
            data, addr = shareClipboardData.recvfrom(1024)
            print(data, addr)
            #if pyperclip.paste() != ""  and pyperclip.paste() not in self.MainGui.EditCopy:
            #    self.MainGui.EditCopy[1], self.MainGui.EditCopy[2] = self.MainGui.EditCopy[0], self.MainGui.EditCopy[1]
            #    self.MainGui.EditCopy[0] = pyperclip.paste()
            #    print(self.MainGui.EditCopy)
            self.mySignal.emit(self.MainGui.EditCopy)
            time.sleep(1)


class Clipboard_QT(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Clipboard_QT, self).__init__()
        self.setupUi(self)
        self.EditCopy = ["", "", ""]
        self.updateDataThread = WorkThread(self)
        self.shareClipboardData = ShareThread(self)
        self.updateDataThread.mySignal.connect(self.Update_EditBox)
        self.shareClipboardData.mySignal.connect(self.Update_EditBox)
        self.updateDataThread.start()
        self.shareClipboardData.start()
        self.actionCopyToClipboard_1.triggered.connect(self.CopyToClipboard_1)
        self.actionCopyToClipboard_2.triggered.connect(self.CopyToClipboard_2)
        self.actionCopyToClipboard_3.triggered.connect(self.CopyToClipboard_3)
        self.statusLable_2 = QLabel("Used to sharing clipboard            ")
        self.statusBar.addPermanentWidget(self.statusLable_2)
        self.statusLable_1 = QLabel("     Designed for Inspur by @HansenWang ")
        self.statusBar.addPermanentWidget(self.statusLable_1)

    def Update_EditBox(self, EditCopy):
        if pyperclip.paste() != "" and pyperclip.paste() not in self.EditCopy:
            self.EditCopy[1], self.EditCopy[2] = self.EditCopy[0], self.EditCopy[1]
            self.EditCopy[0] = pyperclip.paste()
            print(self.EditCopy)
            try:
                self.shareDataSocket.sendto(b"%s"% self.EditCopy, ('100.3.8.218', 9999))
            except:
                pass
            self.EditBox_1.setPlainText(self.EditCopy[0])
            self.EditBox_2.setPlainText(self.EditCopy[1])
            self.EditBox_3.setPlainText(self.EditCopy[2])

    def CopyToClipboard_1(self):
        self.EditCopy[0] = self.EditBox_1.toPlainText()
        self.EditBox_1.selectAll()
        self.EditBox_1.copy()
    def CopyToClipboard_2(self):
        self.EditCopy[1] = self.EditBox_2.toPlainText()
        self.EditBox_2.selectAll()
        self.EditBox_2.copy()
    def CopyToClipboard_3(self):
        self.EditCopy[2] = self.EditBox_3.toPlainText()
        self.EditBox_3.selectAll()
        self.EditBox_3.copy()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Clipboard_QT()
    win.show()
    sys.exit(app.exec_())