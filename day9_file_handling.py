#Reading data from a file
# f=open("sample.txt","r")
# data=f.read()
# data=f.read(15)
# data=f.readlines()
# print(data[2])
# print(type(data))
# f.close()

#Writing data to a file
# f=open("kashmir.txt","w")
# f=open("kashmir.txt","x")
# f.write("Kashmir paradise on earth.\n")
# f.write("Its snowing in Kashmir right now.\t")
# f.write("The temperature in winter falls upto -10C")
# f.close()

#Appending data to files
# f=open("kashmir.txt","a")
# f.write("Kashmir paradise on earth.\n")
# f.write("Its snowing in Kashmir right now.\n")
# f.write("The temperature in winter falls upto -10C")
# f.close()

# with open("sample.txt","r") as f1:
#     data1=f1.read()
#     # f.write("Hello World")
# with open("kashmir.txt","r") as f2:
#     data2=f2.read()

# with open("merge.txt","w") as f:
#     f.write(data1+"\n"+data2)
    # f.write(data2)

# with open("image.jpg", "rb") as f:
#     data = f.read()
#     print(data)
# with open("image2.jpg","wb") as f2:
#     f2.write(data)

import os
# import math
# if os.path.exists("demo\merge.txt"):
#     print("File Exists")
# else:
#     print("File does not exist")
os.remove("demo.txt")
