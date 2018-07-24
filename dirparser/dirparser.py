import os
import re 
import shutil

yearRe = r"\d{4}"
monthRe = r"\d{2}.(\d{2})"

files = os.listdir(".")

for i in files:
	year = re.search(yearRe, i)
	if year:
		yearDir = year.group(0)
		if not os.path.exists(yearDir):
			os.makedirs(yearDir)
		month = re.search(monthRe, i)
		if month:
			monthDir = year.group(0) + "/" + month.group(1)
			if not os.path.exists(monthDir):
				os.makedirs(monthDir)
			shutil.move(i, monthDir + "/" + i)