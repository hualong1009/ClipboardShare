# ----------------------------------------------------------------------------------------------------
#
#   Author : HansenWang
#   Date : 2019/08/01
#   Description : Sharing clipboard in area network
#   Version : v1.0
#   history :
#       2019/08/01  v1.0
#       init
#
# ----------------------------------------------------------------------------------------------------
#
# Copyright (c) [2019] ClipboardShare
# ClipboardShare is licensed under the Mulan PSL v1.
# You can use this software according to the terms and conditions of the Mulan PSL v1.
# You may obtain a copy of Mulan PSL v1 at:
#    http://license.coscl.org.cn/MulanPSL
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v1 for more details.
#
# ----------------------------------------------------------------------------------------------------


import sys, re, subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from Clipboard_QT import Ui_MainWindow
from connect_share import Ui_Dialog
import pyperclip, time, socket
from PyQt5.QtCore import QThread, pyqtSignal, Qt

hostIp = ""
hostPort = ""

class WorkThread(QThread):
    mySignal = pyqtSignal(list)
    def __init__(self, MainGui):
        super(WorkThread, self).__init__()
        self.MainGui = MainGui

    def run(self):
        while True:
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
            data, addr = shareClipboardData.recvfrom(102400)
            pyperclip.copy(eval(str(data.decode('utf-8')))[0])
            self.mySignal.emit(self.MainGui.EditCopy)
            time.sleep(1)


class Connect_QT(QDialog, Ui_Dialog):
    def __init__(self):
        super(Connect_QT, self).__init__()
        self.setupUi(self)
        self.lineEdit_2.setText("9999")
        self.pushButton.clicked.connect(self.testConnection)

    def testConnection(self):
        global hostIp
        global hostPort
        self.ip_addr = self.lineEdit.text()
        self.ip_port = self.lineEdit_2.text()
        if re.match('[1-9][0-9]{1,2}(.[0-9]{1,3}){3}', self.ip_addr):
            if sys.platform == "win32":
                if re.search('ms', subprocess.getoutput("ping -n 1 %s"% self.ip_addr)):
                    self.label_3.setStyleSheet("color:rgb(34,177,76)")
                    self.label_3.setText('PASS')
                    hostIp = self.ip_addr
                    hostPort = self.ip_port
                else:
                    self.label_3.setStyleSheet("color:rgb(237,28,36)")
                    self.label_3.setText("Ping failed, Pls check.")
            elif sys.platform == "linux":
                if re.search('ms', subprocess.getoutput("ping -c 1 %s"% self.ip_addr)):
                    self.label_3.setStyleSheet("color:rgb(34,177,76)")
                    self.label_3.setText('PASS')
                    hostIp = self.ip_addr
                    hostPort = self.ip_port
                else:
                    self.label_3.setStyleSheet("color:rgb(237,28,36)")
                    self.label_3.setText("Ping failed, Pls check.")
            else:
                self.label_3.setStyleSheet("color:rgb(237,28,36)")
                self.label_3.setText("Unknown OS type.")
        else:
            self.label_3.setStyleSheet("color:rgb(237,28,36)")
            self.label_3.setText("Wrong format IP.")


class Clipboard_QT(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Clipboard_QT, self).__init__()
        self.setupUi(self)
        self.child = Connect_QT()
        self.child.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.EditCopy = ["", "", ""]
        self.sendClipboardData = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.updateDataThread = WorkThread(self)
        self.shareClipboardData = ShareThread(self)
        self.updateDataThread.mySignal.connect(self.Update_EditBox)
        self.shareClipboardData.mySignal.connect(self.Update_EditBox)
        self.updateDataThread.start()
        self.shareClipboardData.start()
        self.actionCopyToClipboard_1.triggered.connect(self.CopyToClipboard_1)
        self.actionCopyToClipboard_2.triggered.connect(self.CopyToClipboard_2)
        self.actionCopyToClipboard_3.triggered.connect(self.CopyToClipboard_3)
        self.actionConnect.triggered.connect(self.child.show)
        self.statusLable_2 = QLabel("Used to sharing clipboard                ")
        self.statusLable_2.setAlignment(Qt.AlignLeft)
        self.statusBar.addPermanentWidget(self.statusLable_2)
        self.statusLable_1 = QLabel()
        self.statusLable_1.setText("Designed for Inspur by  <A href='https://hualong1009.github.io/about/'>@HansenWang</A>")
        self.statusBar.addPermanentWidget(self.statusLable_1)

    def connectShareHost(self):
        self.connect_UI = Connect_QT()


    def Update_EditBox(self, EditCopy):
        if pyperclip.paste() != "" and pyperclip.paste() not in self.EditCopy:
            self.EditCopy[1], self.EditCopy[2] = self.EditCopy[0], self.EditCopy[1]
            self.EditCopy[0] = pyperclip.paste()
            if hostIp != "":
                try:
                    self.sendClipboardData.sendto(b"%s"% str(self.EditCopy).encode('utf-8'), (hostIp, int(hostPort)))
                except Exception as e:
                    print(e)
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
    win.setWindowOpacity(0.9)
    win.show()
    sys.exit(app.exec_())