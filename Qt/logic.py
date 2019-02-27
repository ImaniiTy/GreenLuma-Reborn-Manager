from Qt.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QShortcut
from PyQt5.QtCore import  QAbstractItemModel, Qt, QModelIndex, QVariant, QThread, pyqtSignal
from PyQt5.QtGui import QKeySequence, QIcon
import core

profile_manager = core.ProfileManager()
games = []
games_dict = {}

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
        self.populate_list(self.main_window.games_list, games)
        self.populate_table(self.main_window.search_result, games)
        self.populate_list(self.main_window.profile_selector,profile_manager.profiles.values())
        self.show_profile_games(profile_manager.profiles[self.main_window.profile_selector.currentText()])
        self.setup_steam_path()

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
        self.main_window.profile_selector.currentTextChanged.connect(lambda name : self.show_profile_games(profile_manager.profiles[name]))
        self.main_window.generate_btn.clicked.connect(self.generate_app_list)
        self.main_window.remove_game.clicked.connect(self.remove_selected)
        self.main_window.delete_profile.clicked.connect(self.delete_profile)
    
    def toggle_profile_window(self):
        self.toggle_hidden(self.main_window.profile_create_window)
        self.toggle_enable(self.main_window.profile_create_window)
    
    def create_profile(self):
        name = self.main_window.profile_name.text()
        profile_manager.create_profile(name)
        self.main_window.profile_selector.addItem(name)

        self.toggle_profile_window()
        self.main_window.profile_name.clear()

    def delete_profile(self):
        name = self.main_window.profile_selector.currentText()
        if name == "default":
            return
        
        profile_manager.remove_profile(name)

        index = self.main_window.profile_selector.currentIndex()
        self.main_window.profile_selector.removeItem(index)

    def search_games(self):
        query = self.main_window.game_search_text.text()
        if query == "":
            return
        
        self.toggle_hidden(self.main_window.searching_frame)

        self.search_thread = SearchThread(query)
        self.search_thread.signal.connect(self.search_games_done)
        self.search_thread.start()

    def search_games_done(self, result):
        self.toggle_hidden(self.main_window.searching_frame)
        self.populate_table(self.main_window.search_result, result)

    
    def populate_list(self, list, data):
        list.clear()
        for item in data:
            list.addItem(item.name)

    def generate_app_list(self):
        selected_profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]
        core.createFiles(selected_profile.games)

    def show_profile_games(self, profile):
        list = self.main_window.games_list

        self.populate_list(list, profile.games)

    def populate_table(self, table, data):
        #Reset
        table.setRowCount(0)
        table.setSortingEnabled(False)
        #----

        table.setRowCount(len(data))
        table.setColumnCount(3)
        table.setSortingEnabled(True)

        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setMaximumSectionSize(580)
        header.sectionClicked.connect(lambda index : self.main_window.search_result.horizontalHeader().setSortIndicator(index, Qt.AscendingOrder))

        table.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        table.setHorizontalHeaderItem(2, QTableWidgetItem("Type"))
        for i, item in enumerate(data):
            games_dict[item.name] = item
            for j, value in enumerate(item.to_list()):
                table_item = QTableWidgetItem(value)
                print(value)
                if j == 1:
                    table_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                else:
                    table_item.setFlags(Qt.NoItemFlags)
                
                table.setItem(i, j, table_item)

    def add_selected(self):
        items = self.main_window.search_result.selectedItems()
        if len(items) == 0:
            return
        
        profile = profile_manager.profiles[self.main_window.profile_selector.currentText()]

        for item in items:
            profile.add_game(games_dict[item.text()])

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
            return
        
        self.toggle_steam_path_window()

class SearchThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, query):
        super(SearchThread, self).__init__()
        self.query = query

    def run(self):
        result = core.queryGames(self.query)
        self.signal.emit(result)
