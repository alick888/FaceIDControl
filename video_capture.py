import cv2
from PyQt5 import QtGui

class VideoCapture:
    def __init__(self, width, height, faceppFile, device, main):
        self.cap = cv2.VideoCapture(device)
        self.faceppFile = faceppFile
        self.dim = (width, height)
        self.main = main

    def drawPicture(self):
        ret, frame = self.cap.read()
        resized = cv2.resize(frame, self.dim)
        cv2.imwrite(self.faceppFile, resized)
        input_img = QtGui.QPixmap(self.faceppFile)
        self.main.canvas.setPixmap(input_img)

    def waitKey(self):
        return cv2.waitKey(0)