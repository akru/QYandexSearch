#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, uic
 
class YSearch(QtGui.QMainWindow):
    def __init__(s):
        QtGui.QMainWindow.__init__(s)

        # Load UI Qt file
        s.ui = uic.loadUi('ya.ui')
        s.ui.show()

        # Conections
        s.connect(s.ui.toolButton, QtCore.SIGNAL('clicked()'), s.open_input_file)
        s.connect(s.ui.toolButton_2, QtCore.SIGNAL('clicked()'), s.open_output_file)

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

    def main(s):
        s.yakey = s.ui.lineEdit.text
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = YSearch()
    sys.exit(app.exec_())
