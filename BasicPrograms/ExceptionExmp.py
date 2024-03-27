'''
while True:
    try:
        n= int(input("Please enter a integer:"))
        m = int(input("Please enter a integer:"))
        z=n/m
        break
    except Exception as e:
        print("Not an integer! Please 123")
        print(e)
    except ValueError:
        print("Not an integer! Please 456")
    finally:
        print("Succesful running")
'''

#---------------------------------------------
try:
    klu1 = open("file.txt","r+")
    try:
        klu1.write("xyzThis is section crt class")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("This file opened successfully")
    klu1.close()