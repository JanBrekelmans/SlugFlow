import sys
from PyQt5.QtWidgets import *

from . import openfoam_settings_tab

class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.window = QMainWindow()
        self.window.setWindowTitle("Slug Flow Case Generator")

        self.window.setGeometry(0, 0, 600, 480)

        self.main_layout = QVBoxLayout(self.window)
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.window.setCentralWidget(widget)

        self._init_tab_widget()

        self.window.show()
        sys.exit(self.app.exec_())

    def _init_tab_widget(self):
        self.tab_pane = QTabWidget()

        self.settings_tab = openfoam_settings_tab.OpenFoamSettingsTab(self.tab_pane)

        self.tab_pane.resize(600, 480)
        self.main_layout.addWidget(self.tab_pane)


if __name__ == "__main__":
    m = MainWindow()