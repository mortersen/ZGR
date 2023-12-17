# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ReadPDF.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widgetReadPDF(object):
    def setupUi(self, widgetReadPDF):
        widgetReadPDF.setObjectName("widgetReadPDF")
        widgetReadPDF.resize(747, 466)
        widgetReadPDF.setMinimumSize(QtCore.QSize(600, 400))
        widgetReadPDF.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(widgetReadPDF)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget = QtWidgets.QWidget(widgetReadPDF)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_7.addWidget(self.widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_Download = QtWidgets.QToolButton(widgetReadPDF)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Download.setIcon(icon)
        self.btn_Download.setObjectName("btn_Download")
        self.horizontalLayout_6.addWidget(self.btn_Download)
        self.btn_Print = QtWidgets.QToolButton(widgetReadPDF)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Print.setIcon(icon1)
        self.btn_Print.setObjectName("btn_Print")
        self.horizontalLayout_6.addWidget(self.btn_Print)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_PageUp = QtWidgets.QToolButton(widgetReadPDF)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/PageUp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_PageUp.setIcon(icon2)
        self.btn_PageUp.setObjectName("btn_PageUp")
        self.horizontalLayout_5.addWidget(self.btn_PageUp)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_CurrentPage = QtWidgets.QLineEdit(widgetReadPDF)
        self.lineEdit_CurrentPage.setMaximumSize(QtCore.QSize(42, 16777215))
        self.lineEdit_CurrentPage.setObjectName("lineEdit_CurrentPage")
        self.horizontalLayout_4.addWidget(self.lineEdit_CurrentPage)
        self.label_pages = QtWidgets.QLabel(widgetReadPDF)
        self.label_pages.setMaximumSize(QtCore.QSize(42, 16777215))
        self.label_pages.setObjectName("label_pages")
        self.horizontalLayout_4.addWidget(self.label_pages)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.btn_PageDown = QtWidgets.QToolButton(widgetReadPDF)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/PageDown.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_PageDown.setIcon(icon3)
        self.btn_PageDown.setObjectName("btn_PageDown")
        self.horizontalLayout_5.addWidget(self.btn_PageDown)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_ZoomSamller = QtWidgets.QToolButton(widgetReadPDF)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/ZoomSmaller.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_ZoomSamller.setIcon(icon4)
        self.btn_ZoomSamller.setObjectName("btn_ZoomSamller")
        self.horizontalLayout_3.addWidget(self.btn_ZoomSamller)
        self.comboBox_factor = QtWidgets.QComboBox(widgetReadPDF)
        self.comboBox_factor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_factor.setObjectName("comboBox_factor")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.comboBox_factor.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_factor)
        self.btn_ZoomLarger = QtWidgets.QToolButton(widgetReadPDF)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/ZoomLarger.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_ZoomLarger.setIcon(icon5)
        self.btn_ZoomLarger.setObjectName("btn_ZoomLarger")
        self.horizontalLayout_3.addWidget(self.btn_ZoomLarger)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.showArea = QtWidgets.QScrollArea(widgetReadPDF)
        self.showArea.setWidgetResizable(True)
        self.showArea.setObjectName("showArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 382))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.showArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.showArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_FileStatus = QtWidgets.QLabel(widgetReadPDF)
        self.label_FileStatus.setObjectName("label_FileStatus")
        self.horizontalLayout_2.addWidget(self.label_FileStatus)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(widgetReadPDF)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 10)

        self.retranslateUi(widgetReadPDF)
        self.comboBox_factor.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(widgetReadPDF)

    def retranslateUi(self, widgetReadPDF):
        _translate = QtCore.QCoreApplication.translate
        widgetReadPDF.setWindowTitle(_translate("widgetReadPDF", "Form"))
        self.btn_Download.setText(_translate("widgetReadPDF", "..."))
        self.btn_Print.setText(_translate("widgetReadPDF", "..."))
        self.btn_PageUp.setText(_translate("widgetReadPDF", "..."))
        self.label_pages.setText(_translate("widgetReadPDF", "/1000页"))
        self.btn_PageDown.setText(_translate("widgetReadPDF", "..."))
        self.btn_ZoomSamller.setText(_translate("widgetReadPDF", "..."))
        self.comboBox_factor.setItemText(0, _translate("widgetReadPDF", "200%"))
        self.comboBox_factor.setItemText(1, _translate("widgetReadPDF", "180%"))
        self.comboBox_factor.setItemText(2, _translate("widgetReadPDF", "160%"))
        self.comboBox_factor.setItemText(3, _translate("widgetReadPDF", "140%"))
        self.comboBox_factor.setItemText(4, _translate("widgetReadPDF", "120%"))
        self.comboBox_factor.setItemText(5, _translate("widgetReadPDF", "100%"))
        self.comboBox_factor.setItemText(6, _translate("widgetReadPDF", "80%"))
        self.comboBox_factor.setItemText(7, _translate("widgetReadPDF", "60%"))
        self.comboBox_factor.setItemText(8, _translate("widgetReadPDF", "40%"))
        self.comboBox_factor.setItemText(9, _translate("widgetReadPDF", "20%"))
        self.btn_ZoomLarger.setText(_translate("widgetReadPDF", "..."))
        self.label_FileStatus.setText(_translate("widgetReadPDF", "TextLabel"))
        self.label.setText(_translate("widgetReadPDF", "Ctrl+鼠标滚轮调整页面大小"))
import CakeDM_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widgetReadPDF = QtWidgets.QWidget()
    ui = Ui_widgetReadPDF()
    ui.setupUi(widgetReadPDF)
    widgetReadPDF.show()
    sys.exit(app.exec_())
