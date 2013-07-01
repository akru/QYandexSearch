#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, uic
from search import YaSearch

reload(sys)
sys.setdefaultencoding('utf8')
 
SEPARATOR = '\n\n'

class YSearch(QtGui.QMainWindow):
    def __init__(s):
        QtGui.QMainWindow.__init__(s)

        # Load UI Qt file
        s.ui = uic.loadUi('ya.ui')
        s.ui.show()

        # Conections
        s.connect(s.ui.toolButton, QtCore.SIGNAL('clicked()'), s.open_input_file)
        s.connect(s.ui.toolButton_2, QtCore.SIGNAL('clicked()'), s.open_output_file)
        s.connect(s.ui.tryButton, QtCore.SIGNAL('clicked()'), s.read_input_file)

    def open_input_file(s):
        s.input_fname = QtGui.QFileDialog.getOpenFileName(s, "", "", "Text file (*.txt)")
        s.ui.lineEdit_3.setText(s.input_fname)
        s.ui.listWidget.addItem(u'Выбран исходный файл: %s' % s.input_fname)

    def open_output_file(s):
        fname = QtGui.QFileDialog.getSaveFileName(s, "", "", "Text file (*.txt)")
        if len(fname) > 0:
            s.ui.lineEdit_4.setText(fname)
            s.ui.listWidget.addItem(u'Выбран выходной файл: %s' % fname)
            s.output_fname = fname

    def read_input_file(s):
        input_file = open(s.input_fname, 'r')                                 
        output_file = open(s.output_fname, 'w')                                 
        API_USER, API_KEY = s.ui.lineEdit.text().split("@")
        y = YaSearch(API_USER, API_KEY)
        for line in input_file:
            line = line.split("\n")[0]
            if line.strip() is not "":
                s.ui.listWidget.addItem(u'Поиск: %s' % line)
                for i in range(1,10):
                    results = y.search('"%s"' % line, page=i)
                    if results.error is None:
                        for result in results.items:
                            line += '\n' + result.url.encode('utf-8') + '\n' + result.snippet.encode('utf-8')
                    else:
                        line += '\n' + results.error.description

                output_file.write(line+SEPARATOR)
        s.ui.listWidget.addItem(u'Поиск завершен.')


 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = YSearch()
    sys.exit(app.exec_())
