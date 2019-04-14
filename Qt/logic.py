from Qt.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QShortcut, QListWidget
from PyQt5.QtCore import  QAbstractItemModel, Qt, QModelIndex, QVariant, QThread, QEvent, pyqtSignal
from PyQt5.QtGui import QKeySequence, QIcon
import core
import subprocess
import psutil

profile_manager = core.ProfileManager()
games = []

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.setup()
        self.connect_components()
        self.search_thread = SearchThread("")
    
    def setup(self):
        self.setWindowIcon(QIcon("icon.ico"))
        self.main_window.profile_create_window.setHidden(True)
        self.main_window.searching_frame.setHidden(True)
        self.main_window.set_steam_path_window.setHidden(True)
        self.main_window.closing_steam.setHidden(True)
        self.main_window.generic_popup.setHidden(True)
        self.main_window.no_hook_checkbox.setChecked(core.config.no_hook)
        self.main_window.no_update_checkbox.setChecked(core.config.no_update)
        self.populate_list(self.main_window.games_list, games)
        self.main_window.games_list.dropEvent = self.drop_event_handler
        self.populate_table(self.main_window.search_result, games)
        self.show_profile_names()
        self.show_profile_games(profile_manager.profiles[self.main_window.profile_selector.currentText()])
        self.setup_steam_path()
        self.setup_search_table()

        #Shortcuts
        del_game = QShortcut(QKeySequence(Qt.Key_Delete), self.main_window.games_list)
        del_game.activated.connect(self.remove_selected)

    def connect_components(self):
        self.main_window.create_profile.clicked.connect(self.toggle_profile_window)
        self.main_window.create_profile_btn.clicked.connect(self.create_profile)
        self.main_window.cancel_profile_btn.clicked.connect(self.toggle_profile_window)
        self.main_window.change_steam_path_btn.clicked.connect(self.toggle_steam_path_window)
        self.main_window.save_steam_path.clicked.connect(self.set_steam_path)
        self.main_window.cancel_steam_path_btn.clicked.connect(self.toggle_steam_path_window)
        self.main_window.search_btn.clicked.connect(self.search_games)
        self.main_window.game_search_text.returnPressed.connect(self.search_games)
        self.main_window.add_to_profile.clicked.connect(self.add_selected)
        self.main_window.profile_selector.currentTextChanged.connect(self.select_profile)
        self.main_window.generate_btn.clicked.connect(self.generate_app_list)
        self.main_window.run_GLR_btn.clicked.connect(lambda : self.show_popup("This will restart Steam if it's open do you want to continue?", self.run_GLR))
        self.main_window.remove_game.clicked.connect(self.remove_selected)
        self.main_window.delete_profile.clicked.connect(self.delete_profile)
        self.main_window.popup_btn2.clicked.connect(self.toggle_popup)
    
    def toggle_profile_window(self):
        self.toggle_hidden(self.main_window.profile_create_window)
        self.toggle_enable(self.main_window.profile_create_window)
    
    def create_profile(self):
        name = self.main_window.profile_name.text()
        if name != "":
            profile_manager.create_profile(name)
            self.main_window.profile_selector.addItem(name)

        self.toggle_profile_window()
        self.main_window.profile_name.clear()

        self.main_window.profile_selector.setCurrentIndex(self.main_window.profile_selector.count() - 1)

    def delete_profile(self):
        name = self.main_window.profile_selector.currentText()
        if name == "default":
            return
        
        profile_manager.remove_profile(name)

        index = self.main_window.profile_selector.currentIndex()
        self.main_window.profile_selector.removeItem(index)

    def select_profile(self, name):
        core.config.last_profile = name
        core.config.export_config()

        self.show_profile_games(profile_manager.profiles[name])

    def search_games(self):
        query = self.main_window.game_search_text.text()
        if query == "":
            return
        
        self.toggle_hidden(self.main_window.searching_frame)

        self.search_thread = SearchThread(query)
        self.search_thread.signal.connect(self.search_games_done)
        self.search_thread.start()

    def search_games_done(self, result):
        if type(result) is list:
            self.toggle_hidden(self.main_window.searching_frame)
            self.populate_table(self.main_window.search_result, result)
        else:
            self.toggle_hidden(self.main_window.searching_frame)
            self.show_popup("Can't connect to Steamdb. Check if you have internet connection.", self.dummy_callback)

    def setup_search_table(self):
        self.main_window.search_result.setColumnCount(3)

        header = self.main_window.search_result.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setMaximumSectionSize(580)
        header.sectionClicked.connect(lambda index : self.main_window.search_result.horizontalHeader().setSortIndicator(index, Qt.AscendingOrder))

        self.main_window.search_result.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.main_window.search_result.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.main_window.search_result.setHorizontalHeaderItem(2, QTableWidgetItem("Type"))
    
    def populate_list(self, list, data):
        list.clear()
        for item in data:
            list.addItem(item.name)

    def generate_app_list(self):
        if len(profile_manager.profiles[self.main_window.profile_selector.currentText()].games) == 0:
            self.show_popup("No games to generate.", self.dummy_callback)
            return

        selected_profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]
        core.createFiles(selected_profile.games)
        self.show_popup("AppList Folder Generated", self.dummy_callback)

    def generate_app_list_no_popup(self):
        if len(profile_manager.profiles[self.main_window.profile_selector.currentText()].games) == 0:
            self.show_popup("No games to generate.", self.dummy_callback)
            return

        selected_profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]
        core.createFiles(selected_profile.games)

    def show_profile_games(self, profile):
        list = self.main_window.games_list

        self.populate_list(list, profile.games)

    def show_profile_names(self):
        data = profile_manager.profiles.values()

        if core.config.last_profile in profile_manager.profiles.keys():
            self.main_window.profile_selector.addItem(core.config.last_profile)

        for item in data:
            if item.name != core.config.last_profile:
                self.main_window.profile_selector.addItem(item.name)

    def populate_table(self, table, data):
        #Reset
        table.setSortingEnabled(False)
        table.clearSelection()
        table.setRowCount(0)
        #----
        table.setRowCount(len(data))

        for i, item in enumerate(data):
            for j, value in enumerate(item.to_list()):
                table_item = QTableWidgetItem(value)
                if j == 1:
                    table_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
                else:
                    table_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                table.setItem(i, j, table_item)

        table.setSortingEnabled(True)

    def add_selected(self):
        items = self.main_window.search_result.selectedItems()
        if len(items) == 0:
            return
        
        profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]

        for game in core.Game.from_table_list(items):
            if game not in profile.games:
                profile.add_game(game)

        self.show_profile_games(profile)
        profile.export_profile()

    def remove_selected(self):
        items = self.main_window.games_list.selectedItems()
        if len(items) == 0:
            return
        
        profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]

        for item in items:
            profile.remove_game(item.text())

        self.show_profile_games(profile)
        profile.export_profile()

    def toggle_hidden(self, widget):
        widget.setHidden(not widget.isHidden())
        self.repaint()

    def toggle_enable(self, widget):
        widget.setEnabled(not widget.isEnabled())

    def toggle_steam_path_window(self):
        self.toggle_hidden(self.main_window.set_steam_path_window)
        self.toggle_enable(self.main_window.set_steam_path_window)

    def set_steam_path(self):
        path = self.main_window.steam_path.text()
        if not path == "":
            core.config.steam_path = path
            core.config.is_path_setup = True
            core.config.export_config()
        
        self.toggle_steam_path_window()

    def setup_steam_path(self):
        if core.config.is_path_setup:
            self.main_window.steam_path.setText(core.config.steam_path)
            return
        
        self.toggle_steam_path_window()

    def drop_event_handler(self, event):
        self.add_selected()

    def show_popup(self, message, callback):
        self.main_window.popup_text.setText(message)
        self.main_window.popup_btn1.clicked.connect(callback)

        self.toggle_popup()

    def dummy_callback(self):
        self.close_popup()

    def toggle_popup(self):
        self.toggle_hidden(self.main_window.generic_popup)
        self.toggle_enable(self.main_window.generic_popup)
    
    def close_popup(self):
        self.main_window.generic_popup.setHidden(True)
        self.main_window.generic_popup.setEnabled(False)

    def is_steam_running(self):
        for process in psutil.process_iter():
            if process.name() == "Steam.exe" or process.name() == "SteamService.exe" or process.name() == "steamwebhelper.exe":
                return True
        
        return False

    def run_GLR(self):
        self.close_popup()

        if len(profile_manager.profiles[self.main_window.profile_selector.currentText()].games) == 0:
            self.show_popup("No games to generate.", self.dummy_callback)
            return
        self.generate_app_list_no_popup()

        args = ["GreenLuma_Reborn.exe", "-NoQuestion"]
        core.config.no_hook = self.main_window.no_hook_checkbox.isChecked()
        core.config.no_update = self.main_window.no_update_checkbox.isChecked()
        core.config.export_config()

        if core.config.no_hook:
            args.append("-NoHook")
        if core.config.no_update:
            args.append("-NoUpdate")

        core.os.chdir(core.config.steam_path)
        if self.is_steam_running():
            self.toggle_hidden(self.main_window.closing_steam)
            subprocess.run(["Steam.exe", "-shutdown"]) #Shutdown Steam
            while self.is_steam_running():
                core.time.sleep(1)
            core.time.sleep(1)
        
        subprocess.run(args)
        self.close()

class SearchThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, query):
        super(SearchThread, self).__init__()
        self.query = query

    def run(self):
        result = core.queryGames(self.query)
        self.signal.emit(result)
