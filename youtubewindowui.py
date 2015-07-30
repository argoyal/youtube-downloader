# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubewindow.ui'
#
# Created: Wed Feb 11 16:33:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import sys

from script import YoutubeDownloader

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_YoutubeWindow(object):
    def setupUi(self, YoutubeWindow):
        YoutubeWindow.setObjectName(_fromUtf8("YoutubeWindow"))
        YoutubeWindow.resize(800, 600)
        YoutubeWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(YoutubeWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 611, 28))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 761, 501))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(253)
        self.tableWidget.setHorizontalHeaderLabels(['Format ID','Resolution','Extension'])
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 10, 141, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        YoutubeWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(YoutubeWindow)
        QtCore.QMetaObject.connectSlotsByName(YoutubeWindow)

    def retranslateUi(self, YoutubeWindow):
        YoutubeWindow.setWindowTitle(_translate("YoutubeWindow", "Youtube Downloader", None))
        self.lineEdit.setPlaceholderText(_translate("YoutubeWindow", "Enter Youtube Link", None))
        self.pushButton.setText(_translate("YoutubeWindow", "Download", None))

        self.pushButton.clicked.connect(self.get_youtube_link)
        self.tableWidget.cellClicked.connect(self.get_format_id)


    def get_youtube_link(self):
        youtube_link = self.lineEdit.text()
        self.get_processed_details(youtube_link)


    def get_processed_details(self, youtube_link):
        self.downloader_object = YoutubeDownloader(youtube_link)
        video_name, formats = self.downloader_object.get_youtube_link_and_process()
        self.displayTable(formats)
        

    def displayTable(self, formats):
        self.tableWidget.setRowCount(len(formats))
        for i in range(len(formats)):
            format_id = QtGui.QTableWidgetItem(str(formats[i]['format_id']))
            resolution = QtGui.QTableWidgetItem(str(formats[i]['format']))
            extension = QtGui.QTableWidgetItem(str(formats[i]['ext']))
            self.tableWidget.setItem(i,0,format_id)
            self.tableWidget.setItem(i,1,resolution)
            self.tableWidget.setItem(i,2,extension)


    def get_format_id(self, row, column):
        item_format_id = self.tableWidget.item(row, 0).text()
        item_resolution = self.tableWidget.item(row,1).text()
        item_extension = self.tableWidget.item(row,2).text()
        self.downloader_object.processing(item_format_id, item_resolution, item_extension)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('YoutubeDownloader')
    MainWindow = QtGui.QMainWindow()
    ui = Ui_YoutubeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    x = app.exec_()
    sys.exit(x)








