from . import openfoam_system_settings

class OpenFoamSettings:
    def __init__(self):
        self.blockMeshSettings = openfoam_system_settings.BlockMeshDictSettings()