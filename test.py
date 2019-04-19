import file.File
import tempfile
import os.path


fileItem = file.File(path.join(tempfile.gettempdir(), "test.data"))
fileItem.write("testMsg")