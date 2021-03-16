from PyQt5 import QtWidgets

class PopupMsg:

    def popupmsg(self, msg_text, msg_title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(msg_text)
        msg.setWindowTitle(msg_title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()