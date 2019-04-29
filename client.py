import asyncio
import time


def add_elem(diction, key, value):
    item = diction.get(key)
    if item:
        item.append(value)
    else:
        item = [value]
    diction[key] = item
    return diction


class Client:

    @staticmethod
    def __conv_put_req(key, value, timestamp):
        if timestamp is None:
            timestamp = str(int(time.time()))
        return "put {} {} {}\n".format(key, value, timestamp)

    @staticmethod
    def __conv_put_res(message):
        resp = message.split("\n")
        # print(resp)
        if resp[0] != "ok":
            raise ClientError()

    @staticmethod
    def __conv_get_req(key):
        return "get {}\n".format(key)

    @staticmethod
    def __conv_get_res(message):
        resp = message.split("\n")
        # print(resp)
        if resp[0] == "ok":
            i = 1
            d = {}
            while True:
                if resp[i]:
                    items = resp[i].split(" ")
                    add_elem(d, items[0], (int(items[2]), float(items[1])))
                else:
                    break
                i += 1
            return d
        else:
            raise ClientError()

    async def __send_message(self, message):
        reader, writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)
        writer.write(message.encode())
        data = await reader.read(1024)
        writer.close()
        return data.decode()

    def __init__(self, host, port, timeout=None):
        self.loop = asyncio.get_event_loop()
        self.host = host
        self.port = port
        self.timeout = timeout

    def __del__(self):
        self.loop.close()

    def get(self, key):
        response = self.loop.run_until_complete(self.__send_message(self.__conv_get_req(key)))
        return self.__conv_get_res(response)

    def put(self, key, value, timestamp=None):
        response = self.loop.run_until_complete(self.__send_message(self.__conv_put_req(key, value, timestamp)))
        return self.__conv_put_res(response)


class ClientError(Exception):
    pass
