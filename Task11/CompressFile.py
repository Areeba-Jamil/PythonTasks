#Compress the files using python script
#import required modules
import zipfile
import tarfile
import os

#create a new file and write some text
file = open('CompressFile.txt','w+')
file.write('This file must be compressed using python script')
file.close()

#create a new file and write some text
file2 = open('CompressFile2.txt','w+')
file2.write('This file must be compressed using python script')
file2.close()

#Create a zip file
compress_file = zipfile.ZipFile('CompressedTask11.zip','w')
#compress the text file
compress_file.write('CompressFile.txt',compress_type=zipfile.ZIP_DEFLATED)
compress_file.close()

#Compress all files by creating tar
tar_files = tarfile.open("CompressedTarFile.tar.gz", "w:gz")
for files in ['CompressFile.txt','CompressFile2.txt']:
	tar_files.add(files)

tar_files.close()
