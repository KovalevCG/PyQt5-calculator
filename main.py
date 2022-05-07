# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_V2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        # first number for calculation
        self.first_number = "0"
        # second number for calculation
        self.second_number = "0"
        # current operator
        self.op = "none"
        # self.answer = True when "equal" pressed
        self.answer = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 480)
        MainWindow.setMinimumSize(QtCore.QSize(300, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/calculate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #202430;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size:16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: #242a38;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #2a3141;    \n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #4d5f7c;\n"
                                 "}")
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color:#8d939f;")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("font-size:40pt;\n"
                                    "border:none;")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.layout_btns = QtWidgets.QGridLayout()
        self.layout_btns.setObjectName("layout_btns")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("7"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName("btn_7")
        self.layout_btns.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("9"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setShortcut("")
        self.btn_9.setObjectName("btn_9")
        self.layout_btns.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("8"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setObjectName("btn_8")
        self.layout_btns.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("6"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setObjectName("btn_6")
        self.layout_btns.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("0"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("")
        self.btn_0.setObjectName("btn_0")
        self.layout_btns.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("2"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setObjectName("btn_2")
        self.layout_btns.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("3"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setObjectName("btn_3")
        self.layout_btns.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setObjectName("btn_dot")
        self.layout_btns.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("5"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setObjectName("btn_5")
        self.layout_btns.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("1"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.layout_btns.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.backspace_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setStyleSheet("QPushButton {\n"
                                         "    background-color: #4e596f;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         " QPushButton:hover {\n"
                                         "    background-color: #5a6780;\n"
                                         " }\n"
                                         " QPushButton:pressed {\n"
                                         "    background-color: #707f9e;\n"
                                         " }")
        self.btn_backspace.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/backspace.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QtCore.QSize(32, 32))
        self.btn_backspace.setObjectName("btn_backspace")
        self.layout_btns.addWidget(self.btn_backspace, 0, 0, 1, 1)
        self.btn_plus_minus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus_minus.sizePolicy().hasHeightForWidth())
        self.btn_plus_minus.setSizePolicy(sizePolicy)
        self.btn_plus_minus.setStyleSheet("QPushButton {\n"
                                          "    background-color: #4e596f;\n"
                                          "    border: none;\n"
                                          "}\n"
                                          " QPushButton:hover {\n"
                                          "    background-color: #5a6780;\n"
                                          " }\n"
                                          " QPushButton:pressed {\n"
                                          "    background-color: #707f9e;\n"
                                          " }")
        self.btn_plus_minus.setObjectName("btn_plus_minus")
        self.layout_btns.addWidget(self.btn_plus_minus, 0, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.number_it("4"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setObjectName("btn_4")
        self.layout_btns.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_C = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy)
        self.btn_C.setStyleSheet("QPushButton {\n"
                                 "    background-color: #4e596f;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 " QPushButton:hover {\n"
                                 "    background-color: #5a6780;\n"
                                 " }\n"
                                 " QPushButton:pressed {\n"
                                 "    background-color: #707f9e;\n"
                                 " }")
        self.btn_C.setIconSize(QtCore.QSize(32, 32))
        self.btn_C.setObjectName("btn_C")
        self.layout_btns.addWidget(self.btn_C, 0, 1, 1, 1)
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_op_it("*"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setStyleSheet("QPushButton {\n"
                                        "    background-color: #f55d4d;\n"
                                        "    border: none;\n"
                                        "}\n"
                                        " QPushButton:hover {\n"
                                        "    background-color: #f77365;\n"
                                        " }\n"
                                        " QPushButton:pressed {\n"
                                        "    background-color: #ffa298;\n"
                                        " }")
        self.btn_multiply.setObjectName("btn_multiply")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_multiply)
        self.layout_btns.addWidget(self.btn_multiply, 1, 3, 1, 1)
        self.btn_equals = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.equals_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy)
        self.btn_equals.setStyleSheet("QPushButton {\n"
                                      "    background-color: #f55d4d;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      " QPushButton:hover {\n"
                                      "    background-color: #f77365;\n"
                                      " }\n"
                                      " QPushButton:pressed {\n"
                                      "    background-color: #ffa298;\n"
                                      " }")
        self.btn_equals.setObjectName("btn_equals")
        self.layout_btns.addWidget(self.btn_equals, 4, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_op_it("+"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setStyleSheet("QPushButton {\n"
                                    "    background-color: #f55d4d;\n"
                                    "    border: none;\n"
                                    "}\n"
                                    " QPushButton:hover {\n"
                                    "    background-color: #f77365;\n"
                                    " }\n"
                                    " QPushButton:pressed {\n"
                                    "    background-color: #ffa298;\n"
                                    " }")
        self.btn_plus.setObjectName("btn_plus")
        self.buttonGroup.addButton(self.btn_plus)
        self.layout_btns.addWidget(self.btn_plus, 3, 3, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_op_it("-"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setStyleSheet("QPushButton {\n"
                                     "    background-color: #f55d4d;\n"
                                     "    border: none;\n"
                                     "}\n"
                                     " QPushButton:hover {\n"
                                     "    background-color: #f77365;\n"
                                     " }\n"
                                     " QPushButton:pressed {\n"
                                     "    background-color: #ffa298;\n"
                                     " }")
        self.btn_minus.setObjectName("btn_minus")
        self.buttonGroup.addButton(self.btn_minus)
        self.layout_btns.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_op_it("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        self.btn_divide.setStyleSheet("QPushButton {\n"
                                      "    background-color: #f55d4d;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      " QPushButton:hover {\n"
                                      "    background-color: #f77365;\n"
                                      " }\n"
                                      " QPushButton:pressed {\n"
                                      "    background-color: #ffa298;\n"
                                      " }")
        self.btn_divide.setObjectName("btn_divide")
        self.buttonGroup.addButton(self.btn_divide)
        self.layout_btns.addWidget(self.btn_divide, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.layout_btns)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # when dot pressed
    def dot_it(self):
        screen = self.lineEdit.text()
        if "." in screen:
            pass
        else:
            screen = self.lineEdit.text() + "."
            self.lineEdit.setText(screen)

    # when any number pressed
    def number_it(self, pressed):
        if self.answer:
            calc_text = pressed
            self.answer = False
        elif self.lineEdit.text() == "0":
            calc_text = pressed
        else:
            calc_text = self.lineEdit.text() + pressed
        self.lineEdit.setText(calc_text)

    # when "C" pressed
    def clear_it(self):
        self.lineEdit.setText("0")
        self.label.setText("")
        self.first_number = "0"
        self.second_number = "0"
        self.op = "none"
        self.answer = False

    # when backspace pressed
    def backspace_it(self):
        screen = self.lineEdit.text()
        if len(screen) >= 3:
            screen = screen[:-1]
        elif len(screen) == 2:
            if screen[0] == '-':
                screen = '0'
            else:
                screen = screen[:-1]
        elif len(screen) == 1:
            screen = '0'
        self.lineEdit.setText(screen)

    # when +/- pressed
    def plus_minus_it(self):
        screen = self.lineEdit.text()
        if screen == '0':
            return
        if screen[0] == "-":
            screen = screen[1:]
        else:
            screen = "-" + screen
        self.lineEdit.setText(screen)

    # when math operator pressed
    def math_op_it(self, op):
        if self.label.text() != "":
            self.equals_it()
            self.first_number = self.lineEdit.text()
            self.op = op
            self.label.setText(self.first_number + " " + self.op)
            self.lineEdit.setText("0")
            return

        self.first_number = self.lineEdit.text()
        self.op = op
        self.label.setText(self.first_number + " " + self.op)
        self.lineEdit.setText("0")

    # when equal pressed
    def equals_it(self):
        # if "equal" wasn't previous button
        if not self.answer:
            self.second_number = self.lineEdit.text()
            if self.op == '/':
                result = float(self.first_number) / float(self.second_number)
            if self.op == '*':
                result = float(self.first_number) * float(self.second_number)
            if self.op == '+':
                result = float(self.first_number) + float(self.second_number)
            if self.op == '-':
                result = float(self.first_number) - float(self.second_number)
            if self.op == 'none':
                return
        # if previous button was "equal"
        else:
            self.first_number = self.lineEdit.text()
            print("first_number: ", self.first_number)
            if self.op == '/':
                result = float(self.first_number) / float(self.second_number)
            if self.op == '*':
                result = float(self.first_number) * float(self.second_number)
            if self.op == '+':
                result = float(self.first_number) + float(self.second_number)
            if self.op == '-':
                result = float(self.first_number) - float(self.second_number)
                print('result:', result)
            if self.op == 'none':
                return

        # remove unnecessary zeros at the end
        if result % 1 == 0:
            self.lineEdit.setText(str(int(result)))
            self.label.setText("")
        else:
            self.lineEdit.setText(str(result))
            self.label.setText("")

        self.answer = True


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_dot.setShortcut(_translate("MainWindow", "."))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_plus_minus.setText(_translate("MainWindow", "+/-"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_C.setText(_translate("MainWindow", "C"))
        self.btn_C.setShortcut(_translate("MainWindow", "C"))
        self.btn_multiply.setText(_translate("MainWindow", "×"))
        self.btn_multiply.setShortcut(_translate("MainWindow", "*"))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_equals.setShortcut(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))
        self.btn_divide.setText(_translate("MainWindow", "÷"))
        self.btn_divide.setShortcut(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    import resource

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
