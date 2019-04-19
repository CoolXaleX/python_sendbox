import tempfile
import os.path


class File:
    def __init__(self, path):
        self.path = path

    def write(self, string):
        with open(self.path, "w+") as f:
            f.write(string)

    def __str__(self):
        return self.path

    def __readFromPath(self, path):
        with open(path, "r") as f:
            return f.read()
    
    def __add__(self, obj):
        with open(path.join(tempfile.gettempdir(), path.join(self.path, obj.path)), "w+") as tf:
            tf.write(self.__readFromPath(self.path))
            tf.write(self.__readFromPath(obj.path))
        