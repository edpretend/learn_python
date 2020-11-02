import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if __name__ == '__main__':
    # 创建QApplication实例，sys用于获得main参数，main函数调用GUI的api
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()

    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(500, 350)
    # 移动窗口
    w.move(500,250)
    # 设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')

    # 显示窗口
    w.show()

    # 进入程序的主循环，并通过exit()函数确保主循环安全结束
    sys.exit(app.exec_())

