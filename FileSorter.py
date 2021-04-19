from os import listdir, getcwd, rename, path

DOCUMENTS = "/home/borkson/Documents/"
ARCHIVES = "/home/borkson/Archives/"
PICTURES = "/home/borkson/Pictures"

cwd = getcwd()+'/'
unknownFiles = ""

for file in listdir():
	print(cwd+file)
	fileType = path.splitext(file)[1]
	if file == "UNKNOWN_FILETYPES.txt" or file == "FileSorter.py":
		pass
	elif fileType == ".txt" or fileType == ".pdf":
		rename(cwd+file, DOCUMENTS+file)
	elif fileType == ".xz" or fileType == ".deb":
		rename(cwd+file, ARCHIVES+file)
	elif fileType == ".png" or fileType == ".jpg":
		rename(cwd+file, PICTURES+file)
	else:
		if fileType != "":
			unknownFiles += fileType + '\n'

if unknownFiles != "":
	f = open("UNKNOWN_FILETYPES.txt", "w")
	f.write(unknownFiles)
	f.close()