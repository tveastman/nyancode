import sys

class BrainfuckInterpreter(object):
    """A Brainfuck interpreter."""

    def __init__(self):
        self.tape = [0]
        self.ptr = 0
        self.iptr = 0
        ## 
        self.fwd = {}
        self.bwd = {}


    def inc_ptr(self):
        self.ptr += 1
        ## Double the tape if we've reached the edge
        if len(self.tape) == self.ptr:
            self.tape += [0] * len(self.ptr)

    @property
    def here(self):
        return self.tape[self.ptr]
    @here.setter
    def here(self, value):
        self.tape[self.ptr] = value
    

    def dec_ptr(self):
        self.ptr -= 1

    def inc_tape(self):
        self.here += 1

    def dec_tape(self):
        self.here -= 1
        
    def read(self):
        self.here = ord(sys.stdin.read(1))

    def write(self):
        sys.stdout.write(chr(self.here))
        
    def jmp_fwd(self):
        if self.here != 0:
            return
        

    def jmp_bck(self):
        pass
