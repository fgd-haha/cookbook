"""
8.19_实现状态对象或者状态机
"""


class ConnectionState:
    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn):
        raise NotImplementedError()


class OpenConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(CloseConnectionState)

    @staticmethod
    def read(conn):
        print('read')

    @staticmethod
    def write(conn):
        print('write')


class CloseConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

    @staticmethod
    def read(conn):
        raise RuntimeError('not open')

    @staticmethod
    def write(conn):
        raise RuntimeError('not open')


class Connection:
    def __init__(self):
        self._state = CloseConnectionState

    def new_state(self, conn):
        self._state = conn

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

    def read(self):
        return self._state.read(self)

    def write(self):
        return self._state.write(self)


c = Connection()
c.open()
# c.close()
c.read()
c.write()
