#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Copyright (C)2016 William H. Majoros (martiandna@gmail.com).
#=========================================================================
from __future__ import (absolute_import, division, print_function,
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import subprocess
import sys

#=========================================================================
# Attributes:
#   iter = iterator for the subprocess lines
#   p = subprocess
# Instance Methods:
#   pipe=Pipe(command)
#   line=pipe.readline()
#   close()
# Class Methods:
#   output=Pipe.run(command)
#=========================================================================
class Pipe:
    """Pipe reads output from a shell command"""
    def __init__(self,cmd):
        self.p=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True,
                           stderr=subprocess.STDOUT)
        self.iter=iter(self.p.stdout.readline, b'')

    def close(self):
        self.p.terminate()
        
    def readline(self):
        line=next(self.iter,None)
        if(line is None): return None
        line=line.decode(sys.stdout.encoding).rstrip()
        return line

    @classmethod
    def run(cls,cmd):
        line=subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
        line=line.decode(sys.stdout.encoding).rstrip()
        return line

