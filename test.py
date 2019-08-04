from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
 
#继承QThread
 
class Mythread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(int)
 
    def __init__(self, parent=None):
        super().__init__(parent)
        # 下面的初始化方法都可以，有的python版本不支持
        #  super(Mythread, self).__init__()
 
    def run(self):
            #要定义的行为，比如开始一个活动什么的
 
            for i in range(1, 1000):
 
                print(i)
                self.breakSignal.emit(i)
                time.sleep(1)
            
 
 
if __name__ == '__main__':
    app = QApplication([])
    dlg = QDialog()
    dlg.resize(400, 300)
    dlg.setWindowTitle("自定义按钮测试")
    dlgLayout = QVBoxLayout()
    dlgLayout.setContentsMargins(40, 40, 40, 40)
    btn = QPushButton('测试按钮')
    dlgLayout.addWidget(btn)
    dlgLayout.addStretch(40)
    dlg.setLayout(dlgLayout)
    dlg.show()
 
 
    def chuli(a):
        # dlg.setWindowTitle(s)
        btn.setText(str(a))
 
    # 创建线程
    thread = Mythread()
    # # 注册信号处理函数
    thread.breakSignal.connect(chuli)
    # # 启动线程
    thread.start()
    dlg.exec_()
    app.exit()