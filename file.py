import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

    def write(self, string):
        with open(self.path, "w+") as f:
            f.write(string)

    def __str__(self):
        return self.path

    def read(self, path):
        with open(path, "r") as f:
            return f.read()

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line

    def __add__(self, obj):
        path = os.path.join(tempfile.gettempdir(), os.path.basename(self.path) + os.path.basename(obj.path))
        with open(path, "w+") as tf:
            f1 = self.read(self.path)
            f2 = self.read(obj.path)
            tf.write(f1 + f2)
        return File(path)
