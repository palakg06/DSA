##fo1=open("D:\\f1.txt","r")
##s=fo1.read(8)#reads only 1st 8 characters
##print(s)
##print(fo1.closed)
##print("name:",fo1.name)

##with open("D:\\f1.txt","r") as fo1:
##    s=fo1.read()
##    print(s)
##print(fo1.closed)
##fo1=open("D:\\f1.txt","r")
##s=fo1.readline()
##print(s)
##l1=fo1.readlines()
##print(l1)
##f=open("D:\\f1.txt","w")
##s='''this is a demo of write function
##hellooo
##heyyy\n'''
##f.write(s)
##f.close()
##
##f=open("D:\\f1.txt","a")
##l=["psit\n","psit coe\n","psit che"]
##f.writelines(l)
##f.close()

##f=open("D:\\f1.txt","r")
##s1=f.read(10)
##print(s1)
##print(f.tell())
##f.readline()
##print(f.tell())
##f.seek(5)
##print(f.tell())
##f.readline()
f=open("C:\\Users\\91914\\Downloads\\IMG-20211122-WA0034.jpg",'rb')
s=f.read()
print(s)
f.close()
f1=open("C:\\Users\\91914\\Downloads\\thumb.jpg",'wb')
f1.write(s)
f.close()
