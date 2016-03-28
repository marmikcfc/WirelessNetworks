import os
import scipy as scipy
import numpy as np
import difflib
import struct
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


avg_ber_bpsk=[]
avg_ber_qpsk=[]

def getBer(a,b):
	seq=difflib.SequenceMatcher(None,a,b)
	return seq.ratio()

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def mean(ber):
	a =0.0
	for i in range(len(ber)):
		a+=float(ber[i])
	return float(a/len(ber))

def bpsk():
	r=[]
	t=[]

	directory = os.path.join("c:\\","\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\bpsk\\")
	for root,dirs,files in os.walk(directory):
		for file in files:
			if file.endswith(".txt") and file[:2] == "rx":
				r.append(file)
			if file.endswith(".txt") and file[:3] == "trx":
				t.append(file)

	print(t)

	for i in range(0,len(r)):
		ber=[]
		rx=np.loadtxt("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\bpsk\\"+r[i])
		trx=np.loadtxt("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\bpsk\\"+t[i])

		for j in range(0,len(rx)):
			tempBer= getBer(binary(float(rx[j])),binary(float(trx[j])))
			#print str(rx[j]), " ", str(trx[j])
			ber.append(tempBer)

		avg_ber_bpsk.append(abs(float(mean(ber))))


def qpsk():

	r=[]
	t=[]

	directory = os.path.join("c:\\","\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\")
	for root,dirs,files in os.walk(directory):
		for file in files:
			if file.endswith(".txt") and file[:2] == "rx":
				r.append(file)
			if file.endswith(".txt") and file[:3] == "trx":
				t.append(file)

	print(t)

	for i in range(0,len(r)):
		ber=[]
		rx=np.loadtxt("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\"+r[i])
		trx=np.loadtxt("c:\\Users\\Marmik\\Desktop\\WirelessNetworks\\Problem Set 3\\Part 3\\qpsk\\"+t[i])

		for j in range(0,len(rx)):
			tempBer= getBer(binary(float(rx[j])),binary(float(trx[j])))
			#print str(rx[j]), " ", str(trx[j])
			ber.append(tempBer)

		avg_ber_qpsk.append(abs(float(mean(ber))))
	print avg_ber_qpsk


bpsk()
qpsk()

xAxis=[0,1,10,15,20,25,30]

plt.figure(1)
plt.plot(xAxis,avg_ber_bpsk,'r')
plt.plot(xAxis,avg_ber_qpsk,'g')
red_patch = mpatches.Patch(color='red', label='BPSK')
green_patch = mpatches.Patch(color='green', label='QPSK')
plt.legend(handles=[red_patch,green_patch])

plt.ylabel('Average BER')
plt.xlabel('SNR in db')
plt.show()
