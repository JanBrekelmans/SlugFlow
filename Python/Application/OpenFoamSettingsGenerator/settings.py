class Settings:
    def __init__(self):
        self.reset()

    def reset(self):
        self.values_dict = {}

        for key in self.settings_dict.keys():
            self.values_dict[key] = None

    def add_setting(self, name, val):
        self.values_dict[name] = val

    def remove_setting(self, name):
        self.values_dict.pop(name)