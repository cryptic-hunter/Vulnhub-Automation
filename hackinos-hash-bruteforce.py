import hashlib

file_name = raw_input("Please enter your file name : ")
i=1

while i in range(101):
        j = str(i)
        resultant = file_name+j
        i+=1
        final = hashlib.md5(resultant.encode())
        print final.hexdigest()