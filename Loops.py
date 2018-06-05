#understanding while loops
num = 0
while num <= 10:
    print("My name is zac")
    num = num + 1

#list
list = []
while(len(list) < 3):
    newName = input("Enter your name").strip().capitalize()
    list.append(newName)
print(list)
print("list is full")

#for loop (print the numbers 1-10 11 is exlcluded)
for i in range(1,11):
    print(i)
