#Slicing Strings
info = "hi i am a computer engineer"
#print from 8 to 13 (14 excluded) 
print(info[8:14:])

#how to reverse a string
x = "hello"
print(x[::-1])

#slice the name from the input email
email = input("input your email")
username = email[:email.index("@"):]
domain = email[email.index("@") + 1: email.index("."):]

#print user information
print("Your username is {} and your domain is {}".format(username, domain))
