import glob, os
i = 0
for filename in glob.iglob(os.path.join(".", '*')):
	os.rename(filename, str(i) + '.JPEG')
	i = i+1