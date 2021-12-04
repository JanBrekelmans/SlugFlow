from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class OpenFoamSettingsTab:
    def __init__(self, parent_tab_pane: QTabWidget):
        self.parent_tab_pane = parent_tab_pane

        self.tab = QTabWidget()

        self.parent_tab_pane.addTab(self.tab, "Settings")