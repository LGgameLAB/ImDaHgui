import os


def getFileName():
	done = False
	filename = ""
	while not done:
		filename = str(input("Filename:"))
		try:
			f = open(filename, "rb")
			done = True
			f.close()
		except:
			print("Invalid filename.")
	return filename

def encode(vals):
	filename =  vals[1]
	message = vals[0]
	with open(filename, "ab") as f:
		f.write(bytes(message, "UTF-8"))
		f.close()
	return("Encoding SUCCESS")

def decode(vals):
	filename =  vals[1]
	with open(filename, "rb") as f:
		binaryData = f.read()
		pointerIndex = binaryData.index(bytes.fromhex("FFD9")) + 2
		f.seek(pointerIndex)
		byteData = f.read()

	print(byteData.decode("UTF-8"))
	return byteData.decode("UTF-8")

# def strip():
# 	filename = getFileName()
# 	file = open(filename, "rb")
# 	binary = file.read()
# 	pointerIndex = binary.index(bytes.fromhex("FFD9")) + 2
# 	file.close()
# 	file = open(filename, "rb")
# 	done = False
# 	binaryData = b""
# 	while not done:
# 		byte = file.read(1)
# 		binaryData += byte
# 		pos = file.tell()
# 		if pos == pointerIndex:
# 			done = True
# 			break
# 	file.close()
# 	file = open(filename, "wb")
# 	file.write(binaryData)
# 	file.close()