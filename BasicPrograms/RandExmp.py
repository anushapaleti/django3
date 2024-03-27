import random
import string

# n=random.randbytes(4)
# print(n)
# print(random.randrange(1,8))
# print(random.randint(100,211))
#---------------Random function---------------------------------
#
# list =["Hari","Surya","Nikhi","Sowji","Saranya"]
# list2 =("Satish","SuryaKiran","Deepak","Naffesa","Gouse")
# list3 ={1:"Kali",2:"Chinna",3:"Mirchji",4:"billa",5:"Salaar"}
# list1 ={"Anushka","Alia","Deepika","Padukone"}
# print(random.choice(list))
# print(random.choice(list2))
# print(random.choice(list3))
# print(random.choice(list1))
# print(list3[1])

#-------------------------sample function---------------------------------
S=10
ran =''.join(random.sample(string.ascii_uppercase +string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print("The randomly generated string is:"+str(ran))
print(ran1)