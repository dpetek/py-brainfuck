from brainfuck.brainfuck import Brainfuck
from brainfuck.input_stream import StringInputStream
from brainfuck.output_stream import StdoutOutputStream
code = """
>,[
    [
        ----------[
            >>>[>>>>]+[[-]+<[->>>>++>>>>+[>>>>]++[->+<<<<<]]<<<]
            ++++++[>------<-]>--[>>[->>>>]+>+[<<<<]>-],<
        ]>
    ]>>>++>+>>[
        <<[>>>>[-]+++++++++<[>-<-]+++++++++>[-[<->-]+[<<<<]]<[>+<-]>]
        >[>[>>>>]+[[-]<[+[->>>>]>+<]>[<+>[<<<<]]+<<<<]>>>[->>>>]+>+[<<<<]]
        >[[>+>>[<<<<+>>>>-]>]<<<<[-]>[-<<<<]]>>>>>>>
    ]>>+[[-]++++++>>>>]<<<<[[<++++++++>-]<.[-]<[-]<[-]<]<,
]
"""

code2 = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
istream = StringInputStream("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
ostream = StdoutOutputStream()
bf = Brainfuck(code2)

bf.run(istream, ostream)

