# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROJ_INF_2_v2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PROJ_INF_2_v2DialogBase(object):
    def setupUi(self, PROJ_INF_2_v2DialogBase):
        PROJ_INF_2_v2DialogBase.setObjectName("PROJ_INF_2_v2DialogBase")
        PROJ_INF_2_v2DialogBase.resize(967, 756)
        self.button_box = QtWidgets.QDialogButtonBox(PROJ_INF_2_v2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(420, 690, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mMapLayerComboBox = QgsMapLayerComboBox(PROJ_INF_2_v2DialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(530, 60, 241, 61))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.wybor_warstwa = QtWidgets.QLabel(PROJ_INF_2_v2DialogBase)
        self.wybor_warstwa.setGeometry(QtCore.QRect(110, 40, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wybor_warstwa.setFont(font)
        self.wybor_warstwa.setObjectName("wybor_warstwa")
        self.pole_powierzchni = QtWidgets.QLabel(PROJ_INF_2_v2DialogBase)
        self.pole_powierzchni.setGeometry(QtCore.QRect(140, 450, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pole_powierzchni.setFont(font)
        self.pole_powierzchni.setObjectName("pole_powierzchni")
        self.pushButton_dh = QtWidgets.QPushButton(PROJ_INF_2_v2DialogBase)
        self.pushButton_dh.setGeometry(QtCore.QRect(580, 260, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_dh.setFont(font)
        self.pushButton_dh.setObjectName("pushButton_dh")
        self.line = QtWidgets.QFrame(PROJ_INF_2_v2DialogBase)
        self.line.setGeometry(QtCore.QRect(40, 150, 841, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.przewyzszenie = QtWidgets.QLabel(PROJ_INF_2_v2DialogBase)
        self.przewyzszenie.setGeometry(QtCore.QRect(140, 260, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.przewyzszenie.setFont(font)
        self.przewyzszenie.setObjectName("przewyzszenie")
        self.line_2 = QtWidgets.QFrame(PROJ_INF_2_v2DialogBase)
        self.line_2.setGeometry(QtCore.QRect(40, 380, 841, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_2 = QtWidgets.QPushButton(PROJ_INF_2_v2DialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_3 = QtWidgets.QFrame(PROJ_INF_2_v2DialogBase)
        self.line_3.setGeometry(QtCore.QRect(40, 620, 841, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(PROJ_INF_2_v2DialogBase)
        self.button_box.accepted.connect(PROJ_INF_2_v2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(PROJ_INF_2_v2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PROJ_INF_2_v2DialogBase)

    def retranslateUi(self, PROJ_INF_2_v2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        PROJ_INF_2_v2DialogBase.setWindowTitle(_translate("PROJ_INF_2_v2DialogBase", "PROJ_INF_2_v2"))
        self.wybor_warstwa.setText(_translate("PROJ_INF_2_v2DialogBase", "Wybierz warstwę : "))
        self.pole_powierzchni.setText(_translate("PROJ_INF_2_v2DialogBase", "Pole powierzchni : "))
        self.pushButton_dh.setText(_translate("PROJ_INF_2_v2DialogBase", "Oblicz"))
        self.przewyzszenie.setText(_translate("PROJ_INF_2_v2DialogBase", "Przewyższenie :"))
        self.pushButton_2.setText(_translate("PROJ_INF_2_v2DialogBase", "Oblicz"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PROJ_INF_2_v2DialogBase = QtWidgets.QDialog()
    ui = Ui_PROJ_INF_2_v2DialogBase()
    ui.setupUi(PROJ_INF_2_v2DialogBase)
    PROJ_INF_2_v2DialogBase.show()
    sys.exit(app.exec_())
