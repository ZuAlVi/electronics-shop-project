class InstantiateCSVError(Exception):
    def __init__(self, *args):
        """Файл item.csv поврежден"""
        if args:
            self.message = args[0]
        else:
            self.message = 'InstantiateCSVError: Файл item.csv поврежден'

