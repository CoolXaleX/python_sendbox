# import file
# import os
#
#
# file1 = file.File(os.path.join('F:\\WORK\\python_sendbox', "test1.data"))
# file1.write("""testMsg1
# testMsg1""")
#
# file2 = file.File(os.path.join('F:\\WORK\\python_sendbox', "test2.data"))
# file2.write("testMsg2")
#
# file3 = file1 + file2
# for f in file3:
#     print(f)
from value import Value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

    def _get_commission(self):
        return self.commission


new_account = Account(0.1)


for i in range(0, 110, 10):
    new_account.amount = i
    print(str(i) + " " + str(new_account.amount))
