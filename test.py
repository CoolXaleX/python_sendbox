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
# from value import Value
#
#
# class Account:
#     amount = Value()
#
#     def __init__(self, commission):
#         self.commission = commission
#
#     def _get_commission(self):
#         return self.commission
#
#
# new_account = Account(0.1)
#
#
# for i in range(0, 110, 10):
#     new_account.amount = i
#     print(str(i) + " " + str(new_account.amount))
from client import Client
client = Client("127.0.0.1", 10001)
print(client.put("palm.cpu", 0.5, timestamp=1150864247))
print(client.put("palm.cpu", 2.0, timestamp=1150864248))
print(client.put("palm.cpu", 0.5, timestamp=1150864248))

print(client.put("eardrum.cpu", 3, timestamp=1150864250))
print(client.put("eardrum.cpu", 4, timestamp=1150864251))
print(client.put("eardrum.memory", 4200000))

print(client.get("*"))

