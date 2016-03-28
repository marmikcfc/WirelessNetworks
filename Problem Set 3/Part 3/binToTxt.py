import os
import scipy as scipy
import numpy as numpy

directory = os.path.join("c:\\","\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\")
for root,dirs,files in os.walk(directory):
    for file in files:
        f=scipy.fromfile(open("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\"+file),dtype="float32")
        scipy.savetxt("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\"+file+".txt",f)