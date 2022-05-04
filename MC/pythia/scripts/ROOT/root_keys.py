#!/usr/bin/env python

# This script is used to get the ROOT keys stored in a .root file .

from importlib.resources import path
import sys
from ROOT import TFile, gDirectory, TDirectory

def GetAllRootKeys(self):
    klist=[]
    for key in gDirectory.GetListOfKeys():
        path=""
        self.filterkey(key,path,klist)
    return klist

def filterkey(self,key,cpath,klist):
    if key.IsFolder():
        if not cpath.endswith('/') and not cpath == "":
              cpath += '/'
        subfolder = cpath + key.GetName
        self.cd(subfolder)  # cd to subfolder
        for k in gDirectory.GetListOfKeys():
            self.filterkey(k,subfolder,klist)
    else:
        klist.append(cpath + '/' + key.GetName())
        return

TFile.filterkey = filterkey  
TFile.GetListOfKeys = GetAllRootKeys

if len(sys.argv) <= 1; 
      print ("Input file name is missing")
      print ("Usage: root_keys.py <input_file_name>")
      sys.exit()
 
file_name= sys.argv[1]

f = iFile(file_name)

keys = f.GetListOfKeys()

for key in keys:
    object = f.Get(key)
    print (object.ClassName(), ": ", key)

print (len(keys), "Objects Found in ", file_name)      