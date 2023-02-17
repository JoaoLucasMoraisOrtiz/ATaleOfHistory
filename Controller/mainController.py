from View import View
from Additional import Configurations

class mainController:   

    def start():
        helper = Configurations.Helper
        config = helper.getConfigs()
        mainWindow = View.View.window((255,255,255), config['width'], config['heigth'], config['mainWindowName'])
        return mainWindow
    
    def stop():
        return False
