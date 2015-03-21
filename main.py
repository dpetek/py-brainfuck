from brainfuck.brainfuck import Brainfuck
from brainfuck.bf_input_stream import StringInputStream
from brainfuck.bf_output_stream import StdoutOutputStream

code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
istream = StringInputStream("foo bar")
ostream = StdoutOutputStream()

bf = Brainfuck(code)
bf.run(istream, ostream)
