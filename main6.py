from PyQt5.QtWidgets import QApplication
import sys
from showWindow import Main

def detect():
    print('this is detect')

app = QApplication(sys.argv)  # 创建GUI对象
main = Main()  # 创建主窗体ui类对象

main.identification.clicked.connect(detect)

main.show()  # 显示主窗体

sys.exit(app.exec_())