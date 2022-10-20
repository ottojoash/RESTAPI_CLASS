#created on oct 20,2022
#@aurthor ottojoash

print("hello world")

#variables

date = 21
pi = 3.14
email = "ottojoash48@outlook.com"
eat = True

print(eat)

#strings

basketballplayer = input("who is your favourite basketball player")

print("my favorite player is",basketballplayer)


#logical operations

yourage = input("how old are you? : ")

birthyear = 2021 - int(yourage)
print(birthyear)

#exerise 
#numberA and numberB
#subtract numberB from numberA
#print result

NumberA = float(input("first"))
numberB = float(input("second"))
sub  = NumberA-numberB

print("result: "+str(sub))
if sub<0:
    print("negative number")
else:
    print("postive number")   


#operations with strings  

otto = "i love programming and i will learn fast"
#upper case
print(otto.upper())
#lower case
print(otto.lower())
#finding a particular letter
print(otto.fing("g"))
#replacing elements
print(otto.replace("love","just","like"))
#finding the character or index of  a word
print(otto.find("programing"))


#artimetic operations
x =5
y = 11
#remainder
print(y%x)
#multiplication
print(y*x)
#addition
print(y+x)

#using variable
x+=y
print(x)

#comparison and logical statements
x= 5>4

print(x)#it will print true or false
#you can also try x= 5==5 or 5!=4 and so on

rent = 550
#logical and /or
print(rent>50 and rent<100)
#or
print(rent>50 and rent<100)

#if  statements
carspeed = 70

if carspeed > 100:
    print("you drive too fast")
elif carspeed <20:
    print("you drive too slow. this is the a highway"
    )
else:
    print("your speed is good")
print("ready")

#execrise
#master degree  required
#more than 2 years of experience

degree = input("what is your degree? master, bachelor or PHD")
experience = input("how many years of experience do you have")

if degree == "Master" or degree = "master" or degree = "PHD"  or degree = "phd":
    if int(experience) >=2:
        print("you are accepted for the interview")
    else:
        print("you dont have enough experince")
else:
    print("you dont have the required degree") 


#loops
#i = 0

#while i <= 5:
#    print(i)
#    i=i+1


temperature = [67,30,70,43,91]
for item in temperature:
    print(item)

numbers = range(10,100,5)

for number in numbers:
    print(number)