import os, sys, re
from bf_input_stream import StdinInputStream
from bf_output_stream import StdoutOutputStream

class Brainfuck(object):
    """
        Python brainf*ck language wrapper and interpreter.
        Brainfuck object is saving the whole state, so interpreter can run
        for only couple iteration and be restarted at any time.
    """
    def __init__(self, code):
        self.jumps = {}
        self.data = {}
        self.data_pointer = 0
        self.code_pointer = 0
        self.code = code
        self.__code_cleanup()
        self.__preprocess_jumps()

    def __code_cleanup(self):
        """
            Remove all non-interesting characters from the code.
        """
        self.code = re.sub(r"[^\>\<\.\,\+\-\[\]]", "", self.code)

    def __preprocess_jumps(self):
        """
            Pre-calculate jumps map defined by '[' and ']' characters.
        """
        stack = []
        for i, c in enumerate(self.code):
            if c == '[':
                stack.append(i)
            elif c == ']':
                prev = stack.pop()
                self.jumps[i] = prev
                self.jumps[prev] = i

    def __set_data(self, value):
        if value > 255: value -= 256
        if value < 0: value += 256
        self.data[self.data_pointer] = value

    def __get_data(self):
        return self.data.get(self.data_pointer, 0)

    def __increment_data(self, delta):
        self.__set_data(self.data.get(self.data_pointer, 0) + delta)

    def get_jumps_map(self):
        """
            Get jumps destination map for all '[' and ']' in the code.
        """
        return self.jumps

    def get_code(self):
        """
            Get code string (all non-interesting characters filtered out).
        """
        return self.code

    def get_data_map(self):
        """
            Get data values for pointer positions. Returns dictionary (sparse).
        """
        return self.data

    def get_data_pointer_position(self):
        return self.data_pointer

    def get_code_pointer_position(self):
        return self.code_pointer

    def run(self, input_stream = StdinInputStream(), output_stream = StdoutOutputStream(), num_iters = None):
        current_iter = 0
        while (num_iters == None or current_iter < num_iters) and self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]
            if command == "<" or command == ">":
                self.data_pointer += 1 if command  == ">" else -1
            elif command == "+" or command == "-":
                self.__increment_data(1 if command == "+" else -1)
            elif command == ",":
                self.__set_data(ord(input_stream.get_char()))
            elif command == '.':
                output_stream.put_char(chr(self.__get_data()))

            cp = self.code_pointer + 1
            if command == "[" and self.__get_data() == 0:
                cp = self.jumps[self.code_pointer]
            if command == "]" and not self.__get_data() == 0:
                cp = self.jumps[self.code_pointer]

            self.code_pointer = cp
            current_iter += 1
