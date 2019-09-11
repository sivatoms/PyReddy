
#f = open("File-MyData", 'w') # File Creation
f = open("File-MyData", 'a') # Appending data to file

f.write("Shiva Reddy")

f1 = open("File-MyData",'r') #reading data from a file

print(f1.read())  # Reading data from a file
print(f1.readlines())
f3 = open("IMG_5022.JPG",'r') # give you binary data of images

f4 = open("MyPic2.JPG",'wb') # wb creates new image copy

for i in f3:
    f4.write(i)
#f4.write()  # this will create new imgae
print(f3.read())

#  strip() command will erase all the spaces and new lines in a strig or text file

