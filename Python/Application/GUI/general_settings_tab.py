from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..OpenFoamSettingsGenerator import Settings

class GeneralSettingsTab():
    def __init__(self, settings : Settings):
        self.settings = settings
        self.keys = settings.keys

        self.tab = QTabWidget()
        self.layout = QGridLayout()

        self.current_value_dict = {}

        self._init_input_fields()

    def _init_input_fields(self):

        for i,key in enumerate(self.keys):
            label = QLabel(key)
            self.layout.addItem(label, i, 0)

            if self.settings[key] is list:
                input_field = QComboBox()
                for val in self.settings[key]:
                    input_field.addItem(val)
            else:
                input_field = QLineEdit()

            self.layout.addItem(input_field, i, 1)

            self.current_value_dict[key] = input_field