#====================================================================
# Copyright (C)2016 William H. Majoros (martiandna@gmail.com).
# This is OPEN SOURxCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
#====================================================================
from __future__ import (absolute_import, division, print_function,     
   unicode_literals, generators, nested_scopes, with_statement)       
from builtins import (bytes, dict, int, list, object, range, str, ascii, 
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import re
from Rex import Rex

######################################################################
# Attributes:
#   hash
# Methods:
#   configFile=ConfigFile(filename)
#   value=configFile.lookup(key)
#   value=configFile.lookupOrDie(key)
#   list=configFile.lookupList(key,sep=", ")
#   list=configFile.lookupListOrDie(key,sep=", ")
# Private methods:
#   self.load(filename)
######################################################################

class ConfigFile:
    """ConfigFile stores variable assignments as key-value pairs
    in a hash
    """
    def __init__(self,filename):
        self.hash={}
        self.load(filename)
        self.rex=Rex()

    def lookupListOrDie(self,key,sep="[,\s]+"):
        value=self.lookupList(key,sep)
        if(value is None):
            raise Exception(key+" not defined in config file\n")
        return value
        
    def lookupList(self,key,sep="[,\s]+"):
        value=self.lookup(key)
        if(value is None): return value
        return self.rex.split(sep,value)
        
    def lookup(self,key):
        return self.hash.get(key)
        #return self.hash[key]

    def lookupOrDie(self,key):
        if(self.hash[key] is None):
            raise Exception(key+" not defined in config file\n")
        return self.hash[key]

    def load(self,filename):
        hash=self.hash
        with open(filename,"r") as fh:
            while(True):
                line=fh.readline()
                if(not line): break
                match=re.search("^([^#]*)#",line);
                if(match): line=match.group(1)
                #match=re.search("^\s*(\S+)\s*=\s*(\S+)",line);
                match=re.search("^\s*(\S+)\s*=\s*(\S+(\s+\S+)*)",line);
                if(match):
                    key=match.group(1)
                    value=match.group(2)
                    hash[key]=value
                    
