class FileReader:

    def __init__(self, path):
        self._path = path

    def read(self):
        result = ""
        try:
            with open(self._path) as f:
                result = f.read()
        except IOError:
            pass
        finally:
            return result
