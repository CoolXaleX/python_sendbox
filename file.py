import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path

    def write(self, string):
        with open(self.path, "w+") as f:
            f.write(string)

    def __str__(self):
        return self.path

    def read(self, path):
        with open(path, "r") as f:
            return f.read()

    def __iter__(self):
        with open(self.path, "r") as f:
            return iter(f.readlines())

    def __add__(self, obj):
        path = os.path.join(tempfile.gettempdir(), os.path.basename(self.path) + os.path.basename(obj.path))
        with open(path, "w+") as tf:
            f1 = self.read(self.path)
            f2 = self.read(obj.path)
            tf.write(f1 + f2)
        return File(path)
