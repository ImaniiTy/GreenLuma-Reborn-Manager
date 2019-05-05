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
        MainWindow.resize(1120, 747)
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
"QPushButton:hover#settings_btn {\n"
"    background-color: transparent;\n"
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
"QHeaderView::section {\n"
"    background-color: rgb(29, 29, 29);\n"
"    border: 1px solid rgb(245, 245, 245)\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    padding: 2px\n"
"}\n"
"\n"
"QAbstractItemView::item:selected{ \n"
"    background-color: white;\n"
"    color: black\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
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
        self.create_profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_profile_btn.setObjectName("create_profile_btn")
        self.cancel_profile_btn = QtWidgets.QPushButton(self.profile_create_window)
        self.cancel_profile_btn.setGeometry(QtCore.QRect(290, 110, 151, 31))
        self.cancel_profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_profile_btn.setObjectName("cancel_profile_btn")
        self.label_3 = QtWidgets.QLabel(self.profile_create_window)
        self.label_3.setGeometry(QtCore.QRect(32, 19, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0px")
        self.label_3.setObjectName("label_3")
        self.set_steam_path_window = QtWidgets.QWidget(self.centralwidget)
        self.set_steam_path_window.setEnabled(False)
        self.set_steam_path_window.setGeometry(QtCore.QRect(290, 270, 471, 161))
        self.set_steam_path_window.setStyleSheet("border: 1px solid white")
        self.set_steam_path_window.setObjectName("set_steam_path_window")
        self.save_steam_path = QtWidgets.QPushButton(self.set_steam_path_window)
        self.save_steam_path.setGeometry(QtCore.QRect(50, 110, 151, 31))
        self.save_steam_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.cancel_steam_path_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_steam_path_btn.setObjectName("cancel_steam_path_btn")
        self.steam_path = QtWidgets.QLineEdit(self.set_steam_path_window)
        self.steam_path.setGeometry(QtCore.QRect(30, 47, 421, 31))
        self.steam_path.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.steam_path.setObjectName("steam_path")
        self.generic_popup = QtWidgets.QWidget(self.centralwidget)
        self.generic_popup.setEnabled(False)
        self.generic_popup.setGeometry(QtCore.QRect(290, 270, 531, 161))
        self.generic_popup.setStyleSheet("border: 1px solid white")
        self.generic_popup.setObjectName("generic_popup")
        self.popup_btn1 = QtWidgets.QPushButton(self.generic_popup)
        self.popup_btn1.setGeometry(QtCore.QRect(30, 110, 151, 31))
        self.popup_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.popup_btn1.setObjectName("popup_btn1")
        self.popup_btn2 = QtWidgets.QPushButton(self.generic_popup)
        self.popup_btn2.setGeometry(QtCore.QRect(350, 110, 151, 31))
        self.popup_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.popup_btn2.setObjectName("popup_btn2")
        self.popup_text = QtWidgets.QLabel(self.generic_popup)
        self.popup_text.setGeometry(QtCore.QRect(20, 20, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.popup_text.setFont(font)
        self.popup_text.setStyleSheet("border: 0px")
        self.popup_text.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_text.setWordWrap(True)
        self.popup_text.setObjectName("popup_text")
        self.closing_steam = QtWidgets.QWidget(self.centralwidget)
        self.closing_steam.setEnabled(False)
        self.closing_steam.setGeometry(QtCore.QRect(240, 240, 621, 181))
        self.closing_steam.setStyleSheet("border: 1px solid white")
        self.closing_steam.setObjectName("closing_steam")
        self.label_8 = QtWidgets.QLabel(self.closing_steam)
        self.label_8.setGeometry(QtCore.QRect(50, 30, 521, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 0px")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.main_panel = QtWidgets.QWidget(self.centralwidget)
        self.main_panel.setEnabled(True)
        self.main_panel.setGeometry(QtCore.QRect(0, 0, 1121, 751))
        self.main_panel.setObjectName("main_panel")
        self.profile_selector = QtWidgets.QComboBox(self.main_panel)
        self.profile_selector.setGeometry(QtCore.QRect(825, 45, 280, 31))
        self.profile_selector.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
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
        self.label = QtWidgets.QLabel(self.main_panel)
        self.label.setGeometry(QtCore.QRect(825, 15, 120, 21))
        self.label.setStyleSheet("background: transparent;\n"
"font: 75 11pt \"Consolas\";")
        self.label.setObjectName("label")
        self.remove_game = QtWidgets.QPushButton(self.main_panel)
        self.remove_game.setGeometry(QtCore.QRect(825, 605, 120, 31))
        self.remove_game.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_game.setStyleSheet("")
        self.remove_game.setFlat(False)
        self.remove_game.setObjectName("remove_game")
        self.compatibility_mode_checkbox = QtWidgets.QCheckBox(self.main_panel)
        self.compatibility_mode_checkbox.setEnabled(True)
        self.compatibility_mode_checkbox.setGeometry(QtCore.QRect(755, 695, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compatibility_mode_checkbox.setFont(font)
        self.compatibility_mode_checkbox.setChecked(False)
        self.compatibility_mode_checkbox.setObjectName("compatibility_mode_checkbox")
        self.search_result = QtWidgets.QTableView(self.main_panel)
        self.search_result.setGeometry(QtCore.QRect(15, 105, 790, 491))
        self.search_result.setStyleSheet("background-color: rgb(28, 28, 28);")
        self.search_result.setDragEnabled(True)
        self.search_result.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.search_result.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.search_result.setSortingEnabled(True)
        self.search_result.setWordWrap(False)
        self.search_result.setCornerButtonEnabled(False)
        self.search_result.setObjectName("search_result")
        self.search_result.horizontalHeader().setCascadingSectionResizes(False)
        self.search_result.horizontalHeader().setDefaultSectionSize(55)
        self.search_result.horizontalHeader().setMinimumSectionSize(55)
        self.search_result.horizontalHeader().setStretchLastSection(False)
        self.search_result.verticalHeader().setVisible(False)
        self.search_result.verticalHeader().setCascadingSectionResizes(True)
        self.search_result.verticalHeader().setDefaultSectionSize(35)
        self.search_result.verticalHeader().setMinimumSectionSize(35)
        self.searching_frame = QtWidgets.QFrame(self.main_panel)
        self.searching_frame.setEnabled(False)
        self.searching_frame.setGeometry(QtCore.QRect(235, 295, 330, 111))
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
        self.create_profile = QtWidgets.QPushButton(self.main_panel)
        self.create_profile.setGeometry(QtCore.QRect(825, 85, 120, 31))
        self.create_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_profile.setStyleSheet("")
        self.create_profile.setObjectName("create_profile")
        self.label_4 = QtWidgets.QLabel(self.main_panel)
        self.label_4.setGeometry(QtCore.QRect(225, 0, 360, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.run_GLR_btn = QtWidgets.QPushButton(self.main_panel)
        self.run_GLR_btn.setGeometry(QtCore.QRect(525, 665, 220, 51))
        self.run_GLR_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_GLR_btn.setStyleSheet("#run_GLR_btn {\n"
"    background-color: rgb(0, 116, 217);\n"
"    color: rgb(6, 11, 8);\n"
"}\n"
"\n"
"#run_GLR_btn:hover {\n"
"    color: rgb(24, 24, 24);\n"
"    background-color: rgb(245, 245, 245);\n"
"}")
        self.run_GLR_btn.setObjectName("run_GLR_btn")
        self.search_btn = QtWidgets.QPushButton(self.main_panel)
        self.search_btn.setGeometry(QtCore.QRect(745, 47, 50, 26))
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"border: 0px")
        self.search_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/search-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon)
        self.search_btn.setIconSize(QtCore.QSize(25, 25))
        self.search_btn.setObjectName("search_btn")
        self.add_to_profile = QtWidgets.QPushButton(self.main_panel)
        self.add_to_profile.setGeometry(QtCore.QRect(15, 605, 140, 31))
        self.add_to_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_to_profile.setStyleSheet("")
        self.add_to_profile.setObjectName("add_to_profile")
        self.games_list = QtWidgets.QListWidget(self.main_panel)
        self.games_list.setGeometry(QtCore.QRect(825, 155, 280, 441))
        self.games_list.setStyleSheet("background-color: rgb(28, 28, 28);")
        self.games_list.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.games_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.games_list.setObjectName("games_list")
        self.generate_btn = QtWidgets.QPushButton(self.main_panel)
        self.generate_btn.setGeometry(QtCore.QRect(285, 665, 220, 51))
        self.generate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_btn.setStyleSheet("#generate_btn {\n"
"    background-color: rgb(29, 185, 84);\n"
"    color: rgb(6, 11, 8);\n"
"}\n"
"\n"
"#generate_btn:hover {\n"
"    color: rgb(24, 24, 24);\n"
"    background-color: rgb(245, 245, 245);\n"
"}")
        self.generate_btn.setObjectName("generate_btn")
        self.label_2 = QtWidgets.QLabel(self.main_panel)
        self.label_2.setGeometry(QtCore.QRect(825, 125, 120, 21))
        self.label_2.setStyleSheet("background: transparent;\n"
"font: 75 11pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.delete_profile = QtWidgets.QPushButton(self.main_panel)
        self.delete_profile.setGeometry(QtCore.QRect(965, 85, 140, 31))
        self.delete_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_profile.setStyleSheet("")
        self.delete_profile.setObjectName("delete_profile")
        self.game_search_text = QtWidgets.QLineEdit(self.main_panel)
        self.game_search_text.setGeometry(QtCore.QRect(15, 45, 790, 31))
        self.game_search_text.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.game_search_text.setText("")
        self.game_search_text.setObjectName("game_search_text")
        self.no_hook_checkbox = QtWidgets.QCheckBox(self.main_panel)
        self.no_hook_checkbox.setGeometry(QtCore.QRect(755, 665, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.no_hook_checkbox.setFont(font)
        self.no_hook_checkbox.setChecked(True)
        self.no_hook_checkbox.setObjectName("no_hook_checkbox")
        self.version_label = QtWidgets.QLabel(self.main_panel)
        self.version_label.setGeometry(QtCore.QRect(1077, 728, 41, 16))
        self.version_label.setObjectName("version_label")
        self.settings_btn = QtWidgets.QPushButton(self.main_panel)
        self.settings_btn.setGeometry(QtCore.QRect(4, 700, 51, 41))
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setStyleSheet("border: solid 0px;")
        self.settings_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon1)
        self.settings_btn.setIconSize(QtCore.QSize(28, 28))
        self.settings_btn.setObjectName("settings_btn")
        self.profile_selector.raise_()
        self.label.raise_()
        self.remove_game.raise_()
        self.compatibility_mode_checkbox.raise_()
        self.search_result.raise_()
        self.create_profile.raise_()
        self.label_4.raise_()
        self.run_GLR_btn.raise_()
        self.add_to_profile.raise_()
        self.games_list.raise_()
        self.generate_btn.raise_()
        self.label_2.raise_()
        self.delete_profile.raise_()
        self.game_search_text.raise_()
        self.no_hook_checkbox.raise_()
        self.version_label.raise_()
        self.search_btn.raise_()
        self.settings_btn.raise_()
        self.searching_frame.raise_()
        self.settings_window = QtWidgets.QWidget(self.centralwidget)
        self.settings_window.setEnabled(False)
        self.settings_window.setGeometry(QtCore.QRect(220, 190, 660, 280))
        self.settings_window.setStyleSheet("border: 1px solid white")
        self.settings_window.setObjectName("settings_window")
        self.settings_save_btn = QtWidgets.QPushButton(self.settings_window)
        self.settings_save_btn.setGeometry(QtCore.QRect(110, 230, 150, 30))
        self.settings_save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_save_btn.setObjectName("settings_save_btn")
        self.settings_cancel_btn = QtWidgets.QPushButton(self.settings_window)
        self.settings_cancel_btn.setGeometry(QtCore.QRect(400, 230, 150, 30))
        self.settings_cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_cancel_btn.setObjectName("settings_cancel_btn")
        self.settings_label_1 = QtWidgets.QLabel(self.settings_window)
        self.settings_label_1.setEnabled(False)
        self.settings_label_1.setGeometry(QtCore.QRect(20, 10, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.settings_label_1.setFont(font)
        self.settings_label_1.setStyleSheet("border: 0px")
        self.settings_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_label_1.setWordWrap(True)
        self.settings_label_1.setObjectName("settings_label_1")
        self.settings_label_2 = QtWidgets.QLabel(self.settings_window)
        self.settings_label_2.setGeometry(QtCore.QRect(10, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.settings_label_2.setFont(font)
        self.settings_label_2.setStyleSheet("border: 0px")
        self.settings_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_label_2.setWordWrap(True)
        self.settings_label_2.setObjectName("settings_label_2")
        self.update_checkbox = QtWidgets.QCheckBox(self.settings_window)
        self.update_checkbox.setGeometry(QtCore.QRect(22, 170, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_checkbox.setFont(font)
        self.update_checkbox.setStyleSheet("border: solid 0px")
        self.update_checkbox.setCheckable(True)
        self.update_checkbox.setChecked(True)
        self.update_checkbox.setObjectName("update_checkbox")
        self.settings_steam_path = QtWidgets.QLineEdit(self.settings_window)
        self.settings_steam_path.setGeometry(QtCore.QRect(20, 104, 621, 31))
        self.settings_steam_path.setStyleSheet("width: 100%;\n"
"font: 10pt \"Consolas\";\n"
"border-radius: 15px;\n"
"border: 1px solid #ffffff;\n"
"padding: 2px 2px 3px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(6, 11, 8);")
        self.settings_steam_path.setObjectName("settings_steam_path")
        self.settings_window.raise_()
        self.profile_create_window.raise_()
        self.set_steam_path_window.raise_()
        self.generic_popup.raise_()
        self.closing_steam.raise_()
        self.main_panel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GreenLuma Reborn Manager"))
        self.profile_name.setPlaceholderText(_translate("MainWindow", "Profile Name"))
        self.create_profile_btn.setText(_translate("MainWindow", "Create"))
        self.cancel_profile_btn.setText(_translate("MainWindow", "Cancel"))
        self.label_3.setText(_translate("MainWindow", "Profile Name:"))
        self.save_steam_path.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Steam Path"))
        self.cancel_steam_path_btn.setText(_translate("MainWindow", "Cancel"))
        self.steam_path.setPlaceholderText(_translate("MainWindow", "Path"))
        self.popup_btn1.setText(_translate("MainWindow", "Ok"))
        self.popup_btn2.setText(_translate("MainWindow", "Cancel"))
        self.popup_text.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Closing Steam..."))
        self.label.setText(_translate("MainWindow", "Profile"))
        self.remove_game.setText(_translate("MainWindow", "Remove Games"))
        self.compatibility_mode_checkbox.setToolTip(_translate("MainWindow", "Enable this if you\'re having problem with AV detection"))
        self.compatibility_mode_checkbox.setText(_translate("MainWindow", "Compatibility Mode"))
        self.label_5.setText(_translate("MainWindow", "Searching..."))
        self.create_profile.setText(_translate("MainWindow", "New Profile"))
        self.label_4.setText(_translate("MainWindow", "GreenLuma Reborn Manager"))
        self.run_GLR_btn.setText(_translate("MainWindow", "Run GLR"))
        self.add_to_profile.setText(_translate("MainWindow", "Add Games"))
        self.games_list.setSortingEnabled(True)
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.label_2.setText(_translate("MainWindow", "Games List"))
        self.delete_profile.setText(_translate("MainWindow", "Delete Profile"))
        self.game_search_text.setPlaceholderText(_translate("MainWindow", "Search Game"))
        self.no_hook_checkbox.setText(_translate("MainWindow", "NoHook"))
        self.version_label.setText(_translate("MainWindow", "v0.0.0"))
        self.settings_save_btn.setText(_translate("MainWindow", "Save"))
        self.settings_cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.settings_label_1.setText(_translate("MainWindow", "Settings"))
        self.settings_label_2.setText(_translate("MainWindow", "Steam Path:"))
        self.update_checkbox.setToolTip(_translate("MainWindow", "Enable Automatic Updates"))
        self.update_checkbox.setText(_translate("MainWindow", "Check For Updates On Startup"))
        self.settings_steam_path.setPlaceholderText(_translate("MainWindow", "Path"))


from Qt import resources_rc
