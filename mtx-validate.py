#!/usr/bin/env python
#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Copyright (C)2021 William H. Majoros <bmajoros@alumni.duke.edu>
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
# The above imports should allow this program to run in both Python 2 and
# Python 3.  You might need to update your version of module "future".
import sys
import ProgramName
import gzip
from Rex import Rex
rex=Rex()

#=========================================================================
# main()
#=========================================================================
if(len(sys.argv)!=2):
    exit(ProgramName.get()+" <in.mtx.gz>\n")
(infile,)=sys.argv[1:]

uniq1=None; uniq2=None; sum3=None
keys1=set(); keys2=set()
trueSum3=0
with gzip.open(infile,"rt") as IN:
    line=None
    while(True):
        line=IN.readline()
        if(not rex.find("^%",line)): break
    fields=line.rstrip().split()
    if(len(fields)!=3):
        raise Exception("Wrong number of fields in count header line")
    uniq1=int(fields[0]); uniq2=int(fields[1]); sum3=int(fields[2])

    for line in IN:
        fields=line.rstrip().split()
        if(len(fields)!=3):
            raise Exception("Wrong number of fields")
        keys1.add(fields[0]); keys2.add(fields[1])
        trueSum3+=int(fields[2])
trueUniq1=len(keys1)
trueUniq2=len(keys2)
print(trueUniq1," vs ",uniq1,"\t",trueUniq2," vs ",uniq2,"\t",
      trueSum3," vs ",sum3,sep="")



