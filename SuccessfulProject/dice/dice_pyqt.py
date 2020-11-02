import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from random import randint

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(350, 150)
        # 定义数量、最大值、附加值、计算按钮
        self.number_label = QLabel('个数：', self)
        self.max_label = QLabel('面数：', self)
        self.other_label = QLabel('调整值：', self)
        self.number_line = QLineEdit(self)
        self.max_line = QLineEdit(self)
        self.other_line = QLineEdit(self)
        self.sum_button = QPushButton('点击求和：', self)
        self.sum_line = QLineEdit(self)
        # 将clean按钮连接到功能函数
        self.clear_button = QPushButton('重置', self)
        self.clear_button_all = QPushButton('重置所有', self)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button_all.clicked.connect(self.clear)
        # 将sum按钮连接到功能函数
        self.sum_button.clicked.connect(self.roll_one_type)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # 初始化
        self.pushbutton_init()
        self.lineedit_init()
        self.layout_init()

    def layout_init(self):
        # 定义数量
        self.grid_layout.addWidget(self.number_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.number_line, 0, 1, 1, 1)
        # 定义最大值
        self.grid_layout.addWidget(self.max_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.max_line, 1, 1, 1, 1)
        # 定义附加值
        self.grid_layout.addWidget(self.other_label, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.other_line, 2, 1, 1, 1)
        # 计算按钮
        self.grid_layout.addWidget(self.sum_button, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.sum_line, 3, 1, 1, 1)
        # 清楚按钮
        self.grid_layout.addWidget(self.clear_button, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.clear_button_all, 4, 1, 1, 1)

        # 将clear加入水平布局
        self.h_layout.addWidget(self.clear_button)
        self.h_layout.addWidget(self.clear_button_all)
        # 大的垂直布局
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        """检查line内容不为空"""
        self.number_line.setPlaceholderText('请输入个数')
        self.max_line.setPlaceholderText('请输入面数')
        self.other_line.setPlaceholderText('请输入附加值')

        self.number_line.textChanged.connect(self.check_input_func)
        self.max_line.textChanged.connect(self.check_input_func)
        self.sum_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        # 检查number和max不为空
        if self.number_line.text() and self.max_line.text():
            self.sum_button.setEnabled(True)
        else:
            self.sum_button.setEnabled(False)

    def pushbutton_init(self):
        """将sum按钮置为false"""
        self.sum_button.setEnabled(False)
        
    def clear(self):
        """清除一些line，保留附加值"""
        self.number_line.clear()
        self.max_line.clear()
        self.sum_line.clear()

    def clear_all(self):
        """清除所有line"""
        self.number_line.clear()
        self.max_line.clear()
        self.sum_line.clear()
        self.other_line.clear()

    def roll_one_type(self):
        """同一类型的多次roll"""
        sum_roll = 0
        i = 1
        #循环体实现同类型相加
        max = int(self.max_line.text())
        time = int(self.number_line.text())
        while True:
            if i >= 1 and i <= int(time):
                ran = randint(1, max)
                sum_roll += ran
                i += 1
                continue
            break
        if self.other_line.text():
            sum_roll += int(self.other_line.text())
        self.sum_line.setText(str(sum_roll))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())