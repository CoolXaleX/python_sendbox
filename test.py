import file
import tempfile
import os


file1 = file.File(os.path.join('F:\\WORK\\python_sendbox', "test1.data"))
file1.write("""testMsg1
testMsg1""")

file2 = file.File(os.path.join('F:\\WORK\\python_sendbox', "test2.data"))
file2.write("testMsg2")

file3 = file1 + file2
for f in file3:
    print(f)
