import sys
# import 这里导入desiner设计的ui转换来的py文件
import demo
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if __name__ == '__main__':
    # 创建QApplication对象表示整个应用程序
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainWindow = QMainWindow()
# 创建转换来的py文件里的类的实例  ui = Main.ui_MainW()
    ui = demo.Ui_MainWindow()
# 创建类里的方法的控件，需要调用一个主窗口：
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())