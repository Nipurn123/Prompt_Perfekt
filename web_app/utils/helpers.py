import datetime

class Helpers:
    def __init__(self):
        pass

    @staticmethod
    def get_current_timestamp():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
