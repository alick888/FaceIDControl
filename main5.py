from PyQt5.QtWidgets import QApplication
import sys
from showWindow import Main
from PopupMsg import PopupMsg


popupmsg = PopupMsg()
FACEPPFILE = 'facepp.png'
VIDEO_DEVICE = 0
VIDEO_WIDTH = 350
VIDEO_HEIGHT = 240

from AIGate import AIGate
AIGATEURL = 'http://192.168.1.52'
aigate = AIGate(AIGATEURL)

def exit():
    popupmsg.popupmsg('exiting...', 'main')
    sys.exit()  # 除非退出程序关闭窗体，否则一直运行

def detect():
    print('detecting...')
    aigate.open_door()

def addFace():
    print('adding...')

def deleteFace():
    print('deleting...')

app = QApplication(sys.argv)  # 创建GUI对象
main = Main()  # 创建主窗体ui类对象

from video_capture import VideoCapture
videoCapture = VideoCapture(VIDEO_WIDTH, VIDEO_HEIGHT, FACEPPFILE, VIDEO_DEVICE, main)

main.show()  # 显示主窗体

main.pushButton_exit.clicked.connect(exit)
main.identification.clicked.connect(detect)
main.pushButton_pz.clicked.connect(addFace)
main.pushButton_delete.clicked.connect(deleteFace)

while (True):
    videoCapture.drawPicture()
    videoCapture.waitKey()

