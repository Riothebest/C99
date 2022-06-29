import os
import shutil
import time

start_time = time.time()
path = input("Enter source floder name: ")
days = input("Number of days before files You want to seperate: ")
days = days*3600
path1 = path+"/"
destination1 = os.mkdir(path1+"Older")
list_of_files= os.listdir(path)

def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
    #int(ctime)
	return ctime

for file in list_of_files:
   
    if days >= get_file_or_folder_age(path):
        shutil.move((path1+file),destination1)