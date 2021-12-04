from . import settings

class BlockMeshDictSettings(settings.Settings):
    def __init__(self):
        self.keys = ["cX", "cY", "cZ", "numX", "numZ"]

        self.settings_dict = {}

        for key in self.keys:
            self.settings_dict[key] = None

        super().__init__()


