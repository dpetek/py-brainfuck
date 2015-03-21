import sys

class InputStream(object):
    def get_char(self):
        raise NotImplementedException("This is not a concrete implementation")

class StringInputStream(InputStream):
    def __init__(self, s):
        self.buffer = s
        self.index = 0
    def get_char(self):
        if self.index >= len(self.buffer):
            raise IndexError("Input buffer out of range.")
        return self.buffer[self.index]

class FileInputStream(InputStream):
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath)
    def get_char(self):
        c = self.file.read(1)
        if not c:
            raise EOFError("End of file.")
        return c

class StdinInputStream(InputStream):
    def __init__(self):
        pass

    def get_char(self):
        c = sys.stdin.read(1)
        if not c:
            raise EOFError("Stdin interrupt.")
        return c
