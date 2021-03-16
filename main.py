from PyQt5.QtWidgets import QApplication
import sys
from showWindow import Main

# 常数
FACEPP_FILE = 'facepp.png'
VIDEO_DEVICE = 0
VIDEO_WIDTH = 350
VIDEO_HEIGHT = 240
ARDUINO_URL = 'http://192.168.1.61'
FACESET = 'FlagPP'
# FACESET = 'faceplusplus'

from arduino import Arduino
arduino = Arduino(ARDUINO_URL)

from speech import Speech
speaker = Speech()

from face_detection import FaceDetection

app = QApplication(sys.argv)  # 创建GUI对象
main = Main()  # 创建主窗体ui类对象

from video_capture import VideoCapture
videoCapture = VideoCapture(VIDEO_WIDTH, VIDEO_HEIGHT, FACEPP_FILE, VIDEO_DEVICE, main)

facepp = FaceDetection(FACESET, FACEPP_FILE, main, speaker, arduino)

def exit():
    print('exiting...')
    sys.exit()  # 除非退出程序关闭窗体，否则一直运行

main.show()  # 显示主窗体
videoCapture.drawPicture()
speaker.speakMsg("欢迎来到天马星空")
main.pushButton_exit.clicked.connect(exit)
main.identification.clicked.connect(facepp.identify)
main.pushButton_pz.clicked.connect(facepp.addFace)
main.pushButton_delete.clicked.connect(facepp.deleteFace)
while (True):
    videoCapture.drawPicture()
    videoCapture.waitKey()