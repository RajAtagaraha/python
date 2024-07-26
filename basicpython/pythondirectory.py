import os
import shutil

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

exit()

#get current working directory
print(os.getcwd())

#change current directory
os.chdir("..")

#change directory
print(os.getcwd())

#list directory
print(os.listdir())

#to create a directory
os.mkdir('test')

#to rename an existing directory
print(os.rename('test','test3'))

#remove directory
os.rmdir('test3')

#create directory in the current folder
os.mkdir('test')

#delete everything inside test directory
shutil.rmtree('test')