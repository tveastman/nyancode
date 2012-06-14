#!/usr/bin/env python

import sys
import re

def main():
    input = open(sys.argv[1]).read()
    nyancode = NyanCode()
    nyancode.eval(input)


class NyanCode(object):
    operators = {
        "nyan": "-",
        "NYAN": "+",
        "NYan": "<",
        "nyAN": ">",
        "Nyan": "[",
        "nyaN": "]",
        "NyAN": ",",
        "NYaN": ".",
        }
    def eval(self, input):
        bf = BrainfuckInterpreter()
        bf.eval(self.nyan_to_brainfuck(input))
    def nyan_to_brainfuck(self, input):
        tokens = re.split("(nyan)", input, flags=re.IGNORECASE)[1::2]
        bf = []
        for token in tokens:
            bf.append(self.operators[token])
        return "".join(bf)
    def brainfuck_to_nyan(self, input):
        reverse_operators = dict([(j, i) for i, j in self.operators.items()])
        nyan = []
        for char in input:
            if char in reverse_operators:
                nyan.append(reverse_operators[char])
        return " ".join(nyan)
            
        

class BrainfuckInterpreter(object):
    def __init__(self):
        self.tape = [0]
        self.instructions = []
        self.ptr = 0
        self.iptr = 0
        ## map the jump instructions for 'optimized' bf code :-)
        self.fwd = {}
        self.bck = {}

    @property
    def here(self):
        return self.tape[self.ptr]
    @here.setter
    def here(self, value):
        self.tape[self.ptr] = value

    @property
    def instruction(self):
        return self.instructions[self.iptr]

    def eval(self, input):
        self.parse(input)
        while self.iptr < len(self.instructions):
            self.next()

    def parse(self, input):
        operators = {
            "+": self.plus,
            "-": self.minus,
            ",": self.comma,
            ".": self.period,
            "<": self.lessthan,
            ">": self.greaterthan,
            "[": self.leftbracket,
            "]": self.rightbracket,
            }
        for c in input:
            if c in operators:
                self.instructions.append(operators[c])
                
    def next(self):
        """Execute the next instruction in the program"""
        self.instructions[self.iptr]()
        self.iptr += 1

    def greaterthan(self):
        self.ptr += 1
        ## Double the tape if we've reached the edge
        if len(self.tape) == self.ptr:
            self.tape += [0] * len(self.tape)

    def lessthan(self):
        self.ptr -= 1

    def plus(self):
        self.here += 1

    def minus(self):
        self.here -= 1
        
    def comma(self):
        char = sys.stdin.read(1)
        if not char: 
            return
        self.here = ord(char)

    def period(self):
        sys.stdout.write(chr(self.here))
    
    def _find_matching_bracket(self, inc):
        balance = inc
        ptr = self.iptr
        while True:
            ptr += inc
            if self.instructions[ptr] == self.rightbracket:
                balance -= 1
            elif self.instructions[ptr] == self.leftbracket:
                balance += 1
            if balance == 0:
                return ptr

    def leftbracket(self):
        if self.here != 0:
            return
        elif self.iptr in self.fwd:
            self.iptr = self.fwd[self.iptr]
        else:
            match = self._find_matching_bracket(1)
            self.fwd[self.iptr] = match
            self.iptr = match                

    def rightbracket(self):
        if self.here == 0:
            return
        elif self.iptr in self.bck:
            self.iptr = self.bck[self.iptr]
        else:
            match = self._find_matching_bracket(-1)
            self.bck[self.iptr] = match
            self.iptr = match

if __name__ == "__main__": main()
