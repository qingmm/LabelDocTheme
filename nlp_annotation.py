# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nlp_annotation.ui'
#
# @version: 3.0
# @by mamq
# @date: 2018-11-12

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow, QGridLayout
from PyQt5.QtGui import QFont
import sys, os, codecs, json
from translate import baidu_translate

path = sys.path[0] + os.sep

class Ui_Dialog(QMainWindow):
    ''''''
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(944, 726)

        self.label_1 = QtWidgets.QLabel(Dialog) # date
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog) # location
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog) # url
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)  # content
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)  # translation
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)  # label
        self.label_6.setObjectName("label_6")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)  # date
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)  # location
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)  # url
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Dialog)  # content
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(Dialog)  # translation
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)  # label
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.plainTextEdit_4.setFont(QFont("SansSerif", 14))
        self.plainTextEdit_5.setFont(QFont("SansSerif", 14))

        # button: open file
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setObjectName("pushButton_1")
        # button: next line
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        # button: connect to mongodb
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.choice_list = ['politics', 'political conflict', 'political diplomacy', 'military diplomacy', 'military conflict', 'war',
                            'terrorism', 'oil trade', 'financial trade', 'securities trade', 'culture', 'laws', 'natural disaster', 'energy crisis',
                            'financial crisis', 'education', 'crime', 'energy', 'health', 'science and technology']
        self.comboBox.addItems(self.choice_list)
        self.comboBox.currentIndexChanged.connect(lambda: self.on_combobox_func(self.comboBox.currentText()))

        grid = QGridLayout()
        grid.setSpacing(9)
        # first row: date, location, Open
        grid.addWidget(self.label_1, 1, 0)  # date
        grid.addWidget(self.lineEdit_1, 1, 1)
        grid.addWidget(self.label_2, 1, 2)  # location
        grid.addWidget(self.lineEdit_2, 1, 3, 1, 5)
        grid.addWidget(self.pushButton_1, 1, 8)  # Open
        # second row: url, Next
        grid.addWidget(self.label_3, 2, 0)  # url
        grid.addWidget(self.lineEdit_3, 2, 1, 1, 7)
        grid.addWidget(self.pushButton_2, 2, 8)  # Next
        # third row: content
        grid.addWidget(self.label_4, 3, 0)
        grid.addWidget(self.plainTextEdit_4, 3, 1, 5, 9)
        # fourth row: translation
        grid.addWidget(self.label_5, 8, 0)
        grid.addWidget(self.plainTextEdit_5, 8, 1, 5, 9)
        # fifth row: label
        grid.addWidget(self.label_6, 13, 0)
        grid.addWidget(self.lineEdit_6, 13, 1, 1, 8)
        grid.addWidget(self.comboBox, 13, 9)  # label-list
        # sixth row: MongoDB, cancel, ok
        grid.addWidget(self.pushButton_3, 14, 1, 1, 1)
        grid.addWidget(self.buttonBox, 14, 3)

        self.pushButton_1.clicked.connect(self.read_json)
        self.pushButton_2.clicked.connect(self.next_line)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.closeUI)
        self.buttonBox.rejected.connect(self.closeUI)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setLayout(grid)
        Dialog.show()

    def retranslateUi(self, Dialog):
        '''重命名控件'''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自然语言标注工具"))
        self.label_1.setText(_translate("Dialog", "date:"))
        self.label_2.setText(_translate("Dialog", "location"))
        self.label_3.setText(_translate("Dialog", "url"))
        self.label_4.setText(_translate("Dialog", "content"))
        self.label_5.setText(_translate("Dialog", "translation"))
        self.label_6.setText(_translate("Dialog", "label"))
        self.pushButton_1.setText(_translate("Dialog", "Open"))
        self.pushButton_2.setText(_translate("Dialog", "Next"))
        self.pushButton_3.setText(_translate("Dialog", "MongoDB"))

    def on_combobox_func(self, label):
        '''在下拉框中选择值后，将其更新到label框中进行显示'''
        label_text = self.lineEdit_6.text()
        if label_text:
            label_text += ';' + label
        else:
            label_text += label
        self.lineEdit_6.setText(label_text)

    def next_line(self):
        '''点击Nextbutton后，更新label_list与下拉框,并保存标注数据'''
        skip = 4
        for i in range(skip):
            try:
                line = self.f.readline()
            except:
                line = self.f.readline()
        dic = json.loads(line)
        label_text = self.lineEdit_6.text()
        if label_text:
            label_list = label_text.split(';')
            for label in label_list:
                if label not in self.choice_list:
                    self.choice_list.append(label)
                    self.comboBox.addItem(label)
            dic['label'] = label_list
            json.dump(dic, self.outf, ensure_ascii=False)
            self.outf.write('\n')
        self.show_data(dic)

    def closeUI(self):
        dic = {'labels': self.choice_list}
        json.dump(dic, self.labelf, ensure_ascii=False)
        self.labelf.close()
        self.outf.close()
        QCoreApplication.instance().quit()

    def show_data(self, dic):
        '''将数据显示在界面中'''
        date = dic['date']
        location = dic['locinfo']
        url = dic['url']
        content = dic['content']
        self.lineEdit_1.setText(date)
        self.lineEdit_2.setText(str(location))
        self.lineEdit_3.setText(url)
        self.plainTextEdit_4.clear()
        self.plainTextEdit_4.appendPlainText(content)
        translation = baidu_translate(content)
        self.plainTextEdit_5.clear()
        self.plainTextEdit_5.appendPlainText(translation)
        self.lineEdit_6.clear()

    def read_json(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print (fname)
        if fname[0]:
            self.f = codecs.open(fname[0], 'r', 'utf-8')
            line = self.f.readline()
            dic = json.loads(line)
            self.show_data(dic)
            fn = fname[0].split(os.sep)[-1].split('.')[0] + '_labeled.json'
            temp = fname[0].split(os.sep)[:-1]
            folder = os.sep + os.path.join(*temp) + os.sep
            out_fp = folder + fn  # 保存标注数据
            label_fp = folder + 'label_list.json'
            self.outf = codecs.open(out_fp, 'a', 'utf-8')
            self.labelf = codecs.open(label_fp, 'a', 'utf-8')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QDialog()
    w = Ui_Dialog()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())