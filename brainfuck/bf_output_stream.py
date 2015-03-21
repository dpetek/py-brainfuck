import sys

class OutputStream(object):
    def put_char(self, c):
        raise NotImplementedError("This is not a concrete implementation.")

class StdoutOutputStream(OutputStream):
    def __init__(self):
        pass

    def put_char(self, c):
        sys.stdout.write(c)

class FileOuputStream(OutputStream):
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, "w")

    def put_char(self, c):
        self.file.write(c)

class StringOutputStream(OutputStream):
    def __init__(self):
        self.buffer = ""

    def put_char(self, c):
        self.buffer += c
    
    def get_string(self):
        return self.buffer
