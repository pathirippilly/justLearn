import os
import datetime
import subprocess
# print(os.getcwd())   #gives current working directory
# os.chdir("A:\\") # chnage the current working directory
# os.listdir("A:\\")#list the directories and files in the mentioned directory
# os.mkdir("A:\\test_dir") #create a new directory
# os.makedirs("A:\\test_dir\\test123\\test234\\test123") # create parent directories with child directories
# os.chdir("A:\\test_dir\\test123\\test234\\test123")
# with open("test.txt",'w') as fp:
# pass
# print(os.listdir("A:\\test_dir\\test123\\test234\\test123"))
#os.rename("A:\\test_dir\\test123\\test234\\test123\\test.txt", "A:\\test_dir\\test123\\test234\\test123\\new_test.txt")
#print(os.stat("A:\Things to prepare.txt")) # gives the different statistics of a file
#a=list(os.walk("A:\\mygit")) #this will give a recursive list of tuples containing current_path,directories,files
#l=set(x[0] for x in a)
#print(l)
#os.environ.get('path') #get the value of an environmental variable
#os.environ #returns a dictioanry of all environmental variables
#os.path.join(os.environ ,'filname.txt') #this will create a complete path for file to be created
#os.path.basename("A:\\test_dir\\test123\\test234\\test123\\test.txt") #this will give you file name alone from the path
#os.path.basename("A:\\test_dir\\test123\\test234\\test123\\test.txt") #this will extract and give you directory portion alone
#os.path.split("A:\\test_dir\\test123\\test234\\test123\\test.txt") # this will split directory name and filename in to a tuple
#os.path.exists("A:\\test_dir\\test123\\test234\\test123\\new_test.txt") #check if path exists or not
#os.path.isfile() #check if given path is a file
#os.path.isdir() #check if given path is a directory
#os.path.splitext('ur_path') #this will reurn a tuple of first element as full path including text name exluded of extension and second element as extension
os.path.getsize()