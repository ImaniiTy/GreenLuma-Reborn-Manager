# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 728)
        MainWindow.setStyleSheet("background-color: rgb(18, 18, 18);")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(179, 179, 179);\n"
"    border: 1px solid rgb(130, 135, 144);\n"
"    background-color: rgb(28, 28, 28); \n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    color: rgb(179, 179, 179);\n"
"    border-color: transparent\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:images/down-arrow.png);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    padding-right: 18px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"     margin: 2px 1px 2px 1px;\n"
"    color: rgb(255, 255, 255);\n"
"     background-color: rgb(28, 28, 28);\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"     border: 1px solid rgb(28, 28, 28);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:rgba(232, 232, 232);\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(179, 179, 179);\n"
"    font: 75 11pt \"Consolas\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(24, 24, 24);\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    border: 2px solid rgb(85, 85, 85);\n"
"}\n"
"\n"
"#generate_btn {\n"
"    background-color: rgb(29, 185, 84);\n"
"    color: rgb(6, 11, 8);\n"
"}\n"
"\n"
"#generate_btn:hover {\n"
"    color: rgb(24, 24, 24);\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(29, 29, 29);\n"
"    border: 1px solid rgb(245, 245, 245)\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    padding: 2px\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(420, 660, 221, 51))
        self.generate_btn.setStyleSheet("")
        self.generate_btn.setObjectName("generate_btn")
        self.game_search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.game_search_text.setGeometry(QtCore.QRect(10, 50, 781, 31))
        self.game_search_text.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.game_search_text.setText("")
        self.game_search_text.setObjectName("game_search_text")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(730, 52, 51, 26))
        self.search_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"border: 0px")
        self.search_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/search-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon)
        self.search_btn.setIconSize(QtCore.QSize(25, 25))
        self.search_btn.setObjectName("search_btn")
        self.games_list = QtWidgets.QListWidget(self.centralwidget)
        self.games_list.setGeometry(QtCore.QRect(820, 160, 281, 441))
        self.games_list.setStyleSheet("background-color: rgb(28, 28, 28);")
        self.games_list.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.games_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.games_list.setObjectName("games_list")
        self.profile_selector = QtWidgets.QComboBox(self.centralwidget)
        self.profile_selector.setGeometry(QtCore.QRect(820, 50, 281, 31))
        self.profile_selector.setFocusPolicy(QtCore.Qt.NoFocus)
        self.profile_selector.setAcceptDrops(False)
        self.profile_selector.setStyleSheet("QWidget:item{\n"
"     background: rgb(255, 0, 0)\n"
"}\n"
"QWidget:item:checked {\n"
"     font-weight: bold;\n"
"}")
        self.profile_selector.setIconSize(QtCore.QSize(18, 18))
        self.profile_selector.setFrame(False)
        self.profile_selector.setObjectName("profile_selector")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 20, 121, 21))
        self.label.setStyleSheet("background: transparent;\n"
"font: 75 11pt \"Consolas\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 130, 121, 21))
        self.label_2.setStyleSheet("background: transparent;\n"
"font: 75 11pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.create_profile = QtWidgets.QPushButton(self.centralwidget)
        self.create_profile.setGeometry(QtCore.QRect(820, 90, 121, 31))
        self.create_profile.setStyleSheet("")
        self.create_profile.setObjectName("create_profile")
        self.add_to_profile = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_profile.setGeometry(QtCore.QRect(10, 610, 141, 31))
        self.add_to_profile.setStyleSheet("")
        self.add_to_profile.setObjectName("add_to_profile")
        self.profile_create_window = QtWidgets.QWidget(self.centralwidget)
        self.profile_create_window.setEnabled(False)
        self.profile_create_window.setGeometry(QtCore.QRect(290, 270, 471, 161))
        self.profile_create_window.setStyleSheet("border: 1px solid white")
        self.profile_create_window.setObjectName("profile_create_window")
        self.profile_name = QtWidgets.QLineEdit(self.profile_create_window)
        self.profile_name.setGeometry(QtCore.QRect(30, 50, 411, 31))
        self.profile_name.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.profile_name.setObjectName("profile_name")
        self.create_profile_btn = QtWidgets.QPushButton(self.profile_create_window)
        self.create_profile_btn.setGeometry(QtCore.QRect(30, 110, 151, 31))
        self.create_profile_btn.setObjectName("create_profile_btn")
        self.cancel_profile_btn = QtWidgets.QPushButton(self.profile_create_window)
        self.cancel_profile_btn.setGeometry(QtCore.QRect(290, 110, 151, 31))
        self.cancel_profile_btn.setObjectName("cancel_profile_btn")
        self.label_3 = QtWidgets.QLabel(self.profile_create_window)
        self.label_3.setGeometry(QtCore.QRect(32, 19, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0px")
        self.label_3.setObjectName("label_3")
        self.search_result = QtWidgets.QTableWidget(self.centralwidget)
        self.search_result.setGeometry(QtCore.QRect(10, 110, 791, 491))
        self.search_result.setStyleSheet("background-color: rgb(28, 28, 28);")
        self.search_result.setDragEnabled(True)
        self.search_result.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.search_result.setWordWrap(False)
        self.search_result.setObjectName("search_result")
        self.search_result.setColumnCount(0)
        self.search_result.setRowCount(0)
        self.search_result.horizontalHeader().setStretchLastSection(True)
        self.search_result.verticalHeader().setVisible(False)
        self.search_result.verticalHeader().setStretchLastSection(False)
        self.delete_profile = QtWidgets.QPushButton(self.centralwidget)
        self.delete_profile.setGeometry(QtCore.QRect(960, 90, 141, 31))
        self.delete_profile.setStyleSheet("")
        self.delete_profile.setObjectName("delete_profile")
        self.remove_game = QtWidgets.QPushButton(self.centralwidget)
        self.remove_game.setGeometry(QtCore.QRect(820, 610, 121, 31))
        self.remove_game.setStyleSheet("")
        self.remove_game.setObjectName("remove_game")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 5, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.searching_frame = QtWidgets.QFrame(self.centralwidget)
        self.searching_frame.setEnabled(False)
        self.searching_frame.setGeometry(QtCore.QRect(220, 300, 331, 111))
        self.searching_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searching_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searching_frame.setObjectName("searching_frame")
        self.label_5 = QtWidgets.QLabel(self.searching_frame)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.set_steam_path_window = QtWidgets.QWidget(self.centralwidget)
        self.set_steam_path_window.setEnabled(False)
        self.set_steam_path_window.setGeometry(QtCore.QRect(290, 270, 471, 161))
        self.set_steam_path_window.setStyleSheet("border: 1px solid white")
        self.set_steam_path_window.setObjectName("set_steam_path_window")
        self.steam_path = QtWidgets.QLineEdit(self.set_steam_path_window)
        self.steam_path.setGeometry(QtCore.QRect(30, 50, 411, 31))
        self.steam_path.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.steam_path.setObjectName("steam_path")
        self.save_steam_path = QtWidgets.QPushButton(self.set_steam_path_window)
        self.save_steam_path.setGeometry(QtCore.QRect(50, 110, 151, 31))
        self.save_steam_path.setObjectName("save_steam_path")
        self.label_6 = QtWidgets.QLabel(self.set_steam_path_window)
        self.label_6.setGeometry(QtCore.QRect(32, 19, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 0px")
        self.label_6.setObjectName("label_6")
        self.cancel_steam_path_btn = QtWidgets.QPushButton(self.set_steam_path_window)
        self.cancel_steam_path_btn.setGeometry(QtCore.QRect(270, 110, 151, 31))
        self.cancel_steam_path_btn.setObjectName("cancel_steam_path_btn")
        self.change_steam_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_steam_path_btn.setGeometry(QtCore.QRect(170, 610, 201, 31))
        self.change_steam_path_btn.setStyleSheet("")
        self.change_steam_path_btn.setObjectName("change_steam_path_btn")
        self.search_result.raise_()
        self.generate_btn.raise_()
        self.game_search_text.raise_()
        self.search_btn.raise_()
        self.games_list.raise_()
        self.profile_selector.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.create_profile.raise_()
        self.add_to_profile.raise_()
        self.delete_profile.raise_()
        self.remove_game.raise_()
        self.label_4.raise_()
        self.searching_frame.raise_()
        self.profile_create_window.raise_()
        self.set_steam_path_window.raise_()
        self.change_steam_path_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GreenLuma Reborn Manager"))
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.game_search_text.setPlaceholderText(_translate("MainWindow", "Search Game"))
        self.label.setText(_translate("MainWindow", "Profile"))
        self.label_2.setText(_translate("MainWindow", "Games List"))
        self.create_profile.setText(_translate("MainWindow", "New Profile"))
        self.add_to_profile.setText(_translate("MainWindow", "Add Games"))
        self.profile_name.setPlaceholderText(_translate("MainWindow", "Profile Name"))
        self.create_profile_btn.setText(_translate("MainWindow", "Create"))
        self.cancel_profile_btn.setText(_translate("MainWindow", "Cancel"))
        self.label_3.setText(_translate("MainWindow", "Profile Name:"))
        self.delete_profile.setText(_translate("MainWindow", "Delete Profile"))
        self.remove_game.setText(_translate("MainWindow", "Remove Games"))
        self.label_4.setText(_translate("MainWindow", "GreenLuma Reborn Manager"))
        self.label_5.setText(_translate("MainWindow", "Searching..."))
        self.steam_path.setPlaceholderText(_translate("MainWindow", "Path"))
        self.save_steam_path.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Steam Path"))
        self.cancel_steam_path_btn.setText(_translate("MainWindow", "Cancel"))
        self.change_steam_path_btn.setText(_translate("MainWindow", "Change Steam Path"))


from Qt import resources_rc
