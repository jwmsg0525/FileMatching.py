#! /usr/bin/python

import hashlib
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
file_many = raw_input("how many do you wana match files >>")
c = range(0,int(file_many)-1)
b = range(1,int(file_many))
a = range(0,int(file_many))
filepath = []
filehash = []

for i in a:
	filepath.append(raw_input("file" + str(i+1) +" path >>"))


for j in a:
	f = open(filepath[j],"r")
	filehash.append(hashlib.sha256(f.read()).hexdigest())
	f.close()

for k in a:
	print "file("+ filepath[k] +") hash : "+ filehash[k]
	
print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "matching file"
if file_many == "1":
	print "If you wana matching file, you should attach files over 2"
for l in c:
	for n in b:
		if l != n:
			if filehash[l] == filehash[n]:
				print "file("+filepath[l]+") and file("+filepath[n]+") is same file!!"
		
			if filehash[l] != filehash[n]:
				print "file("+filepath[l]+") and file("+filepath[n]+") is 'not' same!"
print "-=-=-=-=-=-=--=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
