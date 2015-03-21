import os, sys, re

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

    def run(self, input_stream, output_stream = sys.stdout, num_iters = None):
        num_iters = -1 if num_iters  == None else num_iters
        current_iter = 0
        while current_iter < num_iters and self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]

            if command == "<" or command == ">":
                self.data_pointer += 1 if command  == ">" else -1
            elif command == "+" or command == "-":
                delta = 1 if command == "+" else -1
                self.data[self.data_pointer] = self.data.get(self.data_pointer, 0 + delta)
            elif command == ",":
                self.data[self.data_pointer] = ord(input_stream.get_char())
            elif command == '.':
                output_stream.put_char(chr(self.data.get(self.data_pointer, 0)))

            code_pointer = self.code_pointer + 1
            if command == "[" and self.data.get(self.data_pointer, 0) == 0:
                code_pointer = self.jumps[self.code_pointer]
            if command == "[" and not self.data.get(self.data_pointer, 0) == 0:
                code_pointer = self.jumps[self.code_pointer]

            self.code_pointer = code_pointer
            current_iter += 1

    def run_for_string(self, input_string, output_stream.sys.stdout, num_iters = None):
        pass
