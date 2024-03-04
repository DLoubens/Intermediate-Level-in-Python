# QR with pyqrcode library
import pyqrcode
name  = "Info: EXAM GRADE,POWER FREE,TEXTURED,LATEX FREE,NON STERILED"

k = pyqrcode.create(name)
k.png('QRcode_eSUPER.png', scale = 10)

import os
os.system('QRcode_eSUPER.png')

# QR with qrcode library

import qrcode
mycode = qrcode.make("Info: EXAM GRADE, POWER FREE,TEXTURED,LATEX FREE,NON STERILED")
mycode.save('mycode_eSUPER.png')

#!pip install pyqrcode
#!pip install pillow

from PIL import Image 

def NewQRGenerator(string):
	"""
	Generates a QR Code and save it in PNG format.
	How a logo will be insert in the code later, some information
will be lost!! In order to prevent it, we use the 'High Redundancy
Algorithm' that allows 30% of lost data that the QR Code will still
work!!.

	Assintotic: O(1)
	"""
	url = pyqrcode.QRCode(string, error='H')
	url.png('qr_code.png', scale=10)
	InsertLogo()


def InsertLogo():
	"""
	Insert a logo inside the QR Code and save the changes in
	PNG format.

	Assintotic: O(1)
	"""
	qr_code = Image.open('qr_code.png')
	
	logo = Image.open('test.png')
	box = (185, 185, 235, 235) # insert position
	qr_code.crop(box)
	region = logo
	region = region.resize((box[2] - box[0], box[3] - box[1]))
	qr_code.paste(region, box)

	qr_code.save('qr_code.png')

NewQRGenerator("https://csfelix.github.io")





