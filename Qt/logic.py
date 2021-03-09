from Qt.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QShortcut, QListWidget, QTableView
from PyQt5.QtCore import  QAbstractItemModel, Qt, QModelIndex, QVariant, QThread, QEvent, pyqtSignal, QAbstractTableModel, QSortFilterProxyModel
from PyQt5.QtGui import QKeySequence, QIcon
from shutil import copyfile
import core
import subprocess
import psutil
import fileinput

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

        # Hidde Other Windows
        self.main_window.profile_create_window.setHidden(True)
        self.main_window.searching_frame.setHidden(True)
        self.main_window.set_steam_path_window.setHidden(True)
        self.main_window.closing_steam.setHidden(True)
        self.main_window.generic_popup.setHidden(True)
        self.main_window.settings_window.setHidden(True)
        #-------

        self.main_window.version_label.setText("v{0}".format(core.CURRENT_VERSION))
        self.main_window.no_hook_checkbox.setChecked(core.config.no_hook)
        self.main_window.compatibility_mode_checkbox.setChecked(core.config.compatibility_mode)
        self.populate_list(self.main_window.games_list, games)
        self.main_window.games_list.dropEvent = self.drop_event_handler
        self.populate_table(self.main_window.search_result)
        self.show_profile_names()
        self.show_profile_games(profile_manager.profiles[self.main_window.profile_selector.currentText()])
        self.setup_steam_path()
        self.setup_search_table()
        # self.main_window.main_panel.raise_()

        # Settings Window Setup
        self.main_window.update_checkbox.setChecked(core.config.check_update)

        # Shortcuts
        del_game = QShortcut(QKeySequence(Qt.Key_Delete), self.main_window.games_list)
        del_game.activated.connect(self.remove_selected)

    def connect_components(self):
        # Profile
        self.main_window.create_profile.clicked.connect(lambda : self.toggle_widget(self.main_window.profile_create_window))
        self.main_window.create_profile_btn.clicked.connect(self.create_profile)
        self.main_window.cancel_profile_btn.clicked.connect(lambda : self.toggle_widget(self.main_window.profile_create_window))
        self.main_window.profile_selector.currentTextChanged.connect(self.select_profile)
        self.main_window.remove_game.clicked.connect(self.remove_selected)
        self.main_window.delete_profile.clicked.connect(self.delete_profile)

        # Steam Path
        self.main_window.save_steam_path.clicked.connect(self.set_steam_path)
        self.main_window.cancel_steam_path_btn.clicked.connect(lambda : self.toggle_widget(self.main_window.set_steam_path_window))

        # Search Area
        self.main_window.search_btn.clicked.connect(self.search_games)
        self.main_window.game_search_text.returnPressed.connect(self.search_games)
        self.main_window.add_to_profile.clicked.connect(self.add_selected)

        # Main Buttons
        self.main_window.generate_btn.clicked.connect(self.generate_app_list)
        self.main_window.run_GLR_btn.clicked.connect(lambda : self.show_popup("This will restart Steam if it's open do you want to continue?", self.run_GLR))
        
        # Settings Window
        self.main_window.settings_btn.clicked.connect(lambda : self.toggle_widget(self.main_window.settings_window))
        self.main_window.settings_save_btn.clicked.connect(self.save_settings)
        self.main_window.settings_cancel_btn.clicked.connect(lambda : self.toggle_widget(self.main_window.settings_window))
        
        # Popup Window
        self.main_window.popup_btn2.clicked.connect(lambda : self.toggle_widget(self.main_window.generic_popup, True))
    
    # Profile Functions
    def create_profile(self):
        name = self.main_window.profile_name.text()
        if name != "":
            profile_manager.create_profile(name)
            self.main_window.profile_selector.addItem(name)
            self.main_window.profile_name.clear()

            self.main_window.profile_selector.setCurrentIndex(self.main_window.profile_selector.count() - 1)
        
        self.toggle_widget(self.main_window.profile_create_window)

    def delete_profile(self):
        name = self.main_window.profile_selector.currentText()
        if name == "default":
            return
        
        profile_manager.remove_profile(name)

        index = self.main_window.profile_selector.currentIndex()
        self.main_window.profile_selector.removeItem(index)

    def select_profile(self, name):
        with core.get_config() as config:
            config.last_profile = name

        self.show_profile_games(profile_manager.profiles[name])

    def show_profile_games(self, profile):
        list_ = self.main_window.games_list

        self.populate_list(list_, profile.games)

    def show_profile_names(self):
        data = profile_manager.profiles.values()

        if core.config.last_profile in profile_manager.profiles.keys():
            self.main_window.profile_selector.addItem(core.config.last_profile)

        for item in data:
            if item.name != core.config.last_profile:
                self.main_window.profile_selector.addItem(item.name)

    # Search Functions
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
            self.populate_table(self.main_window.search_result,result)
        else:
            self.toggle_hidden(self.main_window.searching_frame)
            self.show_popup("Can't connect to Steam. Check if you have internet connection.", lambda : self.toggle_widget(self.main_window.generic_popup, True))

    def setup_search_table(self):
        h_header = self.main_window.search_result.horizontalHeader()
        h_header.setSectionResizeMode(1,QHeaderView.Stretch)
        h_header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        h_header.setMaximumSectionSize(620)

    def populate_table(self, table: QTableView, data=[]):
        model = TableModel(data)
        sortable_model = QSortFilterProxyModel(model)
        sortable_model.setSourceModel(model)
        table.setModel(sortable_model)
    
    def populate_list(self, list_, data):
        list_.clear()
        for item in data:
            list_.addItem(item.name)

    # Search Table and Profile Interaction Functions
    def add_selected(self):
        items = [selected.data() for selected in self.main_window.search_result.selectedIndexes()]
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

    # Settings Functions
    def save_settings(self):
        with core.get_config() as config:
            config.steam_path = self.main_window.settings_steam_path.text()
            config.check_update = self.main_window.update_checkbox.isChecked()

        self.toggle_widget(self.main_window.settings_window)

    # Generation Functions
    def run_GLR(self):
        self.toggle_widget(self.main_window.generic_popup,True)

        if not self.generate_app_list(False):
            return

        args = ["DLLInjector.exe"]
        self.replaceConfig("CreateFiles", " 1")
        self.replaceConfig("FileToCreate_1", " NoQuestion.bin")
        
        with core.get_config() as config:
            config.no_hook = self.main_window.no_hook_checkbox.isChecked()
            config.compatibility_mode = self.main_window.compatibility_mode_checkbox.isChecked()

        # if : else used instead of ternary operator for better readability
        if core.config.compatibility_mode:
            self.replaceConfig("EnableMitigationsOnChildProcess"," 0")
        else:
            self.replaceConfig("EnableMitigationsOnChildProcess"," 1")

        if core.config.no_hook:
            self.replaceConfig("CommandLine","")
            self.replaceConfig("WaitForProcessTermination"," 0")
            self.replaceConfig("EnableFakeParentProcess"," 1")
            self.replaceConfig("CreateFiles", " 2")
            self.replaceConfig("FileToCreate_2", " StealthMode.bin", True)
        else:
            self.replaceConfig("CommandLine"," -inhibitbootstrap")
            self.replaceConfig("WaitForProcessTermination"," 1")
            self.replaceConfig("EnableFakeParentProcess"," 0")
            self.replaceConfig("CreateFiles", " 1")
            self.replaceConfig("FileToCreate_2", "", True)


        core.os.chdir(core.config.steam_path)
        if self.is_steam_running():
            self.toggle_widget(self.main_window.closing_steam)
            subprocess.run(["Steam.exe", "-shutdown"]) #Shutdown Steam
            while self.is_steam_running():
                core.time.sleep(1)
            core.time.sleep(2)
        
        subprocess.Popen(args)
        self.close()

    def generate_app_list(self, popup = True):
        selected_profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]

        if len(selected_profile.games) == 0:
            self.show_popup("No games to generate.", lambda : self.toggle_widget(self.main_window.generic_popup,True))
            return False
        
        core.createFiles(selected_profile.games)
        if(popup):
            self.show_popup("AppList Folder Generated", lambda : self.toggle_widget(self.main_window.generic_popup, True))

        return True

    # Util Functions
    def toggle_hidden(self, widget):
        widget.setHidden(not widget.isHidden())
        self.repaint()

    def toggle_enable(self, widget):
        widget.setEnabled(not widget.isEnabled())

    def toggle_widget(self, widget, force_close = False):
        if force_close:
            widget.lower()
            widget.setHidden(True)
            widget.setEnabled(False)
            return

        if widget.isHidden():
            widget.raise_()
        else:
            widget.lower()
        
        self.toggle_hidden(widget)
        self.toggle_enable(widget)

    def set_steam_path(self):
        path = self.main_window.steam_path.text()
        if not path == "":
            with core.get_config() as config:
                config.steam_path = path
        
        self.toggle_widget(self.main_window.set_steam_path_window)

    def setup_steam_path(self):
        if core.config.steam_path != "":
            self.main_window.settings_steam_path.setText(core.config.steam_path)
            return

        self.toggle_widget(self.main_window.set_steam_path_window)

    def drop_event_handler(self, event):
        self.add_selected()

    def show_popup(self, message, callback):
        self.main_window.popup_text.setText(message)
        self.main_window.popup_btn1.clicked.connect(callback)

        self.toggle_widget(self.main_window.generic_popup)

    def is_steam_running(self):
        for process in psutil.process_iter():
            if process.name() == "Steam.exe" or process.name() == "SteamService.exe" or process.name() == "steamwebhelper.exe" or process.name() == "DLLInjector.exe":
                return True
        
        return False

    def replaceConfig(self, name, new_value, append = False):
        found = False
        with fileinput.input(core.config.steam_path + "/DllInjector.ini", inplace=True) as fp:
            for line in fp:
                if not line.startswith("#"):
                    tokens = line.split("=")
                    if tokens[0].strip() == name:
                        found = True
                        tokens[1] = new_value
                        line = "=".join(tokens) + "\n"
                print(line, end = "")
            
        if append and not found:
            with open(core.config.steam_path + "/DllInjector.ini", "at") as f:
                f.write("\n{0} = {1}".format(name, new_value))

class SearchThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, query):
        super(SearchThread, self).__init__()
        self.query = query

    def run(self):
        result = core.queryGames(self.query)
        self.signal.emit(result)

class TableModel(QAbstractTableModel):
    def __init__(self, datain=[], parent=None):
        super().__init__(parent=parent)
        self.datain = datain
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.datain)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return f"{self.datain[index.row()][index.column()]}"
        if index.column() == 2 and role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return QVariant()

    def headerData(self, index, QtOrientation, role=Qt.DisplayRole):
        names = ["Id", "Name", "Type"]
        if role == Qt.DisplayRole:
            return names[index]
        else:
            return QVariant()

    def flags(self, index):
        if index.column() == 1:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable